from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QLabel, QVBoxLayout, 
    QWidget, QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú Principal")        

        self.layout = layout = QVBoxLayout()
        self.mensaje = QLabel('Menú Principal')
        layout.addWidget(self.mensaje) 

        self.botonStock = QPushButton('Ver stock completo') 
        self.botonStock.setDefault(True) 
        layout.addWidget(self.botonStock) 
        self.botonStock.clicked.connect(self.getStock) 

        self.botonPelicula = QPushButton('Añadir Pelicula') 
        self.botonPelicula.setDefault(True) 
        layout.addWidget(self.botonPelicula) 
        self.botonPelicula.clicked.connect(self.getPelicula)

        self.botonFichaP = QPushButton('Ver ficha de película') 
        self.botonFichaP.setDefault(True) 
        layout.addWidget(self.botonFichaP) 
        self.botonFichaP.clicked.connect(self.getFichaP)


        self.botonAlquilar = QPushButton('Alquilar una película') 
        self.botonAlquilar.setDefault(True) 
        layout.addWidget(self.botonAlquilar) 
        self.botonAlquilar.clicked.connect(self.alquilar)


        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    def getStock(self): 
           pass
    def getPelicula(self): 
           pass
    def getFichaP(self): 
           pass
    def alquilar(self): 
           pass

    
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
      