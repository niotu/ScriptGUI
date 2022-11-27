from PyQt5.QtWidgets import QWidget

from const.CONSTANTS import SCRIPT_NAMES
from const.page import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.pushButton_15.setText('ЗАПУСТИТЬ\nВСЕ')

        buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                   self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10,
                   self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14]

        for i, button in enumerate(buttons):
            button.setText(SCRIPT_NAMES[i].upper())
