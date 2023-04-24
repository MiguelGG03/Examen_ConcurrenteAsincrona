from Problema1.main_ej1 import main_ej1

def main():
    resp="S"
    while resp=="S":
        resp2 = input("Elija el ejercicio a ejecutar (1,2): ")
        if resp2=="1":
            print("\nEjecutando ejercicio 1...\n\n")
            main_ej1()
        elif resp2=="2":
            print("No esta hecho el ejercicio")
        resp=input("\nDesea continuar? (S/N): ")

if __name__ == "__main__":
    main()