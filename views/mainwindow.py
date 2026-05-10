"""Main window for ReadItLoud application."""

from PySide6.QtWidgets import QMainWindow

from views.ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    """Primary application window.

    This class is the main entry point for the UI layer. It sets up the
    Qt Designer-generated UI and connects signals to presenter callbacks.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

