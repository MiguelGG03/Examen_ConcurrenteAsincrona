import random

class Banca:

    def __init__(self):
        self.__num= random.randrange(0,36)
        self.__din= 50000

    def getNum(self):
        return self.__num
    
    def pagarApuesta(self, cliente, tipo, apuesta):

        if(tipo=="CONCRETO"):

        
