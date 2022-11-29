from PyQt5.QtCore import QProcess, pyqtSignal, QObject
from PyQt5.QtGui import QIcon

from const.CONSTANTS import *


class Script(QObject):
    finish = pyqtSignal()

    def __init__(self, name):
        super(Script, self).__init__()
        self.is_completed = False

        self.name = name
        self.dir = ''
        # self.script_path = PREFIX + NAMES_TO_SCRIPTS[self.name] + '.py'
        self.script_path = 'C:\\Users\\noitu\\work\\PycharmProjects\\ScriptGUI\\test.py'

    def run(self):
        self.process = QProcess()
        # self.process.setWorkingDirectory(PREFIX)
        self.process.finished.connect(self.done)
        self.process.errorOccurred.connect(self.error)
        # self.process.readyReadStandardOutput.connect(self.output)
        # self.process.execute('python.exe', [self.script_path])
        self.process.start('python.exe', [self.script_path])
        print('-------run ' + self.script_path + '--------------------------------')
        print(self.process.state())

    def done(self):
        self.is_completed = True
        print('DONE DONE DONE')
        # self.finish.emit()

    def error(self, err):
        print('ERROR ERROR', err)

    def output(self, aaa):
        print('output', aaa)
