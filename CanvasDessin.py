from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QColor
from PyQt5.QtCore import Qt
from Trace import Trace

class CanvasDessin(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 400)
        self.traces = []
        self.currentTrace = None
        self.currentWidth = 3
        self.currentColor = QColor(0, 0, 0)
    
    def setWidth(self, width):
        self.currentWidth = width
    
    def setColor(self, color):
        self.currentColor = color
    
    def getWidth(self):
        return self.currentWidth
    
    def getColor(self):
        return self.currentColor
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.currentTrace = Trace(width=self.currentWidth, color=self.currentColor)
            self.currentTrace.points.append(event.pos())
            self.update()
    
    def mouseMoveEvent(self, event):
        if self.currentTrace is not None:
            self.currentTrace.points.append(event.pos())
            self.update()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.currentTrace is not None:
            self.currentTrace.points.append(event.pos())
            self.traces.append(self.currentTrace)
            self.currentTrace = None
            self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for trace in self.traces:
            self.drawTrace(painter, trace)
        if self.currentTrace is not None and len(self.currentTrace.points) > 0:
            self.drawTrace(painter, self.currentTrace)
    
    def drawTrace(self, painter, trace):
        if len(trace.points) == 0:
            return
        path = QPainterPath()
        path.moveTo(trace.points[0])
        for i in range(1, len(trace.points)):
            path.lineTo(trace.points[i])
        pen = QPen(trace.color)
        pen.setWidth(trace.width)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawPath(path)
    
    def clearAll(self):
        self.traces = []
        self.currentTrace = None
        self.update()
