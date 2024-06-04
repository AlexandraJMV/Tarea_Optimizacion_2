def leer_archivo():

    # Inicializamos las variables
    matrices = []
    cells = []
    max_cells = []
    matriz = []

    # Abrimos el archivo en modo lectura
    with open('instancias.txt', 'r') as f:

        # Leemos el archivo línea por línea
        for line in f.readlines():

            # Si la línea es un salto de línea, ignoramos
            try:

                # Convertimos los valores de la línea a enteros
                value = [int(valor) for valor in line.strip().split(",")]

                # Si el valor es distinto de 0 y 1, agregamos a la lista de celdas, celdas maximas y matrices
                if value[0] != 0 and value[0] != 1:
                    cells.append(value[0])
                    max_cells.append(value[1])
                    matrices.append(matriz)
                    matriz = []

                # Si el valor es 0 o 1, agregamos a la matriz actual
                else:
                    matriz.append(value)
            
            # Si hay un error, ignoramos
            except:
                continue

        # Cerramos el archivo
        f.close()

    return matrices, cells, max_cells