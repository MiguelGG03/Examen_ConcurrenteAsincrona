from Banco import Banco
from Cliente import Cuenta
from Movimiento import Movimiento
import concurrent.futures


def main_ej1():

    results = []

    bank = Banco()
    cliente = Cuenta("123",100) # DNI 123 Saldo 100€
    bank.agregar_cliente(cliente)

    NUM_PROCES_1 = 40
    NUM_PROCES_2 = 20
    NUM_PROCES_3 = 60

    with concurrent.futures.ProcessPoolExecutor() as pool:
        #Agregación de todo el dinero
        futures = [pool.submit(bank.agregar_dinero, ("123",100)) for _ in range(NUM_PROCES_1)]    

        #Espera de que lleguen todos los procesos
        for future in concurrent.futures.as_completed(futures):
            cuenta, cantidad = future.result()
            print("Se ha agregado {}€ a la cuenta {}".format(cantidad, cuenta))
            bank.agregar_dinero(cuenta, cantidad)

    bank.ImprimeTodosLosMovimientos()



if __name__=="__main__":
    main_ej1()