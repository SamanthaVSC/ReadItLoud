"""Business logic for ReadItLoud.

This module contains framework-independent business rules for the
application. It coordinates between the core layer (TTS engines,
extractors) and the presentation layer (presenters).

No UI or framework-specific imports belong here.
"""

from cores.model_factory import ModelFactory


class AppLogic:
    """Central business logic coordinator for ReadItLoud.

    This class encapsulates the core use cases of the application:
    synthesizing speech, evaluating pronunciation, and extracting text.
    Presenters call into this class; it never imports or references
    the UI directly.
    """

    def __init__(self) -> None:
        """Initialize the application logic with a model factory."""
        self.factory = ModelFactory()

    def synthesize_speech(
        self, text: str, engine_name: str, output_path: str, **kwargs
    ) -> str:
        """Synthesize speech from text using the specified engine.

        Args:
            text: The text to convert to speech.
            engine_name: Name of the TTS engine (e.g., "piper").
            output_path: Where to save the generated audio.
            **kwargs: Additional engine-specific parameters.

        Returns:
            Path to the generated audio file.
        """
        engine = self.factory.create(engine_name)
        return engine.synthesize(text, output_path, **kwargs)

    def get_available_voices(self, engine_name: str) -> list[str]:
        """Get available voices for a given engine.

        Args:
            engine_name: Name of the TTS engine.

        Returns:
            List of voice identifiers.
        """
        engine = self.factory.create(engine_name)
        return engine.list_voices()
