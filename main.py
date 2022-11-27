import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from mainWindow import MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.setWindowTitle('ScripGUI')
    application.setWindowIcon(QIcon('stuff/logo.png'))
    application.show()
    sys.excepthook = except_hook
    print("Started")
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Starting...")
    main()