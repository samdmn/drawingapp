from PyQt5.QtGui import QColor


class Trace:
    def __init__(self, width=2, color=QColor(0, 0, 0)):
        self.points = []
        self.width = width
        self.color = color