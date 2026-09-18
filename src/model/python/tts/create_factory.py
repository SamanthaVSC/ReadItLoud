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
import time
import threading
from abc import ABC, abstractmethod

from app.models.EngineFactories.piper_factory import PiperTTS
from app.models.EngineFactories.kokoro_factory import KokoroTTS
#from piper_factory import PiperTTS
#from kokoro_factory import KokoroTTS

kokoro_tts = "Kokoro"
piper_tts = "Piper"

es_text = """El español es un idioma muy dificil"""
en_text = """How can I help you today, dear friend?"""

kokoro_attr = {
    "text_input": en_text,
    "voice": "af_bella",
    "speed": 0.9,
    "volume": 1.0,
    "normalize_audio": True,
    "format": ".mp3",
    "output_path": "./cache/records/",
    "model_path": "./../../../cores/Engines/kokoro-tts/kokoro-v1.0.onnx",
    "voice_path": "./../../../cores/Engines/kokoro-tts/voices-v1.0.bin",
    "detect_lang": "en-us",
    "sample_rate": 48000,
}

piper_attr = {
    "engine_name": "en_GB-southern_english_female-low.onnx",
    "text_input": en_text,
    "speed": 1.0,
    "volume": 1.0,
    "normalize_audio": False,
    "format": ".wav",
    "output_path": "./cache/records",
    "detect_lang": "en",
    "voice": "",
    "model_path": "./../../../cores/Engines/Piper-tts/",
    "sample_rate": 44100,
}


class FactoryTTS:
    @classmethod
    def create(cls, type_str, **attrs):
        if type_str == "Kokoro":
            return KokoroTTS(**attrs)
        elif type_str == "Piper":
            return PiperTTS(**attrs)
        raise ValueError(f"Unknown TTS type: {type_str}")

if __name__ == "__main__":
    
    print("Generating audio with Piper...")
    piper_engine = FactoryTTS.create(piper_tts, **piper_attr)
    audio_p, sr_p = piper_engine.generate_audio()

    # print("Playing on worker thread...")
    # t = threading.Thread(target=piper_engine.play, args=(audio_p, sr_p), daemon=True)
    # t.start()

    # time.sleep(1)            # let it play for 1 second
    # print("Stopping...")
    # piper_engine.stop()      # kills playback; sd.wait() in worker returns early
    # #t.join(timeout=2)        # wait for worker to exit cleanly
    # print("Stopped.")
    piper_engine.save_audio(audio=audio_p, sample_rate=sr_p, output_wav="Test1", format=".wav", normalize_audio=False)
    '''
    print("Piper: Audio played and saved")
    
    print("Generating audio with Kokoro...")
    kokoro_engine = FactoryTTS.create(kokoro_tts, **kokoro_attr)
    audio_k, sr_k = kokoro_engine.generate_audio()

    #print("Playing on worker thread...")
    #t = threading.Thread(target=kokoro_engine.play, args=(audio_k, sr_k), daemon=True)
    #t.start()
    
    kokoro_engine.save_audio(audio=audio_k, sample_rate=sr_k, output_wav="Test", format="mp3")

    time.sleep(1)
    print("Stopping...")
    kokoro_engine.stop()
    #t.join(timeout=2)
    print("Stopped.")
    '''