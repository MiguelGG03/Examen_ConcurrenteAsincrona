import random

class Cliente:

    def __init__(self):
        self.__din= 1000
        self.__num= random.randrange(0,36)

    def getNum(self):
        return self.__num
    
    def getDin(self):
        return self.__din
    
    def pagoApuesta(self, dinero):
        self.__din+= dinero

    def martingala(self):
        apuesta= 10
        