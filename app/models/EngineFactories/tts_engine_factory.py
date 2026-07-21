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
import numpy as np

# Allowed sample rates
ALLOWED_SAMPLE_RATES = [44100, 48000]

import numpy as np
from abc import ABC, abstractmethod

class EngineTTS(ABC):
    def __init__(self, detect_lang: str = "",
                 text_input: str = "",
                 voice: str = "", 
                 speed: float = 1.0, 
                 volume: float = 1.0,
                 model_path: str = "",
                 voice_path: str = "",
                 normalize_audio: bool = False, 
                 format: str = ".wav",
                 sample_rate: int = 48000,
                 output_path: str = ".",
                 **kwargs):
        
        self.detect_lang = detect_lang
        self.text_input = text_input
        self.voice = voice
        self.speed = speed
        self.volume = volume
        self.model_path = model_path
        self.voice_path = voice_path
        self.normalize_audio = normalize_audio
        self.format = format
        self.sample_rate = sample_rate
        self.output_path = output_path
    
        if sample_rate not in ALLOWED_SAMPLE_RATES:
            raise ValueError(
                f"Invalid sample_rate '{sample_rate}'. "
                f"Expected one of: {ALLOWED_SAMPLE_RATES}"
            )
        self.sample_rate = sample_rate


    def _apply_volume(self, 
                      audio
                      ):
        
       
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
    def generate_audio(self,
                       text_input: str = None
                       ):
        
        pass

    @abstractmethod
    def play(self, 
             audio, 
             sample_rate
             ):
        
        pass

    @abstractmethod
    def save_audio(self, 
                   audio, sample_rate,
                   output_wav,
                   normalize_audio: bool = None, 
                   format: str = None, 
                   output_path: str = None
                   ) -> None:
        
        pass

