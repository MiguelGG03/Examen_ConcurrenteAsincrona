class Cuenta:
    
    def __init__(self, dni:str, saldo:float):
        self.dni = dni
        self.saldo = saldo

    def getDni(self):
        return self.dni
    
    def getSaldo(self):
        return self.saldo
    
    def agregar_dinero(self, monto:float):
        if monto > 0:
            self.saldo += monto
            

    def retirar_dinero(self, monto:float):
        if monto < 0:
            if self.saldo >= monto:
                self.saldo += monto
                return True
        return False