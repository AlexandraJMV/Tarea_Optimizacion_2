# Grupo 10

* Ademir Muñoz
* Alexandra Mendoza
* Jorge Palacios

# Ejecución

```(bash)

git clone https://github.com/AlexandraJMV/Tarea_Optimizacion_2.git
cd Tarea_Optimizacion_2

# Linux
python3 main.py

# windows
python main.py

```

Al momento de ejecutar saldra un menu con 5 opciones:

1. Ejecutar la primera matriz
2. Ejecutar la segunda matriz
3. Ejecutar la tercera matriz
4. Utilizar otro txt con instancias
5. Salir del menu y terminar la ejecución

Por otro lado hay un archivo llamado settings.py

```(python)
VERBOSE=False
ITERACIONES=10
ENJAMBRE=5
```

Esos son sus valores por defecto, pero pueden ser cambiadas en cualquier momento.

* **VERBOSE**: Si es verdadero muestra en detalle lo que pasa dentro de la ejecucion del bspo y particle.

* **ITERACIONES**: Es el criterio de termino

* **ENJAMBRE**: Es la cantidad de poblacion y particulas a utilizar dentro del bspo