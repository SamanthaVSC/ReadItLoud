"""Main window for ReadItLoud application."""
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from pathlib import Path
from ui_mainwindow import Ui_mainWindow
from qt_material import apply_stylesheet


import sys
import os
import threading
import queue
import wave
from datetime import datetime
import numpy as np

import sounddevice as sd
import scipy.io.wavfile as wav
import sounddevice as sd
from PySide6.QtCore    import Qt, QThread, Signal, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui     import QColor, QPainter, QBrush, QPen, QFont, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ReadItLoud")
        self.app = app
        
        # Create messages objects
        engine_about = QMessageBox()
        
        # Connect buttons to functions
        self.delete_pB.clicked.connect(self.Show_deleteMSG)
   
        self.copy_pB.clicked.connect(self.COPY)
        self.cut_pB.clicked.connect(self.CUT)
        self.paste_pB.clicked.connect(self.PASTE)
        self.undo_pB.clicked.connect(self.UNDO)
        self.redo_pB.clicked.connect(self.REDO)
        self.export_pB.clicked.connect(self.get_text_save)
        self.clear_pB.clicked.connect(self.CLEAR)
        
        
        self.read_pB.clicked.connect(self.READ)        
        self.translate_pB.clicked.connect(self.TRANSLATE)
        self.transcibe_pB.clicked.connect(self.TRANSCIRBE)
        self.Check_grammar_pB.clicked.connect(self.CHECK_GRAMMAR)
        
        self.theme_pB.clicked.connect(self.change_theme)
        self.open_book_bP.clicked.connect(self.load_pdf)
        self.upload_pB.clicked.connect(self.load_text_files)
        self.reload_audio_pB.clicked.connect(self.load_media_generated)
        self.reload_audio_pB.clicked.connect(self.load_media_record)
 
    # Show a message box to confirm the deletion of a file
    def Show_deleteMSG(self) -> None:
        delete_msg = QMessageBox()
        delete_msg.setMinimumSize(700,200)
        delete_msg.setWindowTitle("Warning")
        delete_msg.setText("Are you sure you want to delete this file?")
        #delete_msg.setIcon(QMessageBox.critical)
        delete_msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        delete_msg.setDefaultButton(QMessageBox.Ok)
        resp = delete_msg.exec()
        # Show message box
        if resp == QMessageBox.Ok:
            print("User chose OK!")
            
        else:
            print("User chose Cancel")
            
    # Show message boxes with license details of the selected model and engine
    def show_modelABOUT(self) -> None:
        delete_msg = QMessageBox()
        delete_msg.setMinimumSize(700,200)
        delete_msg.setWindowTitle("About")
        delete_msg.setText("Here goes license ditails of the selected model")
        #delete_msg.setIcon(QMessageBox.aboutQt)
        delete_msg.setStandardButtons(QMessageBox.Ok)
        delete_msg.setDefaultButton(QMessageBox.Ok)
        ret = delete_msg.exec()
        
    # Show message boxes with license details of the selected model and engine
    def show_engineABOUT(self) -> None:
        delete_msg = QMessageBox()
        delete_msg.setMinimumSize(700,200)
        delete_msg.setWindowTitle("About")
        delete_msg.setText("Here goes license ditails of the selected engine")
        #delete_msg.setIcon(QMessageBox.aboutQt)
        delete_msg.setStandardButtons(QMessageBox.Ok)
        delete_msg.setDefaultButton(QMessageBox.Ok)
        ret = delete_msg.exec()

    # Edit menu functions #
    def COPY(self) -> None:
        self.Reader_editText.copy()

    def CUT(self) -> None:
        self.Reader_editText.cut()
        
    def PASTE(self) -> None:
        self.Reader_editText.paste()
        
    def UNDO(self) -> None:
        self.Reader_editText.undo()
        
    def REDO(self) -> None:
        self.Reader_editText.redo()
        
    def get_text_save(self) -> None:
        """
        Save the content of the text editor to a file chosen by the user.
        """

        # Get the text from the text editor
        text = self.Reader_editText.toPlainText()

        # Open a file dialog to choose where to save the file
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Text File",
            ".txt",
            "*.txt (*.txt)")
    

        # If the user cancels the dialog, file_path will be empty
        if not file_path:
            return

        try:
            # Save the text to the chosen file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)

            QMessageBox.information(
                self,
                "Success",
                "The file was saved successfully."
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Could not save the file:\n{e}"
            )
        
    def CLEAR(self) -> None:
        self.Reader_editText.clear()

        ###############
        # Theme SETUP #
        ###############
        
    # Load the default theme from a txt file and apply it at startup
    def initial_theme(self)  -> None:
        with open('config/themes/default.txt', 'r') as th:
            default = th.read() # tema inicial
        apply_stylesheet(self.app, theme=default)

    def change_theme(self) -> None:
        # Apply the selected theme and save it in a txt file to be loaded at the next start
        with open('config/themes/default.txt', 'r') as th:
            theme = th.read().strip()
    
        if theme == "dark_teal.xml":
            with open('config/themes/default.txt', 'w') as new:
                new.write("light_blue.xml")
            return apply_stylesheet(self.app, theme="light_blue.xml")
        else:
            with open('config/themes/default.txt', 'w') as new:
                new.write("dark_teal.xml")
            return apply_stylesheet(self.app, theme="dark_teal.xml")

        ###############
        # Open a book #
        ###############
        
    # Open a file dialog to select a PDF file and return its path
    def load_pdf(self) -> None:
        paths = QFileDialog.getOpenFileNames(
            self,
            "Open PDF file",
            "",
            "PDF Files (*.pdf)"
         )
        return path

        ###############
        # File UPLOAD #
        ############### 
        
    # Open a file dialog to select a text file and return its name 
    def browse_file(self) -> str:
        fileName = QFileDialog.getOpenFileName(self, 
                                               "Open file","",
                                                "*txt (*.txt)")
        return Path(fileName[0]).name

    # Load the content of the selected text file into the text editor
    def load_text_files(self) -> None:
        with open(self.browse_file(), 'r') as f:
            contents = f.read()
        return self.Reader_editText.setText(contents)
        
   
        #return book_webEngineView.printFinished('book.pdf')
    def load_media_generated(self, folder: str) -> None:
        self.Generated_audioListWidget.clear()
        path = Path('cache/generated')

        # Gather both mp3 and mp4 files
        media_files = sorted(
            [*path.glob("*.mp3"), *path.glob("*.wav")]
        )
        # print(media_files)
        if media_files:
            for file in media_files:
                self.Generated_audioListWidget.addItem(file.name)  # or str(file) for full path
        else:
            self.Generated_audioListWidget.addItem("No .mp3 or .wav files found.")
            
    def load_media_record(self, folder: str) -> None:
        self.yoursListWidget.clear()
        path = Path('cache/records')

        # Gather both mp3 and mp4 files
        media_files = sorted(
            [*path.glob("*.mp3"), *path.glob("*.wav")]
        )

        if media_files:
            for file in media_files:
                self.yoursListWidget.addItem(file.name)  # or str(file) for full path
        else:
            self.yoursListWidget.addItem("No .mp3 or .wav files found.")
            

    
    def CHECK_PRONOUNCE(self):
        pass
    
    def PLAY(self):
        pass #sample_rate, data = wav.read()
    
    def RENAME(self):
        pass
    
    def DELETE(self):
        pass
    
    def READ(self, text):
        pass
    
    def TRANSLATE(self):
        print("Translated")
        
    def TRANSCIRBE(self):
        print("Transcribed")

    def CHECK_GRAMMAR(self):
        print("Checked grammar")
        
