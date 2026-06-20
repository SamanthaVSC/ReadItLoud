"""
DocumentModel — Handles all document/text file operations.

Responsibilities:
  - Reading text files into the editor
  - Saving editor content to files
  - Browsing for files via dialog paths
  - Editor state (copy, cut, paste, undo, redo, clear)
"""

from pathlib import Path


class DocumentModel:
    """Manages document data and file I/O operations."""

    def __init__(self) -> None:
        self._current_file_path: str | None = None

    # ── Properties ──────────────────────────────────────────────

    @property
    def current_file_path(self) -> str | None:
        return self._current_file_path

    @current_file_path.setter
    def current_file_path(self, value: str | None) -> None:
        self._current_file_path = value

    # ── File reading ────────────────────────────────────────────

    def read_text_file(self, file_path: str) -> str:
        """Read and return the full text content of a file.

        Args:
            file_path: Absolute or relative path to the text file.

        Returns:
            The file contents as a string.

        Raises:
            FileNotFoundError: If the file does not exist.
            OSError: For other I/O errors.
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        return path.read_text(encoding="utf-8")

    def extract_file_name(self, dialog_result: tuple) -> str:
        """Extract just the file name from a QFileDialog result tuple.

        Args:
            dialog_result: The tuple returned by QFileDialog.getOpenFileName.

        Returns:
            The base name of the selected file.
        """
        return Path(dialog_result[0]).name

    # ── File writing ────────────────────────────────────────────

    def save_text_file(self, file_path: str, content: str) -> None:
        """Write text content to a file.

        Args:
            file_path: Destination file path.
            content: Text to write.

        Raises:
            OSError: If the file cannot be written.
        """
        Path(file_path).write_text(content, encoding="utf-8")