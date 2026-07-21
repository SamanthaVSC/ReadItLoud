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
import numpy as np
from abc import ABC, abstractmethod
import soundfile as sf
import sounddevice as sd
import subprocess
import tempfile
import os

from app.models.EngineFactories.tts_engine_factory import  EngineTTS

class PiperTTS(EngineTTS):
    def __init__(self, 
                 detect_lang: str = "", 
                 text_input: str = "", 
                 speed: float = 1.0,
                 volume: float = 1.0,
                 format: str = ".wav", 
                 output_path: str = ".", 
                 engine_name: str = "",
                 model_path: str = "./cores/Engines/Piper-tts/",
                 voice_path: str = "",
                 sample_rate: int = 22050,
                 length_scale: float = 1.0, 
                 noise_scale: float = 0.5,
                 noise_w: float = 0.6,
                 sentence_silence: float = 0.1,
                 normalize_audio: bool = False,
                 **kwargs
        ):
        super().__init__(detect_lang, 
                         text_input, 
                         speed=speed,
                         volume=volume,
                         model_path=model_path,
                         voice_path=voice_path,      
                         normalize_audio=normalize_audio,
                         format=format,
                         sample_rate=sample_rate,    
                         output_path=output_path
                        )
        
        self.length_scale = length_scale
        self.noise_scale = noise_scale
        self.noise_w = noise_w
        self.sentence_silence = sentence_silence
        self.engine_name = engine_name
        
    def generate_audio(self,
                       text_input: str = None
                       ):
        
        if text_input is not None:
            self.text_input = text_input

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            temp_path = tmp_file.name

        safe_speed = self.speed if self.speed > 0 else 1.0
        calculated_length_scale = 1.0 / safe_speed

        cmd = [
            "piper",
            "--model", "./" + self.model_path + self.engine_name,
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

    def play(self, 
             audio, 
             sample_rate
             ):
        
        sd.play(audio, sample_rate)
        sd.wait()

    def save_audio(self, 
                   audio, 
                   sample_rate, 
                   output_wav,
                   normalize_audio: bool = None, 
                   format: str = None, 
                   output_path: str = None
                   ) -> None:
        
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

