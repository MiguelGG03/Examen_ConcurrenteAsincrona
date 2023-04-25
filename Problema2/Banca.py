import random
import Cliente

class Banca:

    def __init__(self):
        self.__num= random.randrange(0,36)
        self.__din= 50000

    def getNum(self):
        return self.__num
    
    def checkConcreto(self,cliente:Cliente):
        if(cliente.getNum()==self.__num):
            return True
        else:
            return False
        
    def checkParidad(self,cliente:Cliente, tipo:"PAR" or "IMPAR"):
        if tipo=="PAR":
            if(cliente.getNum()%2==0):
                return True
            else:
                return False
        else:
            if(cliente.getNum()%2!=0):
                return True
            else:
                return False
            
    def pagarApuesta(self, cliente:Cliente, tipo, apuesta):
        if(tipo=="CONCRETO"):
            if(self.checkConcreto(cliente)):
                cliente.pagoApuesta(apuesta*36)
                self.__din-= (apuesta*36)
            
        elif(tipo=="PAR" or tipo=="IMPAR"):
            if(self.checkParidad(cliente, tipo)):
                cliente.pagoApuesta(apuesta*2)
                self.__din-= (apuesta*2)



        
