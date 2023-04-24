from Problema1.main_ej1 import main_ej1

def main():
    resp="S"
    while resp=="S":
        resp2 = input("Elija el ejercicio a ejecutar (1,2): ")
        if resp2=="1":
            main_ej1()
        elif resp2=="2":
            print("Ejercicio 2")
        resp=input("Desea continuar? (S/N): ")

if __name__ == "__main__":
    main()