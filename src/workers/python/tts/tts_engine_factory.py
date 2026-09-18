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

import os
import numpy as np
import sounddevice as sd
import soundfile as sf

from abc import ABC, abstractmethod

# Allowed sample rates
ALLOWED_SAMPLE_RATES = [44100, 48000]


class EngineTTS(ABC):
    """Abstract base for all TTS engines.

    Provides shared state, shared audio helpers (_apply_volume, _resample),
    and concrete implementations of playback (play/stop) and persistence
    (save_audio) that are identical across engines. Subclasses only need
    to implement generate_audio(). Engines that hold extra resources
    (e.g. Piper's subprocess) may override stop() and chain via
    super().stop().
    """

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
                 output_path: str = "./cache/records",
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
        self.output_path = output_path

        if sample_rate not in ALLOWED_SAMPLE_RATES:
            raise ValueError(
                f"Invalid sample_rate '{sample_rate}'. "
                f"Expected one of: {ALLOWED_SAMPLE_RATES}"
            )
        self.sample_rate = sample_rate

        # Playback state
        self._is_playing = False

    # ---- Shared audio helpers -------------------------------------------------

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

    # ---- Shared playback control ---------------------------------------------
    # Concrete (non-abstract): playback is pure sounddevice work and does not
    # depend on which engine produced the audio. Subclasses inherit these
    # as-is. Engines with extra resources (e.g. Piper's subprocess) may
    # override stop() and chain via super().stop().

    def play(self, audio, sample_rate):
        """Play a numpy waveform through the default output device.

        Blocks the calling thread until playback finishes or stop() is
        called from another thread (in which case sd.wait() returns early).
        """
        self._is_playing = True
        try:
            sd.play(audio, sample_rate)
            sd.wait()
        finally:
            self._is_playing = False

    def stop(self):
        """Stop any currently playing audio. Safe to call when not playing."""
        sd.stop()
        self._is_playing = False

    # ---- Shared persistence ---------------------------------------------------

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

    # ---- Engine-specific contract --------------------------------------------

    @abstractmethod
    def generate_audio(self, text_input: str = None):
        """Synthesize speech. Must return (audio_np, sample_rate)."""
        pass
