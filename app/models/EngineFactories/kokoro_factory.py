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
from kokoro_onnx import Kokoro

from app.models.EngineFactories.tts_engine_factory import EngineTTS
#from tts_engine_factory import EngineTTS


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
                 sample_rate: int = 48000,
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

    def generate_audio(self, text_input: str = None):
        if text_input is not None:
            self.text_input = text_input

        tts = Kokoro(
            model_path=self.model_path,
            voices_path=self.voice_path,
        )

        audio, sample_rate = tts.create(
            text=self.text_input,
            voice=self.voice,
            speed=self.speed,
            lang=self.detect_lang
        )

        if isinstance(audio, list):
            audio = np.concatenate(audio)

        audio = self._apply_volume(audio)
        return audio, sample_rate

    # play(), stop(), save_audio() are inherited from EngineTTS.
    # Kokoro is an in-process ONNX model, so stop() = sd.stop() is sufficient.
