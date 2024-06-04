import random

def poblacion(max_pob:int, cells:int, machines:int, constrain:int) -> list:
    """
    Parametros:
    max_pob : int,  numero de individuos en la poblacion
    cells : int,    cantidad de celdas
    machines : int, cantidad de maquinas
    constrain: int, cantidad maxima de maquinas por celda

    Retorna: lista de matrices machina celda que son posibles candidatos

    Por ahora la manera en la que se hara sera random
    Para facilitar un poco las cosas se representara primero
    la matriz maquina celda a crear como un array

    [0,0,0,1]
    [0,0,0,1]  =>  [3,3,0,2]
    [1,0,0,0] 
    [0,0,1,0]

    Donde dentro del array la posicion [i] representara la fila de la
    matriz maquina celda mientras que el valor el array[i] sera la columna
    donde habra un 1 dentro de la fila, se asumira que el resto de columnas de la fila
    seran 0's, una vez creada el array de manera aleatoria se transformara en la matriz maquina celda
    normal y se añadira a una lista de matrices que sera la poblacion.
    """
    poblacion = []
    numbers = [i for i in range(cells)]
    numbers_copy = numbers.copy()

    while len(poblacion) < max_pob:
        ciudadano = []
        ciudadano_cantidad = 0
        while ciudadano_cantidad < machines:
            try:
                choice = random.choice(numbers_copy)
                if ciudadano.count(choice) < constrain:
                    ciudadano.append(choice)
                    ciudadano_cantidad += 1
                else:
                    numbers_copy.remove(choice)
            except:
                print("Error en la creacion de la poblacion, no se puede crear mas matrices.")
                break

        ciudadano_translate = translate(ciudadano, cells)
        poblacion.append(ciudadano_translate)
        numbers_copy = numbers.copy()        

    return poblacion


def translate(lista:list, cells:int) -> list:
    """
    Parametros:
    lista : list, lista de matrices maquina celda

    Retorna: lista de matrices maquina celda

    La funcion se encargara de transformar el array de la matriz maquina celda
    a la matriz maquina celda normal, para ello se creara una matriz de ceros
    de tamaño row[maquinas] y se pondra un 1 en la posicion
    row[lista[i]] de la matriz normal, para despues colocar dentro de la matriz
    matrices con append.
    """
    matrices = []
    for i in range(len(lista)):
        row = [0 for i in range(cells)]
        row[lista[i]] = 1
        matrices.append(row)

    return matrices