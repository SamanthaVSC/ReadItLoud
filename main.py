from mainwindow import MainWindow, QApplication
import sys
from pathlib import Path
from qt_material import apply_stylesheet

import os

def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    w = MainWindow(app)
    w.show()
    app.exec()

if __name__ == "__main__":
    main()