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

import sounddevice as sd
import soundfile as sf
import numpy as np
import time

class Record:
    def __init__(self, samplerate=44100, channels=1):
        self.samplerate = samplerate
        self.channels = channels
        self.audio_data = []
        self.is_recording = False
        self.is_paused = False
        self.stream = None

    def _callback(self, indata, frames, time_info, status):
        # sounddevice calls this continuously in the background
        if self.is_recording and not self.is_paused:
            self.audio_data.append(indata.copy())

    def start(self):
        self.audio_data = []
        self.is_recording = True
        self.is_paused = False
        self.stream = sd.InputStream(samplerate=self.samplerate, channels=self.channels, callback=self._callback)
        self.stream.start()

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def stop_and_save(self, filename):
        self.is_recording = False
        self.stream.stop()
        self.stream.close()
        
        if self.audio_data:
            final_audio = np.concatenate(self.audio_data, axis=0)
            sf.write(filename, final_audio, self.samplerate)


# --- Simple Execution Example ---
if __name__ == "__main__":
    rec = SimpleRecorder(samplerate=44100, channels=1)

    print("Starting recording...")
    rec.start()

    print("Recording for 2 seconds...")
    time.sleep(2)

    print("Pausing for 2 seconds (no audio will be recorded)...")
    rec.pause()
    time.sleep(2)

    print("Resuming and recording for 2 more seconds...")
    rec.resume()
    time.sleep(2)

    print("Stopping and saving to 'output.wav'...")
    rec.stop_and_save("record.wav")
    
    print("Done!")
