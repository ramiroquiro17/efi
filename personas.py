class Persona:
    def __init__(self,nombre,direccion,telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    def getNombreCliente(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getTelefono(self):
        return self.telefono

class Cliente(Persona):
    def __init__(self, idCliente, nombre, direccion, telefono):
        super().__init__(nombre, direccion, telefono)
        self.idCliente = idCliente
        self.pelisAlquiladas = []
    
    def getIdCliente(self):
        return self.idCliente

    def getPelisAlquiladas(self):
        return self.pelisAlquiladas

class RegistroClientes:
    def __init__(self):
        self.clientela = []
        
    def addCliente(self):
        idcliente = len(self.clientela)+1
        nombre = input('ingrese el nombre: ')
        direccion = input('ingrese la direccion: ')
        telefono = int(input('ingrese el nro de telefono: '))
        nuevoCliente = Cliente(idcliente,nombre,direccion,telefono)
        
        self.clientela.append(nuevoCliente)

    def getRegistroClientes(self):
        return self.clientela

class Empleado(Persona):
    def __init__(self, idEmpleado, nombre, direccion, telefono, salario):
        super().__init__(nombre, direccion, telefono)
        self.idEmpleado = idEmpleado
        self.salario = salario

    def getIdEmpleado(self):
        return self.idEmpleado