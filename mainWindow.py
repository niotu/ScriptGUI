from PyQt5.QtWidgets import QWidget
from const.page import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

