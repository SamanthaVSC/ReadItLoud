from qt_material import apply_stylesheet
from PySide6.QtWidgets import QMainWindow
from mainwindow import MainWindow

class Theme(MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def initial_theme(self):
        with open('config/themes/default.txt', 'r') as th:
            default = th.read() # tema inicial
        apply_stylesheet(self.app, theme=default)

   
    def change_theme(self, checked):
    # clicked(checked) entrega True/False
        if checked:
            t = 'dark_teal.xml'
            with open('config/themes/default.txt', 'w') as th:
                new_theme = th.write('dark_teal.xml')
            return apply_stylesheet(self.app, theme=t)
                
        else:
            t = 'light_blue.xml'
            with open('config/themes/default.txt', 'w') as th:
                new_theme = th.write('light_blue.xml')
        return apply_stylesheet(self.app, theme=t)