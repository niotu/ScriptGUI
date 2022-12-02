from PyQt5.QtWidgets import QWidget

from const.logWindow import Ui_Form


class LogShower(QWidget, Ui_Form):
    def __init__(self):
        super(LogShower, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Logs")

