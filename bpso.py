from particle import Particle
import copy

class Bpso():
    def __init__(self, initial_matriz:list, poblation:list, num_dimensions:list, cells:int, constrain:int, iteraciones:int, enjambre:int, verbose:bool) -> None:
        """
        Parametros:
        initial_matriz : list, matriz de maquina parte
        poblation : list, lista de matrices maquina celda
        num_dimensions : int, cantidad de dimensiones de la particula
        cells : int, cantidad de celdas
        constrain : int, cantidad maxima de maquinas por celda

        Inicializa el enjambre con los valores iniciales
        """
        self.__poblation = poblation
        self.__num_dimensions = num_dimensions
        self.__initial_matriz = initial_matriz
        self.__cells = cells
        self.__constrain = constrain
        self.__enjambre = enjambre
        self.__criterio_termino = iteraciones
        self.__verbose = verbose

        self.__swarm = []
        for i in range(self.__enjambre):
            particula = Particle(self.__num_dimensions, self.__poblation[i], self.__initial_matriz, self.__cells, self.__constrain, i, self.__verbose)
            self.__swarm.append(particula)

    def optimizer(self) -> list:
        """
        Inicializar el global best como infinito
        Por criterio de termino
        Por cada particula en el enjambre
        inicializar el local best como infinito
        utilizar la funcion particle.evaluate
        evaluar si la particula tiene el mejor fitness
        En caso de serlo actualizar los valores para en nuevo local best
        Si aun quedan particulas por evaluar, seguir con la siguiente
        En caso contrario, evaluar el fitness con la mejor posicion obtenida
        si es local best es mejor que el actual local best, actualizar los valores
        Actualizar la velocidad y posicion de las particulas
        Si aun quedan iteraciones volver a repetir el proceso
        En caso contario se termina la ejecucion.

        retorna el global best
        """

        iteracion = 0
        global_best = 1234567890123456789012345678901234567890
        pos_best = []
        pos_best_aux = []

        if(self.__verbose):
            print("===================================")
            print("Criterio de termino por iteraciones")
            print(f"iteraciones para el termino: {self.__criterio_termino}\n")
            print(f"Cantidad de poblacion y particulas dentro del optimizer: {len(self.__swarm)}\n")
            print("===================================\n")
            
            print("===================================")
            print("Empieza las iteraciones hasta completar el criterio de termino")
            print("===================================")

        while iteracion < self.__criterio_termino:

            local_best = 1234567890123456789012345678901234567890
            local_pos = []
            local_pos_aux = []

            if(self.__verbose):
                print("Se calculara el fiteness de cada particula: \n\n")

            for particula in self.__swarm:
                particula.evaluate()

                particle_local = particula.get_fitness()

                if(self.__verbose):
                    print(f"Fitness obtenido : {particle_local}\n")
                    print(f"Mejor local actual : {local_best}\n")
                    print(f"El fitness de la encontrado: {particle_local} es menor al local best: {local_best} ?\n")
                    if particle_local < local_best:
                        print(f"El nuevo local best es {particle_local}\n")
                    else:
                        print("No se cambia el valor del local best")
                        print("===================================\n\n")


                if particle_local < local_best:
                    local_best = particle_local
                    local_pos = copy.deepcopy(particula.get_position())
                    local_pos_aux = copy.deepcopy(particula.get_position_aux())
            
            if self.__verbose:
                print(f"El mejor local : {local_best} es menor al mejor global {global_best} ?\n")
                if local_best < global_best:
                    print("Se actualiza el valor del global best")
                else:
                    print("Se sigue con el mismo global best")

            if local_best < global_best:
                global_best = local_best
                pos_best = copy.deepcopy(local_pos)
                pos_best_aux = copy.deepcopy(local_pos_aux)
                
            
            if self.__verbose:
                print("Se modifica los valores de la velocidad y posicion de cada particula")
                print("===================================")

            for particula in self.__swarm:
                best = copy.deepcopy(pos_best)
                particula.update_velocity(best)
                particula.update_position()
            
            iteracion += 1

        return [pos_best, pos_best_aux, global_best]
