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
import os
from kokoro_onnx import Kokoro
import sounddevice as sd
import soundfile as sf

from app.models.EngineFactories.tts_engine_factory import EngineTTS

class KokoroTTS(EngineTTS):
    def __init__(self, 
                 detect_lang: str = "",
                 text_input: str = "",
                 voice: str = "", 
                 speed: float = 1.0,
                 volume: float = 1.0, 
                 model_path: str = "./cores/Engines/kokoro-tts/kokoro-v1.0.onnx", 
                 voice_path: str = "./cores/Engines/kokoro-tts/voices-v1.0.bin",
                 normalize_audio: bool = False, 
                 format: str = ".wav", 
                 output_path: str = ".", 
                 sample_rate: int = 22050,
                 **kwargs):
        
        super().__init__(detect_lang,
                         text_input, 
                         voice, 
                         speed,
                         volume,
                         model_path=model_path,
                         voice_path=voice_path,
                         normalize_audio=normalize_audio,
                         format=format, 
                         output_path=output_path,
                         sample_rate=sample_rate)

    def generate_audio(self, 
                       text_input: str = None
                           ):
        
        if text_input is not None:
            self.text_input = text_input

        tts = Kokoro(
            model_path= self.model_path,
            voices_path= self.voice_path,
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
