"""Main window for ReadItLoud application."""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication
from ui_mainwindow import Ui_mainWindow
from qt_material import apply_stylesheet

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        
        
        # Theme SETUP
        self.themes = ['dark_teal.xml', 'light_blue.xml']
        self.change_theme(self.themes)
        ""
        self.theme_pB.setCheckable(True)
        self.theme_pB.clicked.connect(self.change_theme)  

    def change_theme(self, status):
        if status == 1:
            apply_stylesheet(self,theme='dark_teal.xml')
        else:
            apply_stylesheet(self,theme='light_blue.xml')

        
