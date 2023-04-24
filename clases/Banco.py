class Banco:
    
    def __init__(self):
        self.__clientes = []
        self.__mov = []

    def getClientes(self):
        return self.__clientes
    
    def getMovimientos(self):
        return self.__mov

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)
    
    def agregar_movimiento(self, movimiento):
        self.__mov.append(movimiento)

    def buscar_cliente(self, dni):
        for cliente in self.__clientes:
            if cliente.getDni() == dni:
                return cliente
        return None
    
    def buscar_movimiento(self, dni):
        for movimiento in self.__mov:
            if movimiento.getDni() == dni:
                return movimiento
        return None