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

now = datetime.datetime.now()
output_name = f"{now.strftime('%Y%m%d%H%M%S')}.wav"

kokoro_tts = "Kokoro"
piper_tts = "Piper"
es_text = """El español es un idioma muy dificil"""
en_text = """How can I help you today, dear friend?"""

kokoro_attr = {
    "text_input": es_text,
    "voice": "em_santa",
    "speed": 1.0,
    "volume": 1.0,
    "normalize_audio": True,
    "format": ".mp3",
    "output_path": "./cache/records/",
    "model_path": "cores/Engines/kokoro-tts/kokoro-v1.0.onnx",
    "voice_path": "cores/Engines/kokoro-tts/voices-v1.0.bin",
    "dect_lang": "es"
}

piper_attr = {
    "text_input": en_text,
    "speed": 1.0,
    "volume": 1.0,
    "normalize_audio": False,
    "format": ".wav",
    "output_path": "./cache/records/",
    "voice_path": "cores/Engines/Piper-tts/en/en_GB-alan-medium.onnx",
    "dect_lang": "es",
    "voice": "",
    "model_path": "",
    "length_scale": 1,
    "noise_scale": 0.5,
    "noise_w": 0.6,
    "sentence_silence": 0.1
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
    def __init__(self, text_input: str, voice: str, speed: float, volume: float,
                 model_path: str, voice_path: str,
                 normalize_audio: bool = False, format: str = ".wav", 
                 output_path: str = "."):
        self.text_input = text_input
        self.voice = voice
        self.speed = speed
        self.volume = volume
        self.model_path = model_path
        self.voice_path = voice_path
        self.normalize_audio = normalize_audio
        self.format = format
        self.output_path = output_path  # <-- Stored here

    def _apply_volume(self, audio):
        if not isinstance(audio, np.ndarray):
            audio = np.array(audio)
        audio = audio.astype(np.float32)
        audio = audio * self.volume
        return np.clip(audio, -1.0, 1.0)

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
    def __init__(self, text_input, speed, volume, voice_path, dect_lang="", voice="",
                 model_path="", length_scale=1.0, noise_scale=0.5, noise_w=0.6,
                 sentence_silence=0.1, normalize_audio=False, format=".wav", 
                 output_path: str = "."):
        super().__init__(text_input, voice, speed, volume, model_path, voice_path,
                         normalize_audio=normalize_audio, format=format, 
                         output_path=output_path)
        self.length_scale = length_scale
        self.noise_scale = noise_scale
        self.noise_w = noise_w
        self.sentence_silence = sentence_silence
        self.dect_lang = dect_lang

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
        # Apply instance defaults if parameters are not provided
        if normalize_audio is None:
            normalize_audio = self.normalize_audio
        if format is None:
            format = self.format
        if output_path is None:
            output_path = self.output_path

        if normalize_audio:
            max_val = np.max(np.abs(audio))
            if max_val > 0:
                audio = audio / max_val

        # Ensure the directory exists
        if output_path and not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)

        base_name = os.path.splitext(output_wav)[0]
        file_name = base_name + format
        
        # Join the output directory with the file name
        final_output = os.path.join(output_path, file_name)
        sf_format = format.replace('.', '').upper()

        try:
            sf.write(final_output, audio, sample_rate, format=sf_format)
            print(f"Saved audio to: {final_output}")
        except Exception as e:
            print(f"Error saving {sf_format}: {e}. (Note: MP3 requires libsndfile 1.1.0+)")


class KokoroTTS(EngineTTS):
    def __init__(self, text_input, voice, speed, volume, model_path, voice_path,
                 dect_lang: str, normalize_audio=False, format=".wav", 
                 output_path: str = "."):
        self.dect_lang = dect_lang
        super().__init__(text_input, voice, speed, volume, model_path, voice_path,
                         normalize_audio=normalize_audio, format=format, 
                         output_path=output_path)

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
            lang=self.dect_lang
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
        # Apply instance defaults if parameters are not provided
        if normalize_audio is None:
            normalize_audio = self.normalize_audio
        if format is None:
            format = self.format
        if output_path is None:
            output_path = self.output_path

        if normalize_audio:
            max_val = np.max(np.abs(audio))
            if max_val > 0:
                audio = audio / max_val

        # Ensure the directory exists
        if output_path and not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)

        base_name = os.path.splitext(output_wav)[0]
        file_name = base_name + format
        
        # Join the output directory with the file name
        final_output = os.path.join(output_path, file_name)
        sf_format = format.replace('.', '').upper()

        try:
            sf.write(final_output, audio, sample_rate, format=sf_format)
            print(f"Saved audio to: {final_output}")
        except Exception as e:
            print(f"Error saving {sf_format}: {e}. (Note: MP3 requires libsndfile 1.1.0+)")


if __name__ == "__main__":
    """
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
        output_path=kokoro_attr["output_path"]  # <-- Passing it explicitly
    )
    print("Kokoro: Audio played and saved.\n")
    
    
    print("Generating audio with Piper...")
    piper_engine = FactoryTTS.create(piper_tts, **piper_attr)
    audio_p, sr_p = piper_engine.generate_audio()
    print("Playing...")
    piper_engine.play(audio_p, sr_p)
    
    piper_engine.save_audio(
        audio_p,
        sr_p,
        "piper_" + output_name,
        normalize_audio=piper_attr["normalize_audio"],
        format=piper_attr["format"],
        output_path=piper_attr["output_path"]  # <-- Passing it explicitly
    )
    print("Piper: Audio played and saved.")
    """