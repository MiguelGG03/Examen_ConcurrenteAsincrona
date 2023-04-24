from Banco import Banco
from Cliente import Cuenta
from Movimiento import Movimiento
import multiprocessing


def main_ej1():

    results = []

    bank = Banco()
    cliente = Cuenta("123",100) # DNI 123 Saldo 100€
    bank.agregar_cliente(cliente)

    NUM_PROCES_1 = 40
    NUM_PROCES_2 = 20
    NUM_PROCES_3 = 60

    pool = multiprocessing.Pool(processes=NUM_PROCES_1)

    #Agregación de todo el dinero<

    for _ in range(NUM_PROCES_1):
        results.append(pool.apply_async(bank.agregar_dinero, (100,)))

    

    for result in results:
        result.wait()

    pool.close()
    pool.join()

    bank.ImprimeTodosLosMovimientos()



if __name__=="__main__":
    main_ej1()