from Problema1.Cliente import Cuenta
from Problema1.Movimiento import Movimiento

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
    
    def agregar_dinero(self, dni, cantidad):
        if cantidad > 0 :
            cliente = self.buscar_cliente(dni)
            if cliente is not None:
                cliente.agregar_dinero(cantidad)
                self.agregar_movimiento(Movimiento(dni, cantidad))
                return dni, cantidad
            return False
    

    def retirar_dinero(self, dni, cantidad):
        if cantidad < 0 :
            cliente = self.buscar_cliente(dni)
            if cliente is not None and cliente.getSaldo() >= cantidad:
                    cliente.retirar_dinero(cantidad)
                    self.agregar_movimiento(Movimiento(dni, cantidad))
                    return dni,cantidad
            return False
        
    def ImprimeTodosLosMovimientos(self):
        for i in range(len(self.getMovimientos())):
            print(self.getMovimientos()[i].__str__())
        
if __name__=='__main__':
    bank=Banco()
    c1=Cuenta("123", 1000)
    c2=Cuenta("456", 2000)
    bank.agregar_cliente(c1)
    bank.agregar_cliente(c2)
    bank.agregar_dinero("123", 100)
    bank.agregar_dinero("456", 200)
    bank.retirar_dinero("123", -50)
    bank.retirar_dinero("456", -100)
    bank.ImprimeTodosLosMovimientos()
    

