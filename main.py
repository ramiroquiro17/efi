from personas import *
from stock import *

class App:
    def __init__(self):
        self.stock = Stock()
        self.listastock = self.stock.getStock()
        self.clientes = RegistroClientes()
        self.listaclientes = self.clientes.getRegistroClientes()    
    def Run(self):
       var = True
       while var:
        opcion = int(input('''
        Menú Principal
    1.  Ver stock completo
    2.  Añadir película
    3.  Ver ficha de película
    4.  Ver listado de clientes
    5.  Añadir cliente
    6.  Ver ficha de un cliente
    7.  Alquilar una película
    8.  Salir del programa
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
            print('la clientela esta formada por:')
            for e in self.listaclientes:
                print(f'N°) {e.getNumero()}, {e.getNombreCliente()}')

        elif opcion == 5:
           self.clientes.addCliente()

        elif opcion == 6:
            nro = int(input('nro de cliente: '))
            for e in self.listaclientes:
                if e.getNumero() == nro:
                    print(f'''
                FICHA DEL CLIENTE
                Número: {e.getNumero()}
                Nombre: {e.getNombreCliente()}
                Dirección: {e.getDireccion()}
                Teléfono: {e.getTelefono()}
                Películas alquiladas: {e.getPelisAlquiladas()}''')

        elif opcion == 7:
            print('Películas DISPONIBLES en stock:')
            for e in self.listastock:
                if e.getEstado() == 'NO alquilada':
                    print(f'Id: {e.getId()} - {e.getTitulo()}')

            idPelicula = int(input('Ingrese el id de la película que desea alquilar: '))
            for peli in self.listastock:
                if idPelicula == peli.getId():
                    peli.alquilar()
                    print('Clientela disponible para alquilar:')
                    for c in self.listaclientes:
                        print(f'N°{c.getNumero()}) {c.getNombreCliente()}')
                    idCliente = int(input('Ingrese el nro del cliente que va a alquilar: '))
                    for cliente in self.listaclientes:
                        if idCliente == cliente.getNumero():
                            cliente.pelisAlquiladas.append(peli.getTitulo())
                            print(f'{cliente.getNombreCliente()} alquiló la película {peli.getTitulo()}')

        elif opcion == 8:
            print('Gracias por utilizar este programa')
            var = False
        else:
            print('Ingrese una opción correcta')
        
if __name__ == '__main__':
    new = App()
    new.Run()
