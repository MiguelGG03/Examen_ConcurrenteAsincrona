class Cuenta:
    
    def __init__(self, dni, saldo):
        self.dni = dni
        self.saldo = saldo

    def getDni(self):
        return self.dni
    
    def getSaldo(self):
        return self.saldo