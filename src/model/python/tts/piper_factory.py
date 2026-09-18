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
import os
import subprocess
import tempfile

import numpy as np
import soundfile as sf


from app.models.EngineFactories.tts_engine_factory import EngineTTS
#from tts_engine_factory import EngineTTS


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
                 sample_rate: int = 48000,
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
        # Tracked so stop() can terminate a running piper subprocess.
        self._process = None

    def generate_audio(self, text_input: str = None):
        if text_input is not None:
            self.text_input = text_input

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            temp_path = tmp_file.name

        safe_speed = self.speed if self.speed > 0 else 1.0
        calculated_length_scale = 1.0 / safe_speed

        # FIX: previously "./" + self.model_path + self.engine_name produced
        # "././cores/Engines/Piper-tts/..." (double "./" prefix). Use
        # os.path.join for OS-safe, idempotent path composition.
        model_file = os.path.join(self.model_path, self.engine_name)

        cmd = [
            "piper",
            "--model", model_file,
            "--length-scale", str(calculated_length_scale),
            "--noise-scale", str(self.noise_scale),
            "--noise-w", str(self.noise_w),
            "--sentence-silence", str(self.sentence_silence),
            "--output_file", temp_path
        ]

        self._process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = self._process.communicate(input=self.text_input.encode())
        returncode = self._process.returncode
        self._process = None

        if returncode != 0:
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

    def stop(self):
        """Stop playback AND kill any running piper subprocess.

        Overrides EngineTTS.stop() to also handle the case where stop is
        called during generation (subprocess still running) rather than
        during playback.
        """
        super().stop()
        if self._process is not None:
            try:
                self._process.terminate()
            except Exception:
                # Best-effort; the process may have already exited.
                pass
            self._process = None

    # play() and save_audio() are inherited from EngineTTS.
