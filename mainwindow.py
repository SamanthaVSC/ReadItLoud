"""Main window for ReadItLoud application."""
from PySide6.QtWidgets import QMainWindow, QApplication
from ui_mainwindow import Ui_mainWindow
from qt_material import apply_stylesheet

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        # Theme SETUP
        self.themes = ['dark_teal.xml', 'light_blue.xml']
        self.theme_pB.setCheckable(True)
        self.theme_pB.clicked.connect(self.change_theme)
        apply_stylesheet(self.app, theme=self.themes[1])  # tema inicial

    def change_theme(self, checked):
        # clicked(checked) entrega True/False
        theme = self.themes[0] if checked else self.themes[1]
        apply_stylesheet(self.app, theme=theme)