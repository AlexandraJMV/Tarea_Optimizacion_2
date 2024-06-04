# Calculo del fitness del problema
def cost(part_cell:list, machine_cell:list, machine_part:list) -> int:

    # Inicializamos la variable que contendra el valor de la funcion objetivo
    total_sum = 0

    # Primero las celdas
    for k in range(len(part_cell[0])):

        # Segundo las maquinas
        for i in range(len(machine_cell)):

            # Tercero las partes
            for j in range(len(part_cell)):

                # Funcion objetivo
                total_sum += machine_part[i][j] * part_cell[j][k] * ( 1 - machine_cell[i][k] )

    # Retornamos el valor de la funcion objetivo
    return total_sum