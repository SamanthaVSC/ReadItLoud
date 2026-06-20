"""Model factory for TTS engines.

This module provides the abstract base class and factory pattern for
creating TTS engine instances. New engines can be added by implementing
the TTSEngine interface and registering them in the factory.
"""

from abc import ABC, abstractmethod
from typing import Any


class TTSEngine(ABC):
    """Abstract base class for all TTS engine implementations.

    Every TTS engine (Piper, Kokoro, Coqui, etc.) must implement this
    interface so the application can treat them uniformly.
    """

    @abstractmethod
    def synthesize(self, text: str, output_path: str, **kwargs: Any) -> str:
        """Convert text to speech and save as an audio file.

        Args:
            text: The input text to synthesize.
            output_path: File path where the audio will be saved.
            **kwargs: Engine-specific parameters (voice, speed, etc.).

        Returns:
            The file path of the generated audio file.
        """

    @abstractmethod
    def list_voices(self) -> list[str]:
        """Return a list of available voice identifiers for this engine."""

    @abstractmethod
    def get_name(self) -> str:
        """Return the human-readable name of this engine."""


class ModelFactory:
    """Factory for creating TTS engine instances by name.

    Usage:
        factory = ModelFactory()
        engine = factory.create("piper")
        engine.synthesize("Hello world", "output.wav")
    """

    _registry: dict[str, type[TTSEngine]] = {}

    @classmethod
    def register(cls, name: str, engine_class: type[TTSEngine]) -> None:
        """Register a TTS engine class under a given name."""
        cls._registry[name.lower()] = engine_class

    @classmethod
    def create(cls, name: str, **kwargs: Any) -> TTSEngine:
        """Create a TTS engine instance by registered name.

        Args:
            name: The registered engine name (e.g., "piper", "kokoro").
            **kwargs: Arguments passed to the engine constructor.

        Returns:
            An instance of the requested TTSEngine.

        Raises:
            ValueError: If no engine is registered under the given name.
        """
        engine_class = cls._registry.get(name.lower())
        if engine_class is None:
            available = ", ".join(cls._registry.keys()) or "(none)"
            raise ValueError(
                f"Unknown TTS engine: '{name}'. Available: {available}"
            )
        return engine_class(**kwargs)

    @classmethod
    def available_engines(cls) -> list[str]:
        """Return a list of all registered engine names."""
        return list(cls._registry.keys())