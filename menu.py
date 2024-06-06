from instancia import leer_archivo
from poblacion import poblacion
from bpso import Bpso
import time
import os

def show_menu():
    print("=========================")
    print("       Menu Principal     ")
    print("=========================")
    print("1. Matriz Facil")
    print("2. Matriz Mediana")
    print("3. Matriz Dificil")
    print("4. Leer nuevo archivo")
    print("5. Salir")
    print("=========================")

def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def resolve(matriz:list, cells:int, max_cells:int):
    start = time.time()
    pob = poblacion(100, cells, len(matriz), max_cells)
    bpso = Bpso(matriz, pob, len(matriz), cells, max_cells)

    results = bpso.optimizer()

    print("Matriz Maquina Celda:\n")
    for row in results[0]:
        print(row)
    
    print("\nMatriz Pieza Celda:\n")
    for row in results[1]:
        print(row)
    
    print(f"\nTotal de movimientos: {results[2]}\n")

    end = time.time()

    print(f"Tiempo de ejecución: {end - start:.6f} seconds")
    print("\n\n")
    return


def new_file():
    input_file = input("Ingrese el nombre del archivo: ")

    try:
        matrices, cells, max_cells = leer_archivo(input_file)

        for i in range(len(matrices)):
            print(f"Resolviendo matriz {i+1}...")
            print("\n")
            resolve(matrices[i], cells[i], max_cells[i])
            print("\n")
        
        return

    except:
        print("Error al leer el archivo, intentelo de nuevo.")
        return

def menu():
    matrices, cells, max_cells = leer_archivo()

    while True:
        show_menu()
        option = input("\nIngrese una opcion: ")

        if option == "1":
            clean_screen()
            resolve(matrices[0], cells[0], max_cells[0])
        elif option == "2":
            clean_screen()
            resolve(matrices[1], cells[1], max_cells[1])
        elif option == "3":
            clean_screen()
            resolve(matrices[2], cells[2], max_cells[2])
        elif option == "4":
            clean_screen()
            new_file()
        elif option == "5":
            break
        else:
            print("Opcion no valida, intentelo de nuevo.")

   