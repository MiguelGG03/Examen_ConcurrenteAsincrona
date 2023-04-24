from datetime import datetime

"""
aqui guardaremos los movimientos de una manera mas organizada
"""

class Movimiento:
    def __init__(self, dni, monto):
        self.__dni = dni
        self.__monto = monto
        self.__hora = datetime.now()
    
    def getDni(self):
        return self.__dni
    
    def getMonto(self):
        return self.__monto
    
    def getHora(self):
        return self.__hora
    
    def __str__(self):
        return f"{self.__hora} - DNI: {self.__dni} - Monto: {self.__monto}"