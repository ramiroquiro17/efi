class Pelicula:
    def __init__(self,id,titulo,genero,year,director,protagonista,precio):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.year = year
        self.director = director
        self.protagonista = protagonista
        self.precio = precio
        self.plazo = 15 #dias
        self.alquilado = False   
    def getId(self):
        return self.id
    def getTitulo(self):
        return self.titulo
    def getGenero(self):
        return self.genero
    def getYear(self):
        return self.year
    def getDirector(self):
        return self.director
    def getProtagonista(self):
        return self.protagonista
    def getPrecio(self):
        return self.precio
    def getEstado(self):
        if self.alquilado:
            return 'Alquilada'
        else:
            return 'NO alquilada'
    def setPlazo(self):
        self.plazo = int(input('Ingrese el plazo: '))        
    def getPlazo(self):
        return self.plazo
    def alquilar(self):
        self.alquilado = True

class Stock:
    def __init__(self):
        self.stock = []
       
    def addPelicula(self):
        id = len(self.stock)+1
        titulo = input('ingrese el titulo: ')
        genero = input('ingrese el genero: ')
        year = int(input('ingrese el año: '))
        director = input('ingrese el director: ')
        protagonista = input('ingrese el protagonista: ')
        precio = int(input('ingrese el precio: '))

        pelicula = Pelicula(id,titulo,genero,year,director,protagonista,precio)
        self.stock.append(pelicula)
    
    def getStock(self):
        return self.stock