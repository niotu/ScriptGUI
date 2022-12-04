from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal


class Pic(QtWidgets.QLabel):
    click = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(ev)
        self.click.emit()