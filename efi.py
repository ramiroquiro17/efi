from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QLabel, QVBoxLayout, 
    QWidget, QPushButton, QLineEdit)
from stock import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stock = Stock()
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
       self.listastock = self.stock.getStock() 
       self.w = ventanaStock(self.listastock)
       self.w.show()

    def getPelicula(self): 
           pass
    def getFichaP(self): 
        self.listastock = self.stock.getStock() 
        self.w = ventanaFichaP(self.listastock)
        self.w.show()
    def alquilar(self): 
           pass
    
    

class ventanaStock(QMainWindow):
    def __init__(self, listaStock):
        super().__init__()
        self.layout = layout = QVBoxLayout()
        self.mensaje = QLabel('Películas en stock:')
        layout.addWidget(self.mensaje) 
 
        for e in listaStock:
              self.peli = QLabel(f'Id: {e.getId()} - {e.getTitulo()}')
              layout.addWidget(self.peli) 

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
class ventanaFichaP(QMainWindow):
    def __init__(self, listaStock):
        super().__init__()
        self.listaStock=listaStock
        self.layout = layout = QVBoxLayout()
        
        self.texto = QLabel('Id de película a buscar: ')
        layout.addWidget(self.texto)

        self.id = QLineEdit()
        layout.addWidget(self.id)

        boton = QPushButton('conseguir Ficha') 
        boton.setDefault(True) 
        layout.addWidget(boton) 
        boton.clicked.connect(self.getFicha)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    def getFicha(self):
        for e in self.listaStock:
            if int(self.id.text()) == e.getId():
                ficha = QLabel(f'''
                        FICHA DE LA PELICULA    
                        Id: {e.getId()}
                        Título: {e.getTitulo()}
                        Género: {e.getGenero()}
                        Año: {e.getYear()}
                        Director: {e.getDirector()}
                        Protagonista: {e.getProtagonista()}
                        Precio: {e.getPrecio()}
                        Estado: {e.getEstado()}''')
                self.layout.addWidget(ficha)
         
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
      
