from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget


from const.CONSTANTS import *
from const.page import Ui_Form
from process import Process


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        # self.common = QProperty

        self.pushButton_15.setText('ЗАПУСТИТЬ\nВСЕ')
        self.pushButton_15.clicked.connect(self.start_all)

        self.buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                        self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10,
                        self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14]

        for i, button in enumerate(self.buttons):
            text = SCRIPT_NAMES[i].upper()
            button.setText(text)
            button.setProperty('common', True)
            button.setStyleSheet(COMMON_STYLE)

        self.pushButton.clicked.connect(lambda: self.start_current(self.pushButton))
        self.pushButton_2.clicked.connect(lambda: self.start_current(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.start_current(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.start_current(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.start_current(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.start_current(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.start_current(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.start_current(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.start_current(self.pushButton_9))
        self.pushButton_10.clicked.connect(lambda: self.start_current(self.pushButton_10))
        self.pushButton_11.clicked.connect(lambda: self.start_current(self.pushButton_11))
        self.pushButton_12.clicked.connect(lambda: self.start_current(self.pushButton_12))
        self.pushButton_13.clicked.connect(lambda: self.start_current(self.pushButton_13))
        self.pushButton_14.clicked.connect(lambda: self.start_current(self.pushButton_14))

    def start_all(self):
        for button in self.buttons:
            self.start_current(button)

    def start_current(self, button):
        text = button.text()
        timer = QTimer()
        # if button.isChecked():
        #     button.setStyleSheet(LOADING_STYLE)
        #     print(text)

    def return_style(self, button):
        button.setChecked(False)
        button.setStyleSheet(COMMON_STYLE)
        print(button.text(), button.isChecked())
