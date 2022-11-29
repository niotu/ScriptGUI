from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect

from const.CONSTANTS import *
from const.page import Ui_Form
from process import Script


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.common_icon = QIcon('icons/common.png')
        self.done_icon = QIcon('icons/done.png')
        self.loading_icon = QIcon('icons/loading.png')
        self.error_icon = QIcon('icons/broken.png')

        self.setupUi(self)

        self.pushButton_15.setStyleSheet(ALL_START_STYLE)
        shadow = QGraphicsDropShadowEffect()
        shadow.setParent(self.pushButton_15)
        shadow.setEnabled(True)
        shadow.setColor(QColor(256 // 5, 256 // 5, 256 // 5))
        shadow.setXOffset(0)
        shadow.setBlurRadius(15)
        self.pushButton_15.setGraphicsEffect(shadow)
        self.pushButton_15.setText('ЗАПУСТИТЬ\nВСЕ')
        self.pushButton_15.clicked.connect(self.start_all)

        self.buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                        self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10,
                        self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14]

        for i, button in enumerate(self.buttons):
            text = SCRIPT_NAMES[i].upper()
            button.setText(text)

            shadow = QGraphicsDropShadowEffect()
            shadow.setParent(button)
            shadow.setEnabled(True)
            shadow.setColor(QColor(256 // 5, 256 // 5, 256 // 5))
            shadow.setXOffset(0)
            shadow.setBlurRadius(15)

            button.setGraphicsEffect(shadow)
            button.setIcon(self.common_icon)
            # button.setIconSize(QSize(168, 168))
            button.setProperty('state', 'common')
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
        self.set_state(button, 'loading')
        self.start_script(button.text())

    def set_state(self, button, state):
        # button.setProperty('state', state)
        # button.style().unpolish(button)
        # button.style().polish(button)
        # button.update()
        if state == 'loading':
            button.setIcon(self.loading_icon)
        elif state == 'done':
            button.setIcon(self.done_icon)
        elif state == 'error':
            button.setIcon(self.error_icon)

    def start_script(self, name):
        name = name.lower()
        script = Script(name)
        script.finish.connect(self.script_finished)
        try:
            script.run()
        except Exception as e:
            print(name, e)

    def script_finished(self):
        print('finished')
