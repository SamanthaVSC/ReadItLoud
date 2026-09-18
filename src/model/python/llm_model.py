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
Responsibilities:
  - Translate text between English and Spanish
  - Transcribe audio to text
  - Check grammar and provide feedback
  - Check pronunciation

Concrete engines are injected via the factory or directly, so the model
stays decoupled from any specific implementation.
"""
import whisper
import language_tool_python as tl

from faster_whisper import WhisperModel
from jiwer import wer

class FasterWhisper:
    def __init__(self, model = "cores/audio qualifiers/faster-whisper/faster-whisper-base", device="cpu", compute_type="int8", expected_text='', audio_file=''):
        self.model = model
        self.device = device
        self.compute_type = compute_type
        self.expected_text = expected_text
        self.audio_file = audio_file

    def qualifier(self) -> str:
        self.model_instance = WhisperModel(self.model, device=self.device, compute_type=self.compute_type)
        segments, info = self.model_instance.transcribe(self.audio_file)
        transcription = " ".join([seg.text for seg in segments])
        error = wer(self.expected_text.lower(), transcription.lower())
        score = (1 - error) * 100
        return f"Score: {score:.2f}%"

class TranslateEngine:
    def translate(self, text: str, source_lang: str, target_lang: str) -> str: ...

class Whisper:
    def __init__(self, 
                 model_path: str="./cores/audio transcription/whisper/models/base.pt", 
                 device: str="cpu", 
                 audio_input: str = '',
                ):
        self.model_path = model_path
        self.device = device
        self.audio_input = audio_input

    def transcribe(self) -> str:
        self.model = whisper.load_model(self.model_path, device=self.device)
        return self.model.transcribe(self.audio_input)["text"]

class GrammarChecker:
    def __init__(self, text_input, lang):
        self.text_input = text_input
        self.lang = lang

    def output_corrections(self):
        tool = tl.LanguageTool(self.lang)
        corrections = tool.check(self.text_input)
        for error in corrections:
            return error
        if not corrections:
            return "Nothing to correct"
        else:
            return corrections

# Example usage with one of your models:
if __name__ == "__main__":
    # Choose which model to test
   
    model_path = "./../../cores/audio qualifiers/faster-whisper/faster-whisper-base"
    
    # Configuration
    qualifier_test = FasterWhisper(
        model=model_path,
        device="cuda",  # or "cuda" if you have GPU
        compute_type="int8",  # Options: "int8", "float16", "float32"
        expected_text="Hola, soy una voz artificial. Esto es una prueba, probando, probando. ¿Cómo se escucha?",
        audio_file="../../cache/records/Piper_20260714030617.wav"  # or .mp3, .flac, etc.
    )
    
    
    # Run the qualification test
    result = qualifier_test.qualifier()
    print(result)
   
    
    #check1 = GrammarChecker(text_input="Do you want being there?", lang="en")
    #check1.output_corrections()

    #whisper1 = Whisper(model_path="./cores/audio transcription/whisper/models/medium.pt", device="cpu",audio_input="app/models/English af_bella.wav")
    #print(whisper1.transcribe())