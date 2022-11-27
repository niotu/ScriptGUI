from PyQt5.QtCore import QTimer


class Process():
    def __init__(self):
        self.is_running = False
        self.is_complete = False

    def run(self):
        self.is_running = True
        self.is_complete = False
        timer = QTimer()
        timer.singleShot(3000, lambda: self.stop())

    def stop(self):
        self.is_running = False
        self.is_complete = True
