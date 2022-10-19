from database import Database
base = Database('stock','id','title','genre','principalActor','director','year','price')

class Pelicula:
    def __init__(self,id,titulo,genero,year,protagonista,director,precio):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.year = year
        self.protagonista = protagonista
        self.director = director
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
        datos = base.select()
        self.stock = []
        for e in datos:
            peli = Pelicula(e[0],e[1],e[2],e[3],e[4],e[5],e[6])
            self.stock.append(peli)
       
    def addPelicula(self):
        ultimaPeli = self.stock[len(self.stock)-1]
        idUltima = int(ultimaPeli.getId())
        id = idUltima+1
        titulo = input('ingrese el titulo: ')
        genero = input('ingrese el genero: ')
        year = int(input('ingrese el año: '))
        director = input('ingrese el director: ')
        protagonista = input('ingrese el protagonista: ')
        precio = float(input('ingrese el precio: '))
        base.insert(id,titulo,genero,year,director,protagonista,precio)

    def deletePelicula(self):
        id = int(input('Ingrese el id de la película a borrar: '))
        base.delete(id)

    def getStock(self):
        Stock.__init__(self)
        return self.stock

