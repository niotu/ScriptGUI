import os

from PyQt5.QtCore import QProcess, pyqtSignal, QObject
from PyQt5.QtGui import QIcon

from const.CONSTANTS import *


class Script(QObject):
    # finish = pyqtSignal()

    def __init__(self, name):
        super(Script, self).__init__()
        self.is_completed = False

        self.name = name
        self.dir = ''
        # self.script_path = PREFIX + NAMES_TO_SCRIPTS[self.name] + '.py'
        self.script_path = 'python ' + os.path.join(os.path.dirname(__file__), 'scripts/rash.py')

    def run(self):
        self.process = QProcess(self)

        self.process.readyRead.connect(self.readout)
        self.process.start(self.script_path)
        # self.process.finished.connect(self.done)
        print('-------run ' + self.script_path + '--------------------------------')
        print(self.process.state())

    def readout(self):
        print(self.process.readAll())

    def done(self):
        self.is_completed = True
        print('DONE DONE DONE')
        # self.finish.emit()

    def error(self, err):
        print('ERROR ERROR', err)

    def output(self, aaa):
        print('output', aaa)
