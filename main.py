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
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Author: Samantha Alvarez Hechevarría
Contact: samanthadesktop324@gmail.com
GitHub: https://github.com/SamanthaVSC/ReadItLoud
"""

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
