from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QLabel, QVBoxLayout, 
    QWidget, QPushButton, QLineEdit, QScrollArea)
from PySide6.QtCore import Qt
from stock import *
from PySide6.QtGui import QIntValidator
from qt_material import apply_stylesheet
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
        self.scroll = QScrollArea()
        self.widget = QWidget() 
        self.layout = layout = QVBoxLayout()
        self.mensaje = QLabel('Películas en stock:')
        layout.addWidget(self.mensaje) 
 
        for e in listaStock:
              self.peli = QLabel(f'Id: {e.getId()} - {e.getTitulo()}')
              layout.addWidget(self.peli) 
        self.widget.setLayout(self.layout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        
        self.show()
class ventanaFichaP(QMainWindow):
    def __init__(self, listaStock):
        super().__init__()
        self.listaStock=listaStock
        self.layout = layout = QVBoxLayout()
        
        self.texto = QLabel('Id de película a buscar: ')
        layout.addWidget(self.texto)

        self.id = InputInt()
        layout.addWidget(self.id)
        

        self.boton = QPushButton('Conseguir Ficha') 
        self.boton.setDefault(True) 
        layout.addWidget(self.boton) 
        self.boton.clicked.connect(self.getFicha)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    def getFicha(self):
        for e in self.listaStock:
            if int(self.id.text()) == e.getId():
                self.ficha = QLabel(f'''
                        FICHA DE LA PELICULA    
                        Id: {e.getId()}
                        Título: {e.getTitulo()}
                        Género: {e.getGenero()}
                        Año: {e.getYear()}
                        Director: {e.getDirector()}
                        Protagonista: {e.getProtagonista()}
                        Precio: {e.getPrecio()}
                        Estado: {e.getEstado()}''')
                self.layout.addWidget(self.ficha)
        self.boton.close()
        self.id.close()
        self.texto.close()
        self.boton2 = QPushButton('Buscar otra ficha') 
        self.boton2.setDefault(True) 
        self.layout.addWidget(self.boton2) 
        self.boton2.clicked.connect(self.restablecer)
    def restablecer(self):
        self.ficha.close()
        self.boton2.close()
        self.texto = QLabel('Id de película a buscar: ')
        self.layout.addWidget(self.texto)

        self.id = InputInt()
        self.layout.addWidget(self.id)
        

        self.boton = QPushButton('Conseguir Ficha') 
        self.boton.setDefault(True) 
        self.layout.addWidget(self.boton) 
        self.boton.clicked.connect(self.getFicha)


        

class InputInt(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setValidator(QIntValidator()) 

if __name__ == '__main__':
    app = QApplication()
    apply_stylesheet(app, theme='dark_cyan.xml')
    window = MainWindow()
    window.show()
    app.exec()
