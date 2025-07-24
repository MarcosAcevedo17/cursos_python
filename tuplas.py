print("=====================================")
print("Tuplas en Python")
print("=====================================")

print("Una tupla es una estructura de datos inmutable y ordenada.")
print("Se define con paréntesis (), y sus elementos están separados por comas.\n")

# Creación de una tupla
punto = (3, 4)

print("Creación de la tupla:")
print("punto =", punto)
print("\nAcceso a los elementos por índice:")
print("Coordenada X:", punto[0])  # Imprime 3
print("Coordenada Y:", punto[1])  # Imprime 4

print("\nIMPORTANTE:")
print("Las tuplas son inmutables. No se pueden agregar, eliminar ni modificar sus elementos.")

print("\nLas tuplas son útiles cuando necesitas almacenar datos que no deben modificarse, como coordenadas o configuraciones.")

print("\n-------------------------------------")
print("Métodos útiles para trabajar con tuplas")
print("-------------------------------------")

mi_tupla = (1, 2, 3, 2, 4, 2)
print("mi_tupla =", mi_tupla)

print("\nMétodo count():")
print("Cuenta cuántas veces aparece el número 2")
cantidad_de_dos = mi_tupla.count(2)
print("Resultado:", cantidad_de_dos)  # Imprime: 3

print("\nMétodo index():")
print("Devuelve el índice de la primera aparición del número 2")
indice_2 = mi_tupla.index(2)
print("Resultado:", indice_2)  # Imprime: 1

print("\nMétodo index() con parámetro de inicio:")
print("Busca el número 2 desde el índice 2")
indice_2_desde_2 = mi_tupla.index(2, 2)
print("Resultado:", indice_2_desde_2)  # Imprime: 3

print("\nMétodo index() con rango de búsqueda:")
print("Busca el número 2 entre los índices 2 y 4")
indice_2_rango = mi_tupla.index(2, 2, 4)
print("Resultado:", indice_2_rango)  # Imprime: 3

print("\nFunción len():")
print("Devuelve la cantidad de elementos en la tupla")
longitud = len(mi_tupla)
print("Resultado:", longitud)  # Imprime: 6

print("\nResumen:")
print("- Las tuplas se usan cuando los datos no deben modificarse.")
print("- Ejemplos típicos: coordenadas (x, y), configuraciones fijas, datos constantes.")

