"""
MainWindowView — Pure View layer for the ReadItLoud main window.

This class is responsible ONLY for:
  1. Setting up the UI (via the auto-generated Ui_mainWindow)
  2. Exposing widget references so the Controller can connect signals
  3. Providing helper methods that modify the UI state

No business logic lives here.  All event handling is delegated to the
Controller via Qt signal/slot connections.
"""

from pathlib import Path
from PySide6.QtCore import QSize, Qt, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWebEngineCore import QWebEngineScript, QWebEngineSettings
from PySide6.QtWidgets import (QFileDialog, QLineEdit, QMainWindow,
                                QMdiSubWindow, QMessageBox, QPushButton,
                                QSizePolicy)
from app.views.ui_mainwindow import Ui_mainWindow

# ── JavaScript / CSS for reader dark mode ───────────────────────
# NOTE: these are plain strings, NOT f-strings.
# Single braces { } are real CSS; double braces {{ }} would be literal
# characters and produce invalid CSS.

_DARK_CSS = (
    "html { filter: invert(1) hue-rotate(180deg); }"
    " img, video, iframe { filter: invert(1) hue-rotate(180deg); }"
)

_JS_INJECT_DARK_STYLE = """
(function() {
  var id = 'ril-dark-override';
  if (document.getElementById(id)) return;
  var s = document.createElement('style');
  s.id = id;
  s.textContent = '%s';
  (document.head || document.documentElement).appendChild(s);
})();
""" % _DARK_CSS

_JS_REMOVE_DARK_STYLE = """
(function() {
  var el = document.getElementById('ril-dark-override');
  if (el) el.remove();
})();
"""

_DARK_MODE_SCRIPT_NAME = "ril-dark-mode"


def _format_playback_time(ms: int) -> str:
    """Convert milliseconds to an MM:SS string."""
    total_seconds = max(0, ms) // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


class MainWindowView(QMainWindow):
    """Thin view wrapper around the Qt Designer-generated UI."""

    # ── Límite máximo de caracteres en el editor ────────────────
    MAX_CHARS = 5000

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("ReadItLoud")

        # Ensure the MDI sub-window for the writer widget is active
        sub_window = self.ui.writer_sw.parentWidget()
        if isinstance(sub_window, QMdiSubWindow):
            self.ui.mdiArea.setActiveSubWindow(sub_window)

        # ── Configure book viewer for local file access ──────────
        self._configure_book_viewer()

        # ── Audio playback setup ─────────────────────────────────
        self._media_player = QMediaPlayer(self)
        self._audio_output = QAudioOutput(self)
        self._media_player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(1.0)

        # Track which source is currently playing ("generated" | "recorded" | None)
        self._playing_source: str | None = None

        # ── Playback time tracking ──────────────────────────────
        self._media_player.positionChanged.connect(self._on_position_changed)
        self._media_player.playbackStateChanged.connect(self._on_playback_state_changed)
        self._media_player.mediaStatusChanged.connect(self._on_media_status_changed)

        # ── Reader dark mode toggle button ──────────────────────
        self._reader_dark_mode: bool = False
        self.toggle_reader_mode_pB = QPushButton(self.ui.Reader)
        self.toggle_reader_mode_pB.setObjectName(u"toggle_reader_mode_pB")
        self.toggle_reader_mode_pB.setText(u"\U0001f319 Dark mode")
        self.toggle_reader_mode_pB.setCheckable(True)
        self.ui.horizontalLayout_4.insertWidget(
            self.ui.horizontalLayout_4.count() - 1,  # before the spacer
            self.toggle_reader_mode_pB,
        )

        # Re-apply dark mode after a new book finishes loading
        self.book_viewer.loadFinished.connect(self._on_book_load_finished)

        # ── Wallpaper label setup ───────────────────────────────
        # Prevent the label from expanding the layout based on the pixmap size.
        # The label will take whatever space the layout gives it and the
        # pixmap will be scaled to fit inside.
        self.ui.image1Label_2.setSizePolicy(
            QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored
        )
        self.ui.image1Label_2.setMinimumSize(1, 1)
        self._wallpaper_pixmap: QPixmap | None = None

        # ── Contador de caracteres en tiempo real ────────────────
        self.editor.textChanged.connect(self._on_editor_text_changed)
        self._update_char_counter()  # Mostrar "0 / 5000" al inicio

    # ── Char counter + limit ─────────────────────────────────────

    def _on_editor_text_changed(self) -> None:
        """Se ejecuta cada vez que cambia el texto del editor.
        Actualiza el counterLabel y aplica el límite de caracteres."""
        text = self.editor.toPlainText()

        if len(text) > self.MAX_CHARS:
            # Truncar el texto al límite
            self.editor.blockSignals(True)       # Evitar loop infinito
            self.editor.setPlainText(text[:self.MAX_CHARS])
            self.editor.blockSignals(False)
            # Mover cursor al final para seguir escribiendo desde ahí
            cursor = self.editor.textCursor()
            cursor.movePosition(cursor.MoveOperation.End)
            self.editor.setTextCursor(cursor)

        self._update_char_counter()

    def _update_char_counter(self) -> None:
        """Actualiza el texto de counterLabel con el formato 'NNN / 5000'."""
        current_len = len(self.editor.toPlainText())
        self.ui.counterLabel.setText(f"{current_len} / {self.MAX_CHARS}")

    # ── Book viewer setup ─────────────────────────────────────────

    def _configure_book_viewer(self) -> None:
        """Enable all the settings QWebEngineView needs to display
        local PDF files and EPUB HTML content."""
        settings = self.book_viewer.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, True)
        # Enable PDF viewer built into Chromium
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PdfViewerEnabled, True)

    # ── Convenience accessors for UI widgets ────────────────────
    # The controller uses these instead of reaching into self.ui directly,
    # keeping the coupling minimal and the intent clear.

    @property
    def editor(self):
        """The main text editor widget."""
        return self.ui.Reader_editText

    @property
    def generated_list(self):
        """List widget showing generated audio files."""
        return self.ui.audioListWidget

    @property
    def book_viewer(self):
        """The QWebEngineView used to display PDFs and EPUBs."""
        return self.ui.book_webEngineView

    # ── Button references (for signal connection) ───────────────

    @property
    def buttons(self) -> dict:
        """Return a dict of button-name → QPushButton for the controller
        to connect signals."""
        return {
            "delete": self.ui.delete_pB,
            "copy": self.ui.copy_pB,
            "cut": self.ui.cut_pB,
            "paste": self.ui.paste_pB,
            "undo": self.ui.undo_pB,
            "redo": self.ui.redo_pB,
            "export": self.ui.export_pB,
            "clear": self.ui.clear_pB,
            "read": self.ui.read_pB,
            "translate": self.ui.translate_pB,
            "transcribe": self.ui.transcibe_pB,
            "check_grammar": self.ui.Check_grammar_pB,
            "theme": self.ui.theme_pB,
            "open_book": self.ui.open_book_bP,
            "upload": self.ui.upload_pB,
            "reload_audio": self.ui.reload_audio_pB,
            # Audio action buttons
            "play": self.ui.play_pause_pB,
            "rename": self.ui.rename_pB,
            # Reader mode toggle
            "toggle_reader_mode": self.toggle_reader_mode_pB,
            # Record actions button
            "record_pause": self.ui.record_pause_pB,
            "stop_record": self.ui.stop_pB,
        }

    # ── UI state helpers ────────────────────────────────────────

    def get_editor_text(self) -> str:
        return self.editor.toPlainText()

    def set_editor_text(self, text: str) -> None:
        self.editor.setText(text)

    def clear_editor(self) -> None:
        self.editor.clear()

    def populate_recorded_list(self, items: list[str]) -> None:
        self.generated_list.clear()
        for item in items:
            self.generated_list.addItem(item)

    # ── Audio list helpers ──────────────────────────────────────

    def get_selected_audio_item(self) -> tuple[str | None, str | None]:
        """Return (source, filename) of the currently selected audio item.

        Checks both list widgets. If the user selected an item in the
        Generated list, returns ("generated", filename). If in the
        Recorded list, returns ("recorded", filename). If nothing is
        selected or the placeholder text is selected, returns (None, None).
        """
        # Check generated list first
        current = self.generated_list.currentItem()
        if current is not None:
            name = current.text()
            if name and not name.startswith("No .mp3"):
                return ("generated", name)

        # Check recorded list
        current = self.generated_list.currentItem()
        if current is not None:
            name = current.text()
            if name and not name.startswith("No .mp3"):
                return ("recorded", name)

        return (None, None)

    def get_active_audio_source(self) -> str | None:
        """Return "generated" or "recorded" depending on which list
        has focus / a current selection, or None if neither."""
        source, _ = self.get_selected_audio_item()
        return source

    def select_audio_item_by_name(self, source: str, filename: str) -> None:
        """Select the item with *filename* in the appropriate list widget."""
        list_widget = self.generated_list if source == "record" else print("It is not work")
        items = list_widget.findItems(filename, Qt.MatchFlag.MatchExactly)
        if items:
            list_widget.setCurrentItem(items[0])

    # ── Audio playback helpers ──────────────────────────────────

    def play_audio(self, url: str, source: str) -> None:
        """Start playback of an audio file given its URL.

        Args:
            url: A file:// URL pointing to the audio file.
            source: "generated" or "recorded" — tracks what's playing.
        """
        self._media_player.stop()
        self.ui.rep_timeLabel.setText("00:00")
        self._media_player.setSource(QUrl(url))
        self._media_player.play()
        self._playing_source = source

    def stop_audio(self) -> None:
        """Stop any currently playing audio."""
        self._media_player.stop()
        self._playing_source = None
        self.ui.rep_timeLabel.setText("00:00")

    def is_audio_playing(self) -> bool:
        """Return True if the media player is currently playing."""
        return (self._media_player.playbackState()
                == QMediaPlayer.PlaybackState.PlayingState)

    # ── Playback time label helpers ─────────────────────────

    def _on_position_changed(self, position: int) -> None:
        """Update rep_timeLabel with the current playback position."""
        self.ui.rep_timeLabel.setText(_format_playback_time(position))

    def _on_playback_state_changed(self, state: QMediaPlayer.PlaybackState) -> None:
        """Reset rep_timeLabel to 00:00 when playback stops."""
        if state == QMediaPlayer.PlaybackState.StoppedState:
            self.ui.rep_timeLabel.setText("00:00")

    def _on_media_status_changed(self, status: QMediaPlayer.MediaStatus) -> None:
        """Reset rep_timeLabel when the media reaches the end."""
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.ui.rep_timeLabel.setText("00:00")

    # ── Rename dialog helper ────────────────────────────────────

    def ask_new_filename(self, current_name: str) -> str | None:
        """Show an input dialog asking the user for a new file name.

        Returns:
            The new name the user typed (may lack extension), or None
            if the user cancelled.
        """
        from PySide6.QtWidgets import QInputDialog
        new_name, ok = QInputDialog.getText(
            self,
            "Rename audio file",
            "New file name:",
            QLineEdit.EchoMode.Normal,
            current_name,
        )
        return new_name.strip() if ok and new_name.strip() else None

    # ── Book viewer helpers ─────────────────────────────────────

    def load_book_url(self, url: str) -> None:
        """Load a local file URL (PDF) into the book viewer."""
        self.book_viewer.setUrl(QUrl(url))

    def load_book_html(self, html: str) -> None:
        """Render self-contained HTML (from EPUB) in the book viewer."""
        self.book_viewer.setHtml(html, QUrl("about:blank"))

    def clear_book_viewer(self) -> None:
        """Reset the book viewer to a blank page."""
        self.book_viewer.setUrl(QUrl("about:blank"))

    def activate_reader_panel(self) -> None:
        """Switch the MDI area to show the Reader sub-window
        (where book_webEngineView lives)."""
        reader_sub = self.ui.Reader.parentWidget()
        if isinstance(reader_sub, QMdiSubWindow):
            self.ui.mdiArea.setActiveSubWindow(reader_sub)
            reader_sub.show()

    # ── Reader dark mode ───────────────────────────────────────

    def toggle_reader_dark_mode(self) -> None:
        """Toggle the reader between light and dark mode.

        Two injection mechanisms work together:
          1. **QWebEngineScript** — persisted in the page's script
             collection so it is automatically re-injected every time a
             new page loads (including the Chromium built-in PDF viewer).
          2. **runJavaScript** — applies the change immediately to the
             page that is already displayed, without a reload.

        The CSS ``filter: invert(1) hue-rotate(180deg)`` inverts all
        colours while the double-inversion on images/videos/iframes
        keeps them looking natural.
        """
        self._reader_dark_mode = not self._reader_dark_mode
        self._apply_reader_mode()

    def _apply_reader_mode(self) -> None:
        """Apply the current reader mode (light / dark) to the web view."""
        page = self.book_viewer.page()
        scripts = page.scripts()

        # ── 1. Manage the persistent QWebEngineScript ───────────
        # Remove any previous dark-mode script first
        for existing in scripts.find(_DARK_MODE_SCRIPT_NAME):
            scripts.remove(existing)

        if self._reader_dark_mode:
            dark_script = QWebEngineScript()
            dark_script.setName(_DARK_MODE_SCRIPT_NAME)
            dark_script.setSourceCode(_JS_INJECT_DARK_STYLE)
            dark_script.setInjectionPoint(
                QWebEngineScript.InjectionPoint.DocumentCreation
            )
            dark_script.setRunsOnSubFrames(True)
            dark_script.setWorldId(
                QWebEngineScript.ScriptWorldId.MainWorld
            )
            scripts.insert(dark_script)

        # ── 2. Also apply immediately via runJavaScript ─────────
        # This changes the page that is already visible without
        # requiring a reload.
        js = _JS_INJECT_DARK_STYLE if self._reader_dark_mode else _JS_REMOVE_DARK_STYLE
        page.runJavaScript(js)

        # ── 3. Update button text ──────────────────────────────
        if self._reader_dark_mode:
            self.toggle_reader_mode_pB.setText(u"\u2600 Light mode")
            self.toggle_reader_mode_pB.setChecked(True)
        else:
            self.toggle_reader_mode_pB.setText(u"\U0001f319 Dark mode")
            self.toggle_reader_mode_pB.setChecked(False)

    # ── Wallpaper helpers ───────────────────────────────────────

    def set_wallpaper(self, image_path: str | Path) -> None:
        """Load an image from *image_path* and display it in image1Label_2.

        The original pixmap is stored so it can be re-scaled every time
        the window is resized.  The label's size policy is set to
        *Ignored* so the pixmap never forces the layout to grow.

        If the file does not exist or cannot be read, the label is
        simply cleared (no crash).
        """
        path = Path(image_path)
        print(f"[Wallpaper] Trying to load: {path} | exists={path.is_file()}")
        if path.is_file():
            pixmap = QPixmap(str(path))
            print(f"[Wallpaper] QPixmap isNull={pixmap.isNull()} | size={pixmap.size()}")
            if not pixmap.isNull():
                self._wallpaper_pixmap = pixmap
                self._rescale_wallpaper()
                return
        # File missing or unreadable — clear the label
        print(f"[Wallpaper] FAILED — clearing label (file not found or invalid)")
        self.ui.image1Label_2.clear()
        self._wallpaper_pixmap = None

    def _rescale_wallpaper(self) -> None:
        """Re-scale the stored wallpaper pixmap to fit the label's
        current size, preserving the aspect ratio.

        If the label hasn't been laid out yet (size ≤ 0), a reasonable
        fallback size is used so the image is still visible on startup.
        """
        if self._wallpaper_pixmap is None or self._wallpaper_pixmap.isNull():
            return

        label_size = self.ui.image1Label_2.size()
        # Before the first layout pass the label may report (0,0)
        if label_size.width() < 2 or label_size.height() < 2:
            label_size = QSize(400, 300)

        scaled = self._wallpaper_pixmap.scaled(
            label_size,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.ui.image1Label_2.setPixmap(scaled)

    # ── Resize event ─────────────────────────────────────────────

    def resizeEvent(self, event) -> None:
        """Re-scale the wallpaper when the window is resized."""
        super().resizeEvent(event)
        if self._wallpaper_pixmap is not None:
            self._rescale_wallpaper()

    def _on_book_load_finished(self, ok: bool) -> None:
        """Re-apply dark mode after a new book finishes loading.

        The QWebEngineScript handles re-injection automatically, but
        for the built-in PDF viewer we also run the JS explicitly as a
        safety net (the PDF viewer may initialise after DocumentCreation)."""
        if ok and self._reader_dark_mode:
            self.book_viewer.page().runJavaScript(_JS_INJECT_DARK_STYLE)
            
    ## ── Record ────────────────────────────────────────────────
    
    