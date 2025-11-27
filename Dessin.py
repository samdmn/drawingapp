import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QSlider, QPushButton, QLabel, QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QColor, QPixmap
from CanvasDessin import CanvasDessin

class Dessin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = CanvasDessin()
        self.setCentralWidget(self.canvas)
        self.setWindowTitle("Zone de Dessin")
        self.createToolbar()
    
    def createToolbar(self):
        toolbar = QToolBar("Outils de dessin")
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        
        self.colorAction = toolbar.addAction("Couleur")
        self.colorAction.triggered.connect(self.chooseColor)
        self.updateColorIcon()
        
        toolbar.addSeparator()
        
        widthLabel = QLabel(" Épaisseur: ")
        toolbar.addWidget(widthLabel)
        
        self.widthSlider = QSlider(Qt.Horizontal)
        self.widthSlider.setMinimum(1)
        self.widthSlider.setMaximum(20)
        self.widthSlider.setValue(self.canvas.getWidth())
        self.widthSlider.setTickPosition(QSlider.TicksBelow)
        self.widthSlider.setTickInterval(5)
        self.widthSlider.setMaximumWidth(200)
        self.widthSlider.valueChanged.connect(self.changeWidth)
        toolbar.addWidget(self.widthSlider)
        
        self.widthValueLabel = QLabel(f" {self.widthSlider.value()} ")
        toolbar.addWidget(self.widthValueLabel)
        
        toolbar.addSeparator()
        
        clearButton = QPushButton("Effacer tout")
        clearButton.clicked.connect(self.clearCanvas)
        toolbar.addWidget(clearButton)
    
    def chooseColor(self):
        currentColor = self.canvas.getColor()
        color = QColorDialog.getColor(currentColor, self, "Choisir une couleur")
        if color.isValid():
            self.canvas.setColor(color)
            self.updateColorIcon()
    
    def changeWidth(self, value):
        self.canvas.setWidth(value)
        self.widthValueLabel.setText(f" {value} ")
        print(f"Nouvelle épaisseur: {value}")
    
    def clearCanvas(self):
        self.canvas.clearAll()
        print("Canvas effacé")
    
    def updateColorIcon(self):
        pixmap = QPixmap(20, 20)
        pixmap.fill(self.canvas.getColor())
        icon = QIcon(pixmap)
        self.colorAction.setIcon(icon)

def main(args):
    app = QApplication(args)
    dessin = Dessin()
    dessin.show()
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)