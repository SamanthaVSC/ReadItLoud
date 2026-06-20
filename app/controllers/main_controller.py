"""
MainController — Mediates between the View and the Models.

Responsibilities:
  - Connect every UI signal (button clicks, etc.) to the appropriate handler
  - Delegate business logic to the correct Model
  - Update the View based on Model results
  - Manage dialog interactions (file open/save, confirmation messages)

The Controller never manipulates widgets directly — it calls View helper
methods instead.  The View never calls Model methods — the Controller
does that on its behalf.
"""

from PySide6.QtWidgets import QFileDialog, QMessageBox
from qt_material import apply_stylesheet

from app.views.main_window import MainWindowView
from app.models.document_model import DocumentModel
from app.models.theme_model import ThemeModel
from app.models.media_model import MediaModel
from app.models.llm_model import TTSModel
from app.models.book_model import BookModel
from app.models.record_model import Record


class MainController:
    """Central controller wiring the ReadItLoud UI to its domain models."""

    def __init__(self, view: MainWindowView, app) -> None:
        self._view = view
        self._app = app  # QApplication reference (needed for theme application)

        # ── Instantiate models ──────────────────────────────────
        self._doc_model = DocumentModel()
        self._theme_model = ThemeModel()
        self._media_model = MediaModel()
        self.llm_model = TTSModel()
        self._book_model = BookModel()
        self.record = Record()

        # ── Wire signals ────────────────────────────────────────
        self._connect_signals()

    # ── Public lifecycle ────────────────────────────────────────

    def apply_initial_theme(self) -> None:
        """Apply the persisted theme and its wallpaper on startup."""
        theme_path, invert = self._theme_model.apply_initial()
        apply_stylesheet(self._app, theme=theme_path, invert_secondary=invert)
        self._view.set_wallpaper(self._theme_model.wallpaper_path)

    # ── Signal wiring ───────────────────────────────────────────

    def _connect_signals(self) -> None:
        btns = self._view.buttons

        # Edit operations
        btns["delete"].clicked.connect(self._on_delete)
        btns["copy"].clicked.connect(self._on_copy)
        btns["cut"].clicked.connect(self._on_cut)
        btns["paste"].clicked.connect(self._on_paste)
        btns["undo"].clicked.connect(self._on_undo)
        btns["redo"].clicked.connect(self._on_redo)
        btns["export"].clicked.connect(self._on_export)
        btns["clear"].clicked.connect(self._on_clear)

        # TTS / NLP operations
        btns["read"].clicked.connect(self._on_read)
        btns["translate"].clicked.connect(self._on_translate)
        btns["transcribe"].clicked.connect(self._on_transcribe)
        btns["check_grammar"].clicked.connect(self._on_check_grammar)
        
        # Record actions
        btns["record_pause"].clicked.connect(self.on_record_pause)
        btns["stop_record"].clicked.connect(self.on_stop_record)

        # Theme
        btns["theme"].clicked.connect(self._on_toggle_theme)

        # File operations
        btns["open_book"].clicked.connect(self._on_open_book)
        btns["upload"].clicked.connect(self._on_upload_text)

        # Audio / Media operations
        btns["play"].clicked.connect(self._on_play)
        btns["rename"].clicked.connect(self._on_rename)
        btns["reload_audio"].clicked.connect(self._on_reload_media)

        # Reader mode toggle
        btns["toggle_reader_mode"].clicked.connect(self._on_toggle_reader_mode)

        # ── Book viewer debug signal ────────────────────────────
        # (loadFinished is already connected inside MainWindowView to
        # re-apply dark mode — no need to connect it again here.)

    # ── Edit handlers ───────────────────────────────────────────

    def _on_copy(self) -> None:
        self._view.editor.copy()

    def _on_cut(self) -> None:
        self._view.editor.cut()

    def _on_paste(self) -> None:
        self._view.editor.paste()

    def _on_undo(self) -> None:
        self._view.editor.undo()

    def _on_redo(self) -> None:
        self._view.editor.redo()

    def _on_export(self) -> None:
        """Save the editor content to a text file chosen by the user."""
        text = self._view.get_editor_text()
        file_path, _ = QFileDialog.getSaveFileName(
            self._view, "Save Text File", ".txt", "*.txt (*.txt)"
        )
        if not file_path:
            return
        try:
            self._doc_model.save_text_file(file_path, text)
            QMessageBox.information(self._view, "Success", "The file was saved successfully.")
        except Exception as e:
            QMessageBox.critical(self._view, "Error", f"Could not save the file:\n{e}")

    def _on_clear(self) -> None:
        self._view.clear_editor()

    # ── TTS / NLP handlers ──────────────────────────────────────

    def _on_read(self) -> None:
        text = self._view.get_editor_text()
        self.llm_model.read_aloud(text)

    def _on_translate(self) -> None:
        text = self._view.get_editor_text()
        result = self.llm_model.translate(text)
        print("Translated:", result)

    def _on_transcribe(self) -> None:
        self.llm_model.transcribe("")
        print("Transcribed")

    def _on_check_grammar(self) -> None:
        text = self._view.get_editor_text()
        issues = self.llm_model.check_grammar(text)
        print("Checked grammar — issues:", len(issues))
        
    def on_record_pause(self, checked):
        if checked:
            self.record.record_audio()
        else:
            self.record.pause()
        
    def on_stop_record(self):
        self.record.stop()

    # ── Theme handler ───────────────────────────────────────────

    def _on_toggle_theme(self) -> None:
        """Switch between the modern dark and modern light templates."""
        theme_path, invert = self._theme_model.toggle()
        apply_stylesheet(self._app, theme=theme_path, invert_secondary=invert)
        wp = self._theme_model.wallpaper_path
        print(f"[Theme] current={self._theme_model.current_theme} | "
              f"is_dark={self._theme_model.is_dark} | "
              f"wallpaper={wp} | exists={wp.is_file()}")
        self._view.set_wallpaper(wp)

    # ── Book load debug ─────────────────────────────────────────

    def _on_book_load_finished(self, ok: bool) -> None:
        """Slot connected to QWebEngineView.loadFinished — logs whether
        the page/PDF loaded successfully.

        Note: The dark-mode re-application on loadFinished is handled
        inside MainWindowView._on_book_load_finished()."""
        if ok:
            print("[BookViewer] Load finished successfully.")
        else:
            print("[BookViewer] Load FAILED — the content could not be rendered.")

    # ── Reader mode handler ────────────────────────────────────

    def _on_toggle_reader_mode(self) -> None:
        """Toggle the book viewer between light and dark mode."""
        self._view.toggle_reader_dark_mode()

    # ── File handlers ───────────────────────────────────────────

    def _on_open_book(self) -> None:
        """Open a file dialog to select a PDF or EPUB and display it
        in the book viewer."""
        file_path, _ = QFileDialog.getOpenFileName(
            self._view,
            "Open book",
            "",
            self._book_model.filter_string(),
        )
        if not file_path:
            return

        print(f"[OpenBook] Selected: {file_path}")

        try:
            result = self._book_model.build_url_or_html(file_path)
        except (ValueError, FileNotFoundError) as e:
            QMessageBox.critical(self._view, "Error", f"Could not open the book:\n{e}")
            return

        # Load into the web engine view based on type
        if result["type"] == "pdf" and result["url"]:
            print(f"[OpenBook] Loading PDF URL: {result['url']}")
            self._view.load_book_url(result["url"])
        elif result["type"] == "epub" and result["html"]:
            print(f"[OpenBook] Loading EPUB HTML ({len(result['html'])} chars)")
            self._view.load_book_html(result["html"])

        # Switch MDI to the Reader panel so the user can see the book
        self._view.activate_reader_panel()

        # Update the window title with the book info
        title = result.get("title", "")
        author = result.get("author", "")
        if title:
            caption = f"{title}"
            if author:
                caption += f" — {author}"
            self._view.setWindowTitle(f"ReadItLoud — {caption}")

    def _on_upload_text(self) -> None:
        """Browse for a text file and load its contents into the editor."""
        dialog_result = QFileDialog.getOpenFileName(
            self._view, "Open file", "", "*txt (*.txt)"
        )
        if not dialog_result or not dialog_result[0]:
            return
        try:
            file_name = self._doc_model.extract_file_name(dialog_result)
            contents = self._doc_model.read_text_file(file_name)
            self._view.set_editor_text(contents)
        except FileNotFoundError as e:
            QMessageBox.critical(self._view, "Error", f"Could not open the file:\n{e}")

    # ── Media handlers ──────────────────────────────────────────

    def _on_play(self) -> None:
        """Play the selected audio file from either list widget.

        If the selected file is already playing, stops playback instead
        (toggle behaviour).
        """
        source, filename = self._view.get_selected_audio_item()
        if source is None or filename is None:
            QMessageBox.information(
                self._view, "Play",
                "Please select an audio file from the list first."
            )
            return

        # Toggle: if the same file is playing, stop it
        if self._view.is_audio_playing():
            self._view.stop_audio()
            print(f"[Play] Stopped playback")
            return

        url = self._media_model.get_playback_url(source, filename)
        if url is None:
            QMessageBox.warning(
                self._view, "File not found",
                f"Could not find the audio file:\n{filename}"
            )
            return

        print(f"[Play] Playing: {filename} (source={source})")
        self._view.play_audio(url, source)

    def _on_rename(self) -> None:
        """Rename the selected audio file after user confirmation."""
        source, filename = self._view.get_selected_audio_item()
        if source is None or filename is None:
            QMessageBox.information(
                self._view, "Rename",
                "Please select an audio file from the list first."
            )
            return

        # Ask the user for a new name
        new_name = self._view.ask_new_filename(filename)
        if new_name is None or new_name == filename:
            return  # User cancelled or typed the same name

        try:
            actual_new_name = self._media_model.rename_file(source, filename, new_name)
        except FileNotFoundError:
            QMessageBox.warning(
                self._view, "File not found",
                f"Could not find the audio file:\n{filename}"
            )
            return
        except OSError as e:
            QMessageBox.critical(
                self._view, "Rename error",
                f"Could not rename the file:\n{e}"
            )
            return

        print(f"[Rename] {filename} → {actual_new_name}")
        self._refresh_audio_lists()

        # Re-select the renamed item so the user sees it highlighted
        self._view.select_audio_item_by_name(source, actual_new_name)

    def _on_delete(self) -> None:
        """Delete the selected audio file after user confirmation."""
        source, filename = self._view.get_selected_audio_item()
        if source is None or filename is None:
            QMessageBox.information(
                self._view, "Delete",
                "Please select an audio file from the list first."
            )
            return

        # Stop playback if the file being deleted is currently playing
        self._view.stop_audio()

        # Confirmation dialog
        msg = QMessageBox(self._view)
        msg.setMinimumSize(500, 180)
        msg.setWindowTitle("Delete audio file")
        msg.setText(f"Are you sure you want to permanently delete this file?\n\n{filename}")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        msg.setDefaultButton(QMessageBox.StandardButton.Cancel)
        resp = msg.exec()

        if resp != QMessageBox.StandardButton.Yes:
            return

        try:
            self._media_model.delete_file(source, filename)
        except FileNotFoundError:
            QMessageBox.warning(
                self._view, "File not found",
                f"Could not find the audio file:\n{filename}"
            )
            return
        except OSError as e:
            QMessageBox.critical(
                self._view, "Delete error",
                f"Could not delete the file:\n{e}"
            )
            return

        print(f"[Delete] Removed: {filename} (source={source})")
        self._refresh_audio_lists()

    def _on_reload_media(self) -> None:
        """Refresh both generated and recorded audio lists."""
        self._refresh_audio_lists()

    # ── Private helpers ─────────────────────────────────────────

    def _refresh_audio_lists(self) -> None:
        """Reload both audio lists from disk and update the view."""
        recorded = self._media_model.list_recorded_media()
        self._view.populate_recorded_list(recorded)
        
    