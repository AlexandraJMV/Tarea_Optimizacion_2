from instancia import leer_archivo
from poblacion import poblacion
from bpso import Bpso
import time

if __name__ == "__main__":
    start = time.time()
    matrices, cells, max_cells = leer_archivo()
    matrizA, matrizB, matrizC = matrices
    cellsA, cellsB, cellsC = cells
    max_cellsA, max_cellsB, max_cellsC = max_cells
    poblacion = poblacion(100, cellsA, len(matrizA), max_cellsA)
    
    bpso = Bpso(matrizA, poblacion, len(matrizA), cellsA, max_cellsA)
    a,b,c = bpso.optimizer()

    """print(a)
    print("\n\n",b)
    print("\n\n",c)"""

    print("Matriz Maquina Celda:\n")
    for row in a:
        print(row)

    print("\nMatriz Pieza Celda:\n")
    for row in b:
        print(row)
    
    print(f"\nTotal de movimientos: {c}\n")

    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.6f} seconds")
