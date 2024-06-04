import random
import math
from collections import Counter

class Particle:
    def __init__(self, num_dimensions:int, ciudadano:list, matrix:list, cells:int, constrain:int, index:int) -> None:
        """
        Parametros:
        num_dimensions : int, cantidad de dimensiones de la particula
        ciudadano : list, posicion inicial de la particula
        matrix : list, matriz de maquina parte
        cells : int, cantidad de celdas
        constrain : int, cantidad maxima de maquinas por celda

        Inicializa la particula con los valores iniciales
        """

        # variables estaticas
        self.__index = index
        self.__num_dimensions = num_dimensions
        self.__cells = cells
        self.__constrain = constrain
        self.__initial_matrix = matrix.copy()

        # Posiciones de la particula
        self.__position_aux = []
        self.__position = ciudadano.copy()

        # Velocidad de la particula
        self.__velocity = []

        # Mejor posiciones y fitness de la particula
        self.__best_position = []
        self.__best_position_aux = []
        self.__best_fitness = 1234567890123456789012345678901234567890

        # Fitness de la particula
        self.__fitness = 1234567890123456789012345678901234567890

        # Inicializacion de las velocidades
        for i in range(self.__num_dimensions):
            fila = [random.random() for i in range(self.__cells)]
            self.__velocity.append(fila)


    def evaluate(self) -> None:
        """
        Aqui se debera evaluar la particula, es decir, calcular su fitness
        """
        if self.need_fix_row(): self.fix_row()
        if self.need_fix_column(): self.fix_column()

        self.set_aux()

        self.__fitness = self.cost()

        if self.__fitness < self.__best_fitness:
            self.__best_fitness = self.__fitness
            self.__best_position = self.__position.copy()
            self.__best_position_aux = self.__position_aux.copy()

    
    def update_velocity(self, pos_best_global:list) -> None:
        """
        Aqui se debera actualizar la velocidad de la particula
        """
        weight = 0.5
        c1 = 1
        c2 = 2

        for i in range(self.__num_dimensions):
            for j in range(self.__cells):
                r1=random.random()
                r2=random.random()

                vel_cognitive = c1*r1*(self.__best_position[i][j] - self.__position[i][j])
                vel_social = c2*r2*(pos_best_global[i][j] - self.__position[i][j])
                self.__velocity[i][j] = weight*self.__velocity[i][j] + vel_cognitive + vel_social


    def update_position(self) -> None:
        """
        Aqui se debera actualizar la posicion de la particula
        """
        for i in range(self.__num_dimensions):
            lista = [self.__velocity[i][j] for j in range(self.__cells)]
            sigmund = self.sigmund(lista)

            flag = True
            for j in range(self.__cells):
                if sigmund[j] == max(sigmund) and flag:
                    self.__position[i][j] = 1
                    flag = False
                else:
                    self.__position[i][j] = 0
                

    def need_fix_row(self) -> bool:
        """
        Aqui se verificara si la posicion necesita ser corregida,
        especificamente en la fila.
        """
        for row in self.__position:
            if not (sum(row) == 1):
                return False
            
        return True
    

    def need_fix_column(self) -> bool:
        """
        Aqui se verificara si la posicion necesita ser corregida, 
        especificamente en la columna.
        """
        for i in range(self.__cells):
            column = [self.__position[j][i] for j in range(len(self.__position))]
            if sum(column) > self.__constrain:
                return False
            
        return True    

    
    def fix_row(self) -> None:
        """
        Aqui se debera corregir la posicion a uno que cumpla con las restricciones de la fila.
        """
        position = []
        for row in self.__position:
            if sum(row) > 1:
                for i in range(len(row)):
                    row[i] = 0
                new_position = random.randint(0, self.__cells - 1)
                row[new_position] = 1
                position.append(row)

            else:
                position.append(row)

        self.__position = position.copy()        
                

    def fix_column(self) -> None:
        """
        Aqui se debera corregir la posicion a uno que cumpla con las restricciones de la columna.
        """
        for i in range(self.__cells):
            column = [self.__position[j][i] for j in range(len(self.__position))]
            if sum(column) > self.__constrain:
                suma = 0
                for j in range(len(self.__position)):
                    if self.__position[j][i] == 1:  suma += 1

                    if suma > self.__constrain:
                        self.__position[j][i] = 0
                        if j + 1 == len(self.__position):
                            self.__position[j][0] = 1
                        else:
                            self.__position[j][i+1] = 1


    def set_aux(self) -> None:
        """
        Aqui se debera retornar la posicion auxiliar que sera la matriz parte x celda.
        La manera de calcularlo sera la misma usada en la entrega anterior:

        Se vera que tipo de maquinas hara cada parte y se colocara en la celda que mas se repita
        dentro de la matriz posicion.
        """
        aux = []
        for i in range(len(self.__initial_matrix[0])):
            column = [self.__initial_matrix[j][i] for j in range(len(self.__initial_matrix))]
            position = []
            for j in range(len(column)):
                if column[j] == 1: position.append(j)

            fila = [0 for i in range(self.__cells)]
            repetidos = []
            for valor in position:
                for j in range(self.__cells):
                    if self.__position[valor][j] == 1:
                        repetidos.append(j)

            repetido = Counter(repetidos).most_common(1)[0][0]
            fila[repetido] = 1
            aux.append(fila)             
    
        self.__position_aux = aux.copy()


    @staticmethod
    def sigmund(velocity:list) -> list:
        lista = []
        for i in range(len(velocity)):
            lista.append(1/(1 + math.exp(-velocity[i])))

        return lista    


    def cost(self) -> int:
        """
        Aqui se debera calcular el costo de la particula.
        """
        total_sum = 0

        # Primero las celdas
        for k in range(self.__cells):
            # Segundo las maquinas
            for i in range(len(self.__position)):
                # Tercero las partes
                for j in range(len(self.__position_aux)):
                    total_sum += self.__position[i][k] * self.__position_aux[j][k] * ( 1 - self.__initial_matrix[i][j] )

        return total_sum
    

    # Getters
    get_velocity = lambda self: self.__velocity
    get_position = lambda self: self.__position
    get_position_aux = lambda self: self.__position_aux
    get_best_position = lambda self: self.__best_position
    get_best_position_aux = lambda self: self.__best_position_aux
    get_best_fitness = lambda self: self.__best_fitness
    get_fitness = lambda self: self.__fitness
    get_index = lambda self: self.__index