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

Author: Samantha Alvarez Hechevarria
Contact: samanthadesktop324@gmail.com
GitHub: https://github.com/SamanthaVSC/ReadItLoud
"""

"""
Record — Captures audio from the default input device with pause/resume
support and saves WAV files to cache/records.

State machine
-------------
    IDLE  ──record_audio()──▶  RECORDING
    RECORDING  ──pause()──▶  PAUSED
    PAUSED  ──resume()──▶  RECORDING
    RECORDING | PAUSED  ──stop()──▶  IDLE  (audio data preserved)

After stop() the captured audio remains in memory until save(filename)
writes it to disk (clearing the buffer) or discard() throws it away.
"""

from datetime import datetime
from enum import Enum
from pathlib import Path

import numpy as np
import sounddevice as sd
import soundfile as sf


class RecordState(Enum):
    """States of the Record state machine."""

    IDLE = "idle"
    RECORDING = "recording"
    PAUSED = "paused"


class Record:
    """Records mono/stereo audio with pause/resume support.

    The audio is captured in chunks by a sounddevice callback running on
    a background thread. Each chunk is appended to ``self.audio_data``;
    on save() they are concatenated into a single numpy array and written
    as a WAV file.
    """

    DEFAULT_RECORDS_DIR = "cache/records"

    def __init__(self, samplerate: int = 44100, channels: int = 1) -> None:
        self.samplerate: int = samplerate
        self.channels: int = channels
        self.audio_data: list[np.ndarray] = []
        self.state: RecordState = RecordState.IDLE
        self.stream = None

    # ── Audio callback (runs on sounddevice's thread) ──────────

    def _callback(self, indata, frames, time_info, status) -> None:
        """Append captured audio while in the RECORDING state.

        Reading ``self.state`` is safe under the GIL; a stale read at
        most drops a single chunk (~tens of ms), which is acceptable.
        """
        if self.state == RecordState.RECORDING:
            self.audio_data.append(indata.copy())

    # ── State transitions ──────────────────────────────────────

    def record_audio(self) -> None:
        """Start a new recording session. Only valid from IDLE."""
        if self.state != RecordState.IDLE:
            return
        self.audio_data = []
        self.state = RecordState.RECORDING
        self.stream = sd.InputStream(
            samplerate=self.samplerate,
            channels=self.channels,
            callback=self._callback,
        )
        self.stream.start()

    def pause(self) -> None:
        """Pause the current recording. Only valid from RECORDING."""
        if self.state == RecordState.RECORDING:
            self.state = RecordState.PAUSED

    def resume(self) -> None:
        """Resume a paused recording. Only valid from PAUSED."""
        if self.state == RecordState.PAUSED:
            self.state = RecordState.RECORDING

    def stop(self) -> None:
        """Stop the recording and close the stream.

        Audio data captured so far is preserved in memory so it can be
        saved with save() or thrown away with discard(). Calling stop()
        from IDLE is a no-op.
        """
        if self.state == RecordState.IDLE:
            return
        self.state = RecordState.IDLE
        if self.stream is not None:
            try:
                self.stream.stop()
                self.stream.close()
            except Exception:
                # Stream may already be stopped/closed; ignore.
                pass
            self.stream = None

    # ── Output ─────────────────────────────────────────────────

    def has_audio(self) -> bool:
        """Return True if there is captured audio data available to save."""
        return bool(self.audio_data)

    def save(self, filename: str | Path) -> str:
        """Write the captured audio to a WAV file.

        Args:
            filename: Destination path. Parent directories are created
                automatically.

        Returns:
            The filename as a string.

        Raises:
            ValueError: If no audio data has been captured.
            OSError: If the file cannot be written.
        """
        if not self.audio_data:
            raise ValueError("No audio data to save")

        final_audio = np.concatenate(self.audio_data, axis=0)
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        sf.write(str(path), final_audio, self.samplerate)

        # Clear the buffer so the next recording starts fresh.
        self.audio_data = []
        return str(path)

    def discard(self) -> None:
        """Discard any captured audio data without writing to disk."""
        self.audio_data = []

    # ── Filename generation ────────────────────────────────────

    @staticmethod
    def generate_filename(directory: str | Path = DEFAULT_RECORDS_DIR) -> str:
        """Generate a timestamped filename like ``record_20260522201545.wav``.

        Uses the current local time. The timestamp follows the
        ``YYYYMMDDHHMMSS`` layout (year, month, day, hour, minute,
        second — no separators inside the date/time block) so that
        files sort alphabetically by recency. The prefix ``record_``
        and ``.wav`` extension are fixed.
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return str(Path(directory) / f"record_{timestamp}.wav")
