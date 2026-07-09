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
GNU General Public License for more details.x

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Author: Samantha Alvarez Hechevarría
Contact: samanthadesktop324@gmail.com
GitHub: https://github.com/SamanthaVSC/ReadItLoud
"""

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
import json
from pathlib import Path
from os import walk

from PySide6.QtWidgets import QFileDialog, QMessageBox
from qt_material import apply_stylesheet

from app.views.main_window import MainWindowView
from app.models.document_model import DocumentModel
from app.models.theme_model import ThemeModel
from app.models.media_model import MediaModel
from app.models.book_model import BookModel
from app.models.record_model import Record, RecordState

with open("data/tts_engine.json", "r") as file:
    TTS_DATA = json.load(file)

class MainController:
    """Central controller wiring the ReadItLoud UI to its domain models."""

    def __init__(self, view: MainWindowView, app) -> None:
        self._view = view
        self._app = app  # QApplication reference (needed for theme application)

        # ── Instantiate models ──────────────────────────────────
        self._doc_model = DocumentModel()
        self._theme_model = ThemeModel()
        self._media_model = MediaModel()
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
        cmbs = self._view.comoboxes

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
        
        # ── TTS engine combos ───────────────────────────────────
        # Engine change  →  refresh available languages
        cmbs["engine"].currentTextChanged.connect(self.update_languages)
        # Language change → refresh available voices
        cmbs["engine_lang"].currentTextChanged.connect(self.update_voices)

        # Seed the engine combo with every available TTS engine.
        # This first population will trigger `update_languages` automatically
        # (currentTextChanged fires when the first item is added).
        cmbs["engine"].addItems(list(TTS_DATA.keys()))
        

    def update_languages(self, selected_engine: str) -> None:
        """Refresh the language combo box based on the selected engine.

        Triggered when the user picks a different TTS engine. Clears
        both the language and voice combos, then fills the language
        combo with the keys available under that engine in TTS_DATA.
        """
        lang_combo = self._view.comoboxes["engine_lang"]
        voice_combo = self._view.comoboxes["engine_voices"]

        lang_combo.blockSignals(True)
        voice_combo.blockSignals(True)
        lang_combo.clear()
        voice_combo.clear()
        lang_combo.blockSignals(False)
        voice_combo.blockSignals(False)

        if selected_engine in TTS_DATA:
            lang_combo.addItems(list(TTS_DATA[selected_engine].keys()))

        # If no languages are available, the voice combo stays empty.
        # Otherwise, adding the first item to lang_combo will emit
        # currentTextChanged and trigger update_voices automatically.

    def update_voices(self, selected_language: str) -> None:
        """Refresh the voice combo box based on the current engine
        and the selected language.

        Triggered when the user picks a different language (or when
        `update_languages` populates the language combo).
        """
        engine_combo = self._view.comoboxes["engine"]
        voice_combo = self._view.comoboxes["engine_voices"]

        voice_combo.blockSignals(True)
        voice_combo.clear()
        voice_combo.blockSignals(False)

        selected_engine = engine_combo.currentText()
        if (selected_engine in TTS_DATA
                and selected_language in TTS_DATA[selected_engine]):
            voice_combo.addItems(TTS_DATA[selected_engine][selected_language])
        
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

    def _on_read(self, checked) -> None:
        pass
                
    
    def _on_translate(self) -> None:
        pass

    def _on_transcribe(self) -> None:
        pass

    def _on_check_grammar(self) -> None:
        pass

        
    def on_record_pause(self, checked: bool) -> None:
        """Toggle between recording and paused states.

        Because ``record_pause_pB`` is checkable, the click alternates
        the checked flag. We use the controller's own state machine
        (Record.state) as the source of truth and treat ``checked``
        as a hint:

          - checked=True  → start a new recording (from IDLE)
                            or resume (from PAUSED)
          - checked=False → pause the current recording (from RECORDING)
        """
        if checked:
            if self.record.state == RecordState.IDLE:
                # Start a brand-new recording
                try:
                    self.record.record_audio()
                    self._view.start_recording_timer()
                except Exception as e:
                    # e.g. no input device available, PortAudio error, ...
                    QMessageBox.critical(
                        self._view, "Recording error",
                        f"Could not start recording:\n{e}"
                    )
                    # Roll back the button to the IDLE state
                    self._view.reset_recording_ui()
            elif self.record.state == RecordState.PAUSED:
                # Resume from pause
                self.record.resume()
                self._view.start_recording_timer()
        else:
            if self.record.state == RecordState.RECORDING:
                self.record.pause()
                self._view.pause_recording_timer()

    def on_stop_record(self) -> None:
        """Stop the recording and ask the user whether to save it.

        If the user accepts, the audio is written to
        ``cache/records/record_YYYYMMDDHHMMSS.wav`` and the audio list
        is refreshed so the new file shows up immediately. If the user
        declines, the captured audio is discarded. After either branch
        the UI returns to the IDLE state.

        Calling stop() while in IDLE is ignored silently (the user
        clicked STOP without an active recording).
        """
        # Nothing to do if there is no recording in progress
        if self.record.state == RecordState.IDLE:
            return

        # Stop the stream and freeze the timer
        self.record.stop()
        self._view.pause_recording_timer()

        # If nothing was captured, just reset the UI
        if not self.record.has_audio():
            self._view.reset_recording_ui()
            return

        # Ask the user whether to save the recording
        resp = QMessageBox.question(
            self._view, "Save recording",
            "Do you want to save this recording?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes,
        )

        if resp == QMessageBox.StandardButton.Yes:
            filename = Record.generate_filename()
            try:
                saved_path = self.record.save(filename)
                # Refresh the audio list so the new file appears immediately
                self._refresh_audio_lists()
                QMessageBox.information(
                    self._view, "Saved",
                    f"Recording saved as:\n{Path(saved_path).name}"
                )
            except Exception as e:
                QMessageBox.critical(
                    self._view, "Save error",
                    f"Could not save the recording:\n{e}"
                )

        # Always return to the IDLE state and discard any leftover audio
        self.record.discard()
        self._view.reset_recording_ui()

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
        
    
