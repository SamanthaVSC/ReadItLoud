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
