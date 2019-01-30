# Importamos las clases
from ordenamientoInsercion import *
from ordenamientoSeleccion import *

# Creamos una lista de datos cualquiera
datos = [7, 23, 55, 78, 12, 98, 56, 32, 76, 90, 5, 12, 43, 4, 34]


# Instanciamos los objetos de cada tipo de Ordenamiento
insercion = OrdenamientoInsercion(datos)
seleccion = OrdenamientoSeleccion(datos)

# Llamamos a los metodos ordenar de cada clase para ver como se ejecutna cada pequeno
print("\nMetodo de insercion: \n")
insercion.ordenar()
print("\nMetodo de seleccion: \n")
seleccion.ordenar()
