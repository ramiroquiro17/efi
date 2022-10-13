from stock import *

class App:
    def __init__(self):
        self.stock = Stock()
        self.listastock = self.stock.getStock() 
    def Run(self):
       var = True
       while var:
        opcion = int(input('''
        Menú Principal
    1.  Ver stock completo
    2.  Añadir película
    3.  Ver ficha de película
    4.  Alquilar una película
    5.  Salir del programa
    Seleccione la opción deseada: '''))
        if opcion == 1:
            print('Películas en stock:')
            for e in self.listastock:
                print(f'Id: {e.getId()} - {e.getTitulo()}')
        elif opcion == 2:
            self.stock.addPelicula()
        elif opcion == 3:
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

        elif opcion == 4:
            print('Películas DISPONIBLES en stock:')
            for e in self.listastock:
                if e.getEstado() == 'NO alquilada':
                    print(f'Id: {e.getId()} - {e.getTitulo()}')

            idPelicula = int(input('Ingrese el id de la película que desea alquilar: '))
            for peli in self.listastock:
                if idPelicula == peli.getId():
                    peli.alquilar()

        elif opcion == 5:
            print('Gracias por utilizar este programa')
            var = False
        else:
            print('Ingrese una opción correcta')
        
if __name__ == '__main__':
    new = App()
    new.Run()
