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
BookModel — Manages book (PDF / EPUB) loading and rendering logic.

Responsibilities:
  - Validate that a selected file is a supported format (PDF, EPUB)
  - Build the appropriate URL or HTML content for the QWebEngineView
  - Extract metadata (title, author) from books when available
  - Convert EPUB to HTML for display in the web engine view

QWebEngineView can render PDFs natively via a local file URL.
For EPUB files, we extract the XHTML content and build a self-contained
HTML page that the engine can display.
"""

import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

# EPUB namespace constants
_EPUB_NS = {
    "container": "urn:oasis:names:tc:opendocument:xmlns:container",
    "opf": "http://www.idpf.org/2007/opf",
    "dc": "http://purl.org/dc/elements/1.1/",
}

SUPPORTED_EXTENSIONS = {".pdf", ".epub"}


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
        return "Books (*.pdf *.epub);;PDF Files (*.pdf);;EPUB Files (*.epub);;All Files (*)"

    # ── URL / HTML generation ───────────────────────────────────

    def build_url_or_html(self, file_path: str) -> dict:
        """Analyze *file_path* and return a dict describing how to load it.

        Returns:
            {
                "type": "pdf" | "epub",
                "url": str | None,     # local file URL for PDFs
                "html": str | None,    # self-contained HTML for EPUBs
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
        elif suffix == ".epub":
            return self._build_epub(path)
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

    # ── EPUB handling ───────────────────────────────────────────

    def _build_epub(self, path: Path) -> dict:
        """Extract content from an EPUB file and build a self-contained
        HTML page for display.

        EPUB is a ZIP archive. We:
          1. Read META-INF/container.xml to find the OPF file
          2. Parse the OPF to find the spine (reading order)
          3. Concatenate all spine items into a single HTML document
          4. Extract Dublin Core metadata (title, author)
        """
        try:
            with zipfile.ZipFile(path, "r") as epub:
                # 1. Locate the OPF file
                opf_path = self._find_opf(epub)

                # 2. Parse the OPF
                opf_content = epub.read(opf_path).decode("utf-8")
                opf_root = ET.fromstring(opf_content)

                # 3. Extract metadata
                self._extract_epub_metadata(opf_root)

                # 4. Build the reading order from the spine
                spine_ids = self._get_spine_item_ids(opf_root)
                manifest = self._get_manifest(opf_root)

                # 5. Read and concatenate spine items
                opf_dir = str(Path(opf_path).parent)
                body_parts: list[str] = []
                stylesheets: list[str] = []

                for item_id in spine_ids:
                    href = manifest.get(item_id)
                    if href is None:
                        continue
                    item_path = f"{opf_dir}/{href}" if opf_dir else href
                    try:
                        raw = epub.read(item_path).decode("utf-8")
                    except KeyError:
                        continue

                    # Separate CSS links for the <head>
                    if item_path.lower().endswith(".css"):
                        stylesheets.append(raw)
                        continue

                    # Extract <body> content from XHTML items
                    body_content = self._extract_body(raw)
                    if body_content:
                        body_parts.append(body_content)

                # 6. Assemble the final HTML
                html = self._assemble_html(stylesheets, body_parts)
                return {
                    "type": "epub",
                    "url": None,
                    "html": html,
                    "title": self._book_title,
                    "author": self._book_author,
                }

        except (zipfile.BadZipFile, ET.ParseError, KeyError) as exc:
            raise ValueError(f"Could not parse EPUB file: {exc}") from exc

    # ── EPUB private helpers ────────────────────────────────────

    @staticmethod
    def _find_opf(epub: zipfile.ZipFile) -> str:
        """Read META-INF/container.xml and return the OPF file path."""
        container_xml = epub.read("META-INF/container.xml").decode("utf-8")
        root = ET.fromstring(container_xml)
        rootfile = root.find(".//container:rootfile", _EPUB_NS)
        if rootfile is None:
            raise ValueError("Invalid EPUB: no rootfile found in container.xml")
        return rootfile.attrib["full-path"]

    def _extract_epub_metadata(self, opf_root: ET.Element) -> None:
        """Extract title and author from the OPF metadata."""
        title_el = opf_root.find(".//opf:metadata/dc:title", _EPUB_NS)
        author_el = opf_root.find(".//opf:metadata/dc:creator", _EPUB_NS)
        self._book_title = title_el.text.strip() if title_el is not None and title_el.text else "Unknown Title"
        self._book_author = author_el.text.strip() if author_el is not None and author_el.text else "Unknown Author"

    @staticmethod
    def _get_spine_item_ids(opf_root: ET.Element) -> list[str]:
        """Return the list of idref values from the spine, in order."""
        spine = opf_root.find("{http://www.idpf.org/2007/opf}spine")
        if spine is None:
            return []
        return [item.attrib.get("idref", "") for item in spine.findall("{http://www.idpf.org/2007/opf}itemref")]

    @staticmethod
    def _get_manifest(opf_root: ET.Element) -> dict[str, str]:
        """Return a dict of item-id → href from the manifest."""
        manifest = opf_root.find("{http://www.idpf.org/2007/opf}manifest")
        if manifest is None:
            return {}
        result: dict[str, str] = {}
        for item in manifest.findall("{http://www.idpf.org/2007/opf}item"):
            item_id = item.attrib.get("id", "")
            href = item.attrib.get("href", "")
            if item_id and href:
                result[item_id] = href
        return result

    @staticmethod
    def _extract_body(xhtml: str) -> str:
        """Extract the content inside <body>…</body> from an XHTML string.
        Falls back to the full string if no <body> tag is found."""
        lower = xhtml.lower()
        start = lower.find("<body")
        if start == -1:
            return xhtml
        # Skip past the opening <body …>
        gt = xhtml.find(">", start)
        if gt == -1:
            return xhtml
        end = lower.rfind("</body>")
        if end == -1:
            return xhtml[gt + 1:]
        return xhtml[gt + 1:end]

    @staticmethod
    def _assemble_html(stylesheets: list[str], body_parts: list[str]) -> str:
        """Build a complete HTML document from collected CSS and body parts."""
        css_block = "\n".join(
            f"<style>\n{css}\n</style>" for css in stylesheets
        )
        body_block = "\n<hr/>\n".join(body_parts)
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>ReadItLoud — EPUB Viewer</title>
{css_block}
<style>
body {{
    font-family: Georgia, "Noto Serif", serif;
    line-height: 1.7;
    max-width: 800px;
    margin: 2em auto;
    padding: 0 1em;
    color: #222;
    background: #fafafa;
}}
h1, h2, h3, h4, h5, h6 {{
    line-height: 1.3;
    margin-top: 1.5em;
}}
img {{
    max-width: 100%;
    height: auto;
}}
hr {{
    border: none;
    border-top: 1px solid #ccc;
    margin: 2em 0;
}}
</style>
</head>
<body>
{body_block}
</body>
</html>"""
