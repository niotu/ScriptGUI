from PyQt5.QtCore import QProcess
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QLabel

from const.CONSTANTS import *
from const.page import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.common_icon = QPixmap('icons/common.png')
        self.done_icon = QPixmap('icons/done.png')
        self.loading_icon = QPixmap('icons/loading.png')
        self.error_icon = QPixmap('icons/broken.png')

        self.setupUi(self)

        self.pushButton_15.setStyleSheet(ALL_START_STYLE)
        shadow = QGraphicsDropShadowEffect()
        shadow.setParent(self.pushButton_15)
        shadow.setEnabled(True)
        shadow.setColor(QColor(256 // 5, 256 // 5, 256 // 5))
        shadow.setXOffset(0)
        shadow.setBlurRadius(20)
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
            # button.setIcon(self.common_icon)
            circle = QPixmap('icons/circle.png')
            # circle.scaled(119, 119)

            label = QLabel(button)
            label.setPixmap(self.common_icon)
            label.setStyleSheet('background: transparent;')
            label.move(24, 24)
            label.setParent(button)
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

        self.script_path = 'python ' + os.path.join(os.path.dirname(__file__))

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
        label = button.children()[-1]
        button.setToolTip(state + '...')
        if state == 'loading':
            label.setPixmap(self.loading_icon)
        elif state == 'done':
            label.setPixmap(self.done_icon)
        elif state == 'error':
            label.setPixmap(self.error_icon)

    def start_script(self, name):
        prname = NAMES_TO_SCRIPTS[name.lower().replace('\n', '')]

        path = f'\scripts\{prname}.py'
        path = self.script_path + path

        logger.info(path)

        self.process = QProcess(self)
        process = self.process
        self.process.setObjectName(name)
        self.process.errorOccurred.connect(self.error)
        self.process.finished.connect(lambda: self.done(process))
        self.process.readyRead.connect(self.readout)
        self.process.start(path)
        logger.info('-------' + path + '--------------------------------')
        logger.info(self.process.state())

    def readout(self):
        logger.info(self.process.readAll())

    def done(self, process):
        state = process.exitCode()
        name = process.objectName()
        name = name.upper()
        print(state, name)
        if state == 0:
            logger.info(('DONE DONE DONE', name))
            self.set_state(self.find_widget_by_name(name), 'done')
        else:
            self.error('UNKNOWN ERROR!! state is: ' + str(state))
            self.set_state(self.find_widget_by_name(name), 'error')

    def error(self, e):
        logger.error(('error:', e))

    def find_widget_by_name(self, name):
        for button in self.buttons:
            if button.text() == name:
                return button

    def format_name(self, name):
        if len(name) > 7:
            return name.replace(' ', '\n')

    def startAnimation(self):
        pass
