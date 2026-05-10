"""ReadItLoud — A desktop app for reading, listening, and pronunciation practice."""

import sys

from PySide6.QtWidgets import QApplication

from views.mainwindow import MainWindow


def main():
    """Entry point for the ReadItLoud application."""
    app = QApplication(sys.argv)
    app.setApplicationName("ReadItLoud")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
