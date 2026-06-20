"""
MediaModel — Manages media file discovery and operations for recordings.

Responsibilities:
  - Scanning cache/records for audio files
  - Returning sorted lists of media file names for display in list widgets
  - Playing audio files (returning the full path for the controller to play)
  - Renaming audio files on disk
  - Deleting audio files from disk
"""

from pathlib import Path

class MediaModel:
    """Handles discovery, playback, renaming and deletion of media (audio) files."""

    SUPPORTED_EXTENSIONS = ("*.mp3", "*.wav")

    def __init__(
        self,
        records_dir: str | Path = "cache/records",
    ) -> None:
        self._records_dir = Path(records_dir)

    # ── Public API — Listing ─────────────────────────────────────

    def list_recorded_media(self) -> list[str]:
        """Return a sorted list of recorded audio file names.

        Returns:
            List of file names (not full paths). If the directory does not
            exist or is empty, returns ['No .mp3 or .wav files found.'].
        """
        return self._scan_directory(self._records_dir)

    # ── Public API — Resolve path ────────────────────────────────

    def resolve_path(self, source: str, filename: str) -> Path | None:
        """Resolve a file name to its full path on disk.

        Args:
            source: Either "recorded".
            filename: The audio file name (e.g. "output.wav").

        Returns:
            The full Path if the file exists, None otherwise.
        """
        directory = self._dir_for_source(source)
        full_path = directory / filename
        return full_path if full_path.exists() else None

    # ── Public API — Playback ────────────────────────────────────

    def get_playback_url(self, source: str, filename: str) -> str | None:
        """Return a file:// URL suitable for QMediaPlayer.

        Args:
            source: "recorded".
            filename: The audio file name.

        Returns:
            A file:// URL string, or None if the file does not exist.
        """
        path = self.resolve_path(source, filename)
        if path is None:
            return None
        return path.resolve().as_uri()          # ← .resolve() convierte a absoluta

    # ── Public API — Rename ──────────────────────────────────────

    def rename_file(self, source: str, old_name: str, new_name: str) -> str:
        """Rename an audio file on disk.

        Args:
            source: "recorded".
            old_name: Current file name (e.g. "output.wav").
            new_name: Desired new file name (e.g. "my_audio.wav").

        Returns:
            The actual new file name (may differ if a collision was resolved).

        Raises:
            FileNotFoundError: If the original file does not exist.
            ValueError: If new_name has no supported extension.
            OSError: If the OS fails to rename the file.
        """
        old_path = self.resolve_path(source, old_name)
        if old_path is None:
            raise FileNotFoundError(f"File not found: {old_name}")

        # Ensure the new name has a supported extension
        new_path = self._dir_for_source(source) / new_name
        new_name = self._ensure_extension(new_path, old_path).name
        new_path = self._dir_for_source(source) / new_name

        # Avoid overwriting: append a numeric suffix if needed
        if new_path.exists() and new_path != old_path:
            stem = new_path.stem
            suffix = new_path.suffix
            counter = 1
            while new_path.exists():
                new_path = new_path.parent / f"{stem}_{counter}{suffix}"
                counter += 1

        old_path.rename(new_path)
        return new_path.name

    # ── Public API — Delete ──────────────────────────────────────

    def delete_file(self, source: str, filename: str) -> None:
        """Permanently delete an audio file from disk.

        Args:
            filename: The audio file name to delete.

        Raises:
            FileNotFoundError: If the file does not exist.
            OSError: If the OS fails to delete the file.
        """
        path = self.resolve_path(source, filename)
        if path is None:
            raise FileNotFoundError(f"File not found: {filename}")
        path.unlink()

    # ── Private helpers ──────────────────────────────────────────

    def _dir_for_source(self, source: str) -> Path:
        """Return the directory Path for the given source identifier."""
        if source == "recorded" or source == "generated":
            return self._records_dir
        else:
            raise ValueError(
                f"Unknown media source: '{source}'. "
                f"Valid values are 'recorded' or 'generated'."
            )

    def _scan_directory(self, directory: Path) -> list[str]:
        """Scan *directory* for supported audio files and return their names."""
        if not directory.exists():
            return ["No .mp3 or .wav files found."]

        media_files: list[Path] = []
        for ext in self.SUPPORTED_EXTENSIONS:
            media_files.extend(directory.glob(ext))

        if not media_files:
            return ["No .mp3 or .wav files found."]

        media_files.sort()
        return [f.name for f in media_files]

    @staticmethod
    def _ensure_extension(new_path: Path, old_path: Path) -> Path:
        """Make sure *new_path* keeps a supported audio extension.

        If the user typed a name without an extension, carry over the
        original file's extension. If they typed a different extension
        (but still .mp3 or .wav), keep their choice.
        """
        supported = {".mp3", ".wav"}
        new_ext = new_path.suffix.lower()
        if new_ext in supported:
            return new_path
        # No supported extension on the new name → carry over the old one
        return new_path.with_suffix(old_path.suffix.lower())
