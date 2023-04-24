from Banco import Banco
from Cliente import Cuenta
from Movimiento import Movimiento
import concurrent.futures

def multiproceso_agregar(bank, NUM_PROCES,cantid):
    with concurrent.futures.ProcessPoolExecutor() as pool:
        #Agregación de todo el dinero
        futures = [pool.submit(bank.agregar_dinero, "123",cantid) for _ in range(NUM_PROCES)]    

        #Espera de que lleguen todos los procesos
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                cuenta, cantidad = result
                bank.agregar_dinero(cuenta, cantidad)
            except Exception as e:
                print(f"Error al ejecutar el proceso: {e}")


def multiproceso_retirar(bank, NUM_PROCES,cantid):
    with concurrent.futures.ProcessPoolExecutor() as pool:
        #Agregación de todo el dinero
        futures = [pool.submit(bank.retirar_dinero, "123",cantid) for _ in range(NUM_PROCES)]    

        #Espera de que lleguen todos los procesos
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                cuenta, cantidad = result
                bank.retirar_dinero(cuenta, cantidad)
            except Exception as e:
                print(f"Error al ejecutar el proceso: {e}")


def main_ej1():

    bank = Banco()
    cliente = Cuenta("123",100) # DNI 123 Saldo 100€
    bank.agregar_cliente(cliente)

    NUM_PROCES_1 = 40
    NUM_PROCES_2 = 20
    NUM_PROCES_3 = 60

    multiproceso_agregar(bank, NUM_PROCES_1, 100)
    multiproceso_agregar(bank, NUM_PROCES_2, 50)
    multiproceso_agregar(bank, NUM_PROCES_3, 20)

    print("------------------------------------------\n")
    print(f"Despues de agregar el dinero - {cliente.__str__()}\n")

    multiproceso_agregar(bank, NUM_PROCES_1, -100)
    multiproceso_agregar(bank, NUM_PROCES_2, -50)
    multiproceso_agregar(bank, NUM_PROCES_3, -20)

    print("------------------------------------------\n")
    print(f"Despues de retirar el dinero - {cliente.__str__()}\n")    

    print("------------------------------------------\n")

    bank.ImprimeTodosLosMovimientos()



if __name__=="__main__":
    main_ej1()