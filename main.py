"""
ReadItLoud — Entry point.

This module bootstraps the Qt application using the MVC architecture:
  - View:   MainWindowView  (UI only)
  - Model:  DocumentModel, ThemeModel, MediaModel, TTSModel  (data & logic)
  - Controller: MainController  (mediates between View and Models)
"""

import sys

from PySide6.QtWidgets import QApplication

from app.views.main_window import MainWindowView
from app.controllers.main_controller import MainController


def main() -> None:
    app = QApplication(sys.argv)

    # ── Create the View ─────────────────────────────────────────
    view = MainWindowView()

    # ── Create the Controller (which creates Models internally) ─
    controller = MainController(view, app)

    # ── Apply the persisted theme before showing the window ─────
    controller.apply_initial_theme()

    view.show()
    app.exec()


if __name__ == "__main__":
    main()