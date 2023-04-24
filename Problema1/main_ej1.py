from Banco import Banco
from Cliente import Cuenta
from Movimiento import Movimiento
import multiprocessing


def main_ej1():
    NUM_PROCES_1 = 40
    pool = multiprocessing.Pool(processes=NUM_PROCES_1)
    results = []

    for i in range(NUM_PROCES_1):
        results.append(pool.apply_async("LAFUNCION"))

    for result in results:
        result.wait()

    pool.close()
    pool.join()



if __name__=="__main__":
    main_ej1()