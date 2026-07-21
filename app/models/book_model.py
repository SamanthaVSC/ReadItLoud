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
BookModel — Manages book (PDF loading and rendering logic)

Responsibilities:
  - Validate that a selected file is a supported format for PDF
  - Build the appropriate URL or HTML content for the QWebEngineView
  - Extract metadata (title, author) from books when available

QWebEngineView can render PDFs natively via a local file URL.
"""

import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

SUPPORTED_EXTENSIONS = {".pdf"}

class BookModel:
    """Handles book file validation, content extraction and URL building."""

    def __init__(self) -> None:
        self._current_book_path: str | None = None
        self._book_title: str = ""
        self._book_author: str = ""

    # ── Properties ──────────────────────────────────────────────

    @property
    def current_book_path(self) -> str | None:
        return self._current_book_path

    @property
    def book_title(self) -> str:
        return self._book_title

    @property
    def book_author(self) -> str:
        return self._book_author

    # ── Validation ──────────────────────────────────────────────

    @staticmethod
    def is_supported_file(file_path: str) -> bool:
        """Check whether *file_path* has a supported extension."""
        return Path(file_path).suffix.lower() in SUPPORTED_EXTENSIONS

    @staticmethod
    def filter_string() -> str:
        """Return a QFileDialog filter string for supported book formats."""
        return "Books (*.pdf);;PDF Files (*.pdf);;All Files (*)"

    # ── URL / HTML generation ───────────────────────────────────

    def build_url_or_html(self, file_path: str) -> dict:
        """Analyze *file_path* and return a dict describing how to load it.

        Returns:
            {
                "type": "pdf",
                "url": str | None,     # local file URL for PDFs
                "title": str,
                "author": str,
            }

        Raises:
            ValueError: If the file format is not supported.
            FileNotFoundError: If the file does not exist.
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        self._current_book_path = str(path.resolve())

        suffix = path.suffix.lower()
        if suffix == ".pdf":
            return self._build_pdf(path)
        else:
            raise ValueError(f"Unsupported book format: {suffix}")

    # ── PDF handling ────────────────────────────────────────────

    def _build_pdf(self, path: Path) -> dict:
        """Build a load result for a PDF file.

        QWebEngineView can display PDFs natively when pointed at a
        local file:// URL (requires Qt 6+ with PDF support enabled).
        """
        url = path.as_uri()
        self._book_title = path.stem
        self._book_author = ""
        return {
            "type": "pdf",
            "url": url,
            "html": None,
            "title": self._book_title,
            "author": self._book_author,
        }
