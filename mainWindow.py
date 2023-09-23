from PyQt5.QtCore import QProcess
from PyQt5.QtGui import QColor, QPixmap, QTextCursor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QLabel, QMenu

from const.CONSTANTS import *
from const.page import Ui_Form
from logShower import LogShower


class Task:
    pass


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.common_icon = QPixmap('icons/common.png')
        self.done_icon = QPixmap('icons/done.png')
        self.loading_icon = QPixmap('icons/loading.png')
        self.error_icon = QPixmap('icons/broken.png')

        self.log_window = None

        self.setupUi(self)

        self.label_2.setText('')
        self.label_2.resize(32, 20)
        self.label_2.setStyleSheet(
            'QLabel{background: transparent} QLabel:hover{background: #E11111}')
        self.label_2.setPixmap(QPixmap('icons/exit.png'))
        self.label_2.click.connect(self.exit)

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
            shadow.setColor(QColor(256 // 4, 256 // 4, 256 // 4))
            shadow.setXOffset(0)
            shadow.setBlurRadius(15)

            button.setGraphicsEffect(shadow)

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

        self.tasks = []

    def start_all(self):
        for button in self.buttons:
            self.start_current(button)

    def start_current(self, button):
        self.set_state(button, 'loading')
        self.start_script(button.text())

    def set_state(self, button, state):
        label = button.children()[1]
        button.setToolTip(state + '...')
        if state == 'loading':
            label.setPixmap(self.loading_icon)
        elif state == 'done':
            label.setPixmap(self.done_icon)
        elif state == 'error':
            # self.show_helper(button)

            label.setPixmap(self.error_icon)

    def start_script(self, name):
        if name == 'ЭЙС':
            self.run_ace()

        prname = NAMES_TO_SCRIPTS[name.lower().replace('\n', '')]
        logname = SPECIAL[name.lower().replace('\n', '')]
        path = prname

        task = Task()
        self.tasks.append(task)

        process = QProcess(self)
        task.process = process


        if prname[0] == '/':
            process.setWorkingDirectory('/' + '/'.join(prname.split('/')[:-1]))
        process.setObjectName(name)
        process.errorOccurred.connect(lambda: self.done(process, True))
        process.finished.connect(lambda: self.done(process))
        process.readyRead.connect(lambda: self.readout(process))
        process.readyReadStandardError.connect(lambda: self.readerror(process))
        process.start(path)
        # print(path)?
        # logger.write(logname, path)

    def run_ace(self):
        name = 'ace'
        path = ''
        task = Task()
        self.tasks.append(task)
        
        process = QProcess(self)
        task.process = process

        process.setObjectName(name)
        process.errorOccurred.connect(lambda: self.done(process, True))
        process.finished.connect(lambda: self.done(process))
        process.readyRead.connect(lambda: self.readout(process))
        process.readyReadStandardError.connect(lambda: self.readerror(process))
        process.start(path)

    def readout(self, process):
        name = process.objectName()
        logname = SPECIAL[name.lower().replace('\n', '')]
        info = process.readAll()
        if not info:
            return
        print(name, info)
        logger.write(logname, info)

    def readerror(self, process):
        name = process.objectName()
        logname = SPECIAL[name.lower().replace('\n', '')]

        err = process.readAllStandardError()
        logger.write(logname, err)

    def done(self, process, is_error=False):
        state = process.exitCode()
        print(state)
        name = process.objectName()
        logname = SPECIAL[name.lower().replace('\n', '')]
        name = name.upper()
        logger.write(logname, process.readAll())
        # logger.write(logname, str(str(state) + '--' + name.replace('\n', ' ')))
        widget = self.find_widget_by_name(name)
        if state == 0 and not is_error:
            # logger.write(logname, str('DONE DONE DONE ' + name.replace('\n', ' ')))
            self.set_state(widget, 'done')
        else:
            self.error('UNKNOWN ERROR!! state is: ' + str(state))
            self.menu = QMenu()
            self.menu.addAction('Show logs', lambda: self.show_logs(logname))
            self.menu.addAction('Restart', lambda: self.start_current(widget))
            self.menu.setAutoFillBackground(True)
            self.menu.setStyleSheet(MENU_STYLE)
            widget.setMenu(self.menu)
            self.set_state(widget, 'error')

    def show_logs(self, name):
        self.log_window = LogShower()

        lines = logger.read(name)

        self.log_window.plainTextEdit.setPlainText(' '.join(lines))
        self.log_window.plainTextEdit.moveCursor(QTextCursor.End)
        self.log_window.show()

    def error(self, e):
        logger.write('errors_QT', str('error:' + e))

    def find_widget_by_name(self, name):
        for button in self.buttons:
            if button.text() == name:
                return button

    def startAnimation(self):
        pass

    def exit(self):
        self.close()
