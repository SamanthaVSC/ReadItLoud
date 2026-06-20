"""
TTSModel — High-level model for Text-to-Speech, Translation, Transcription
and Grammar operations.

Responsibilities (future):
  - Read text aloud using an offline TTS engine
  - Translate text between English and Spanish
  - Transcribe audio to text
  - Check grammar and provide feedback
  - Check pronunciation

Concrete engines are injected via the factory or directly, so the model
stays decoupled from any specific implementation.
"""

from typing import Protocol

from app.models.tts_engine_factory import TTSEngine, ModelFactory


class TranslateEngine(Protocol):
    """Protocol for translation backends."""

    def translate(self, text: str, source_lang: str, target_lang: str) -> str: ...

class TranscribeEngine(Protocol):
    """Protocol for transcription backends."""

    def transcribe(self, audio_path: str) -> str: ...


class GrammarEngine(Protocol):
    """Protocol for grammar-check backends."""

    def check(self, text: str) -> list[dict]: ...


class TTSModel:
    """High-level model that orchestrates TTS, translation, transcription
    and grammar checking.  Concrete engines are injected so the model
    stays decoupled from any specific implementation."""

    def __init__(self) -> None:
        self._tts_engine: TTSEngine | None = None
        self._translate_engine: TranslateEngine | None = None
        self._transcribe_engine: TranscribeEngine | None = None
        self._grammar_engine: GrammarEngine | None = None

    # ── Engine setters (dependency injection) ───────────────────

    def set_tts_engine(self, engine: TTSEngine) -> None:
        """Set the TTS engine instance directly."""
        self._tts_engine = engine

    def set_tts_engine_by_name(self, name: str, **kwargs) -> None:
        """Create and set a TTS engine via the ModelFactory registry."""
        self._tts_engine = ModelFactory.create(name, **kwargs)

    def set_translate_engine(self, engine: TranslateEngine) -> None:
        self._translate_engine = engine

    def set_transcribe_engine(self, engine: TranscribeEngine) -> None:
        self._transcribe_engine = engine

    def set_grammar_engine(self, engine: GrammarEngine) -> None:
        self._grammar_engine = engine

    # ── Public API ──────────────────────────────────────────────

    def read_aloud(self, text: str) -> None:
        """Send *text* to the TTS engine for spoken output."""
        if self._tts_engine:
            self._tts_engine.synthesize(text, "cache/records/output.wav")
        else:
            print("[TTSModel] read_aloud — no engine configured")

    def translate(self, text: str, source_lang: str = "en", target_lang: str = "es") -> str:
        """Translate *text* and return the result."""
        if self._translate_engine:
            return self._translate_engine.translate(text, source_lang, target_lang)
        print("[TTSModel] translate — no engine configured")
        return text

    def transcribe(self, audio_path: str) -> str:
        """Transcribe the audio at *audio_path* and return text."""
        if self._transcribe_engine:
            return self._transcribe_engine.transcribe(audio_path)
        print("[TTSModel] transcribe — no engine configured")
        return ""

    def check_grammar(self, text: str) -> list[dict]:
        """Check grammar of *text* and return a list of issues."""
        if self._grammar_engine:
            return self._grammar_engine.check(text)
        print("[TTSModel] check_grammar — no engine configured")
        return []

    def check_pronunciation(self, text: str) -> None:
        """Pronunciation feedback stub."""
        print("[TTSModel] check_pronunciation — not implemented yet")