import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QProcess
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSizePolicy

from mainWindow import MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.setWindowTitle('ScripGUI')
    application.setWindowIcon(QIcon('icons/logo.png'))
    application.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    application.show()
    application.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sys.excepthook = except_hook
    print("Started")
    sys.exit(app.exec())


def cleanup():
    from os import walk
    fnames = []
    for (dirpath, dirnames, filenames) in walk('logs'):
        fnames.extend(filenames)
        break

    for f in fnames:
        if f != 'errors_QT_logs.log':
            with open('logs/'+f, 'w') as f:
                f.truncate(0)


if __name__ == "__main__":
    cleanup()
    print("Starting...")
    main()
    print("Closing")
