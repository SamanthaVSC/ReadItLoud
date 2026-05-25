import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from qt_material import apply_stylesheet


def main():
    app = QApplication(sys.argv)
    w = MainWindow(app)
    w.initial_theme()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()