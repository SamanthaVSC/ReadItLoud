"""
ReadItLoud — Desktop application for language learning through
reading documents with speech synthesis (TTS), pronunciation feedback
and integrated grammar correction.

Copyright (C) 2026 Samantha Alvarez Hechevarría

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Author: Samantha Alvarez Hechevarría
Contact: samanthadesktop324@gmail.com
GitHub: https://github.com/SamanthaVSC/ReadItLoud
"""

"""
ReadItLoud — Desktop application for language learning through
reading documents with speech synthesis (TTS), pronunciation feedback
and integrated grammar correction.
...
"""

import sys
import io
import numpy as np
from abc import ABC, abstractmethod
from kokoro_onnx import Kokoro
import soundfile as sf
import sounddevice as sd
import subprocess
import datetime
import tempfile
import os

kokoro_tts = "Kokoro"
piper_tts = "Piper"
es_text = """El español es un idioma muy dificil"""
en_text = """How can I help you today, dear friend?"""

# Allowed sample rates
ALLOWED_SAMPLE_RATES = [44100, 48000]

kokoro_attr = {
    "text_input": en_text,
    "voice": "af_bella",
    "speed": 1.0,
    "volume": 1.0,
    "normalize_audio": True,
    "format": ".mp3",
    "output_path": "./cache/records/",
    "model_path": "cores/Engines/kokoro-tts/kokoro-v1.0.onnx",
    "voice_path": "cores/Engines/kokoro-tts/voices-v1.0.bin",
    "detect_lang": "en-us",
    "sample_rate": 48000,
}

piper_attr = {
    "text_input": en_text,
    "speed": 1.0,
    "volume": 1.0,
    "normalize_audio": False,
    "format": ".wav",
    "output_path": "./cache/records/",
    "detect_lang": "en",
    "voice": "",
    "model_path": "",
    "length_scale": 1,
    "noise_scale": 0.5,
    "noise_w": 0.6,
    "sentence_silence": 0.1,
    "sample_rate": 48000,
}


class FactoryTTS:
    @classmethod
    def create(cls, type_str, **attrs):
        if type_str == "Kokoro":
            return KokoroTTS(**attrs)
        elif type_str == "Piper":
            return PiperTTS(**attrs)
        raise ValueError(f"Unknown TTS type: {type_str}")


class EngineTTS(ABC):
    def __init__(self, detect_lang: str = "", text_input: str = "", voice: str = "", 
                 speed: float = 1.0, volume: float = 1.0,
                 model_path: str = "", voice_path: str = "",
                 normalize_audio: bool = False, format: str = ".wav", 
                 output_path: str = ".", sample_rate: int = 48000, **kwargs):
        self.text_input = text_input
        self.voice = voice
        self.speed = speed
        self.volume = volume
        self.model_path = model_path
        self.voice_path = voice_path
        self.normalize_audio = normalize_audio
        self.format = format
        self.output_path = output_path
        self.detect_lang = detect_lang
        
        if sample_rate not in ALLOWED_SAMPLE_RATES:
            raise ValueError(
                f"Invalid sample_rate '{sample_rate}'. "
                f"Expected one of: {ALLOWED_SAMPLE_RATES}"
            )
        self.sample_rate = sample_rate

    def _apply_volume(self, audio):
        if not isinstance(audio, np.ndarray):
            audio = np.array(audio)
        audio = audio.astype(np.float32)
        audio = audio * self.volume
        return np.clip(audio, -1.0, 1.0)

    def _resample(self, audio, orig_sr, target_sr):
        if orig_sr == target_sr:
            return audio.astype(np.float32)

        audio = np.asarray(audio, dtype=np.float32)

        if audio.ndim == 2:
            num_channels = audio.shape[1]
            resampled_channels = []
            for ch in range(num_channels):
                num_samples = int(len(audio) * target_sr / orig_sr)
                resampled = np.interp(
                    np.linspace(0, len(audio) - 1, num_samples),
                    np.arange(len(audio)),
                    audio[:, ch]
                )
                resampled_channels.append(resampled)
            return np.column_stack(resampled_channels)
        else:
            num_samples = int(len(audio) * target_sr / orig_sr)
            resampled = np.interp(
                np.linspace(0, len(audio) - 1, num_samples),
                np.arange(len(audio)),
                audio
            )
            return resampled.astype(np.float32)

    @abstractmethod
    def generate_audio(self, text_input: str = None):
        pass

    @abstractmethod
    def play(self, audio, sample_rate):
        pass

    @abstractmethod
    def save_audio(self, audio, sample_rate, output_wav,
                   normalize_audio: bool = None, format: str = None, 
                   output_path: str = None) -> None:
        pass


class PiperTTS(EngineTTS):
    def __init__(self, detect_lang: str = "", text_input: str = "", voice: str = "", 
                 speed: float = 1.0, volume: float = 1.0, voice_path: str = "", model_path: str = "",
                 length_scale=1.0, noise_scale=0.5, noise_w=0.6,
                 sentence_silence=0.1, normalize_audio=False, format=".wav", 
                 output_path: str = ".", sample_rate: int = 48000, **kwargs):
        super().__init__(detect_lang, text_input, voice, speed, volume, model_path, voice_path,
                         normalize_audio=normalize_audio, format=format, 
                         output_path=output_path, sample_rate=sample_rate)
        self.length_scale = length_scale
        self.noise_scale = noise_scale
        self.noise_w = noise_w
        self.sentence_silence = sentence_silence

    def generate_audio(self, text_input: str = None):
        if text_input is not None:
            self.text_input = text_input

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            temp_path = tmp_file.name

        safe_speed = self.speed if self.speed > 0 else 1.0
        calculated_length_scale = 1.0 / safe_speed

        cmd = [
            "piper",
            "--model", "./" + self.voice_path,
            "--length-scale", str(calculated_length_scale),
            "--noise-scale", str(self.noise_scale),
            "--noise-w", str(self.noise_w),
            "--sentence-silence", str(self.sentence_silence),
            "--output_file", temp_path
        ]

        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate(input=self.text_input.encode())

        if process.returncode != 0:
            try:
                os.remove(temp_path)
            except OSError:
                pass
            print("Error:", stderr.decode())
            raise RuntimeError(f"Piper error: {stderr.decode()}")

        audio, sample_rate = sf.read(temp_path)

        try:
            os.remove(temp_path)
        except OSError:
            pass

        audio = self._apply_volume(audio)
        return audio, sample_rate

    def play(self, audio, sample_rate):
        sd.play(audio, sample_rate)
        sd.wait()

    def save_audio(self, audio, sample_rate, output_wav,
                   normalize_audio: bool = None, format: str = None, 
                   output_path: str = None) -> None:
        if normalize_audio is None:
            normalize_audio = self.normalize_audio
        if format is None:
            format = self.format
        if output_path is None:
            output_path = self.output_path

        audio = self._resample(audio, sample_rate, self.sample_rate)
        sample_rate = self.sample_rate

        if normalize_audio:
            max_val = np.max(np.abs(audio))
            if max_val > 0:
                audio = audio / max_val

        if output_path and not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)

        base_name = os.path.splitext(output_wav)[0]
        file_name = base_name + format
        final_output = os.path.join(output_path, file_name)
        sf_format = format.replace('.', '').upper()

        try:
            sf.write(final_output, audio, sample_rate, format=sf_format)
            print(f"Saved audio to: {final_output} (sample_rate={sample_rate})")
        except Exception as e:
            print(f"Error saving {sf_format}: {e}. (Note: MP3 requires libsndfile 1.1.0+)")


class KokoroTTS(EngineTTS):
    def __init__(self, detect_lang: str = "", text_input: str = "", voice: str = "", 
                 speed: float = 1.0, volume: float = 1.0, 
                 model_path: str = "cores/Engines/kokoro-tts/kokoro-v1.0.onnx", 
                 voice_path: str = "cores/Engines/kokoro-tts/voices-v1.0.bin",
                 normalize_audio: bool = False, format: str = ".wav", 
                 output_path: str = ".", sample_rate: int = 48000, **kwargs):
        super().__init__(detect_lang, text_input, voice, speed, volume, model_path, voice_path,
                         normalize_audio=normalize_audio, format=format, 
                         output_path=output_path, sample_rate=sample_rate)

    def generate_audio(self, text_input: str = None):
        if text_input is not None:
            self.text_input = text_input

        tts = Kokoro(
            model_path="./" + self.model_path,
            voices_path="./" + self.voice_path,
        )

        audio, sample_rate = tts.create(
            text=self.text_input,
            voice=self.voice,
            speed=self.speed,
            lang=self.detect_lang  # Fixed property name
        )

        if isinstance(audio, list):
            audio = np.concatenate(audio)

        audio = self._apply_volume(audio)
        return audio, sample_rate

    def play(self, audio, sample_rate):
        sd.play(audio, sample_rate)
        sd.wait()

    def save_audio(self, audio, sample_rate, output_wav,
                   normalize_audio: bool = None, format: str = None, 
                   output_path: str = None) -> None:
        if normalize_audio is None:
            normalize_audio = self.normalize_audio
        if format is None:
            format = self.format
        if output_path is None:
            output_path = self.output_path

        audio = self._resample(audio, sample_rate, self.sample_rate)
        sample_rate = self.sample_rate

        if normalize_audio:
            max_val = np.max(np.abs(audio))
            if max_val > 0:
                audio = audio / max_val

        if output_path and not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)

        base_name = os.path.splitext(output_wav)[0]
        file_name = base_name + format
        final_output = os.path.join(output_path, file_name)
        sf_format = format.replace('.', '').upper()

        try:
            sf.write(final_output, audio, sample_rate, format=sf_format)
            print(f"Saved audio to: {final_output} (sample_rate={sample_rate})")
        except Exception as e:
            print(f"Error saving {sf_format}: {e}. (Note: MP3 requires libsndfile 1.1.0+)")

"""
if __name__ == "__main__":
    
    print("Generating audio with Kokoro...")
    kokoro_engine = FactoryTTS.create(kokoro_tts, **kokoro_attr)
    audio_k, sr_k = kokoro_engine.generate_audio()
    kokoro_engine.play(audio_k, sr_k)
    
    kokoro_engine.save_audio(
        audio_k,
        sr_k,
        "kokoro_" + output_name,
        normalize_audio=kokoro_attr["normalize_audio"],
        format=kokoro_attr["format"],
        output_path=kokoro_attr["output_path"],
        sample_rate=kokoro_attr["sample_rate"]
    )
    print("Kokoro: Audio played and saved.\n")
    
    
    print("Generating audio with Piper...")
    piper_engine = FactoryTTS.create(piper_tts, **piper_attr)
    audio_p, sr_p = piper_engine.generate_audio()
    prin                        "model_path": "cores/Engines/kokoro-tts/kokoro-v1.0.onnx",
                        "voice_path": "cores/Engines/kokoro-tts/voices-v1.0.bin",t(f"Original sample rate from Piper: {sr_p}")
    print("Playing...")
    piper_engine.play(audio_p, sr_p)
    
    piper_engine.save_audio(
        audio_p,
        sr_p,
        "piper_" + output_name,
        normalize_audio=piper_attr["normalize_audio"],
        format=piper_attr["format"],
        output_path=piper_attr["output_path"],
        sample_rate=piper_attr["sample_rate"]
    )
    print(f"Piper: Audio played and saved")
    """