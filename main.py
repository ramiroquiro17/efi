from stock import *

class App:
    def __init__(self):
        self.stock = Stock()
    def Run(self):
       var = True
       while var:
        opcion = int(input('''
        Menú Principal
    1.  Ver stock completo
    2.  Ver lista de peliculas alquiladas
    3.  Añadir película al stock
    4.  Eliminar película del stock
    5.  Ver ficha de película
    6.  Alquilar una película
    0.  Salir del programa
    Seleccione la opción deseada: '''))
        if opcion == 1:
            self.listastock = self.stock.getStock() 
            print('Películas en stock:')
            for e in self.listastock:
                print(f'Id: {e.getId()} - {e.getTitulo()}')
        elif opcion == 2:
            print('Películas alquiladas:')
            for e in self.listastock:
                if e.getEstado() == 'Alquilada':
                  print(f'Id: {e.getId()} - {e.getTitulo()}')
        elif opcion == 3:
            self.stock.addPelicula()
        
        elif opcion == 4:
            self.stock.deletePelicula()

        elif opcion == 5:
            nro = int(input('Id de película a buscar: '))
            for e in self.listastock:
                if nro == e.getId():
                    print(f'''
                FICHA DE LA PELICULA    
                Id: {e.getId()}
                Título: {e.getTitulo()}
                Género: {e.getGenero()}
                Año: {e.getYear()}
                Director: {e.getDirector()}
                Protagonista: {e.getProtagonista()}
                Precio: {e.getPrecio()}
                Estado: {e.getEstado()}''')

        elif opcion == 6:
            print('Películas DISPONIBLES en stock:')
            for e in self.listastock:
                if e.getEstado() == 'NO alquilada':
                    print(f'Id: {e.getId()} - {e.getTitulo()}')

            idPelicula = int(input('Ingrese el id de la película que desea alquilar: '))
            for peli in self.listastock:
                if idPelicula == peli.getId():
                    peli.alquilar()

        elif opcion == 0:
            print('Gracias por utilizar este programa')
            var = False
        else:
            print('Ingrese una opción correcta')
        
if __name__ == '__main__':
    new = App()
    new.Run()
