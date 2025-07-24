print("=====================================")
print("Conjuntos en Python (set)")
print("=====================================")

print("Un conjunto es una estructura de datos mutable y no ordenada.")
print("Almacena elementos únicos (sin duplicados).")
print("Se define con llaves {} o usando la función set().\n")

# Creación de conjuntos
print("Creación de conjuntos:")
frutas = {"manzana", "banana", "naranja"}
print('frutas = {"manzana", "banana", "naranja"} ->', frutas)

numeros = set([1, 2, 3, 4, 5])
print("numeros = set([1, 2, 3, 4, 5]) ->", numeros)

print("\n=====================================")
print("Operaciones de conjuntos")
print("=====================================")

# Conjuntos para operaciones
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

print("conjunto1 =", conjunto1)
print("conjunto2 =", conjunto2)

# Unión
print("\nUnión (|): conjunto1 | conjunto2")
union = conjunto1 | conjunto2
print("Resultado:", union)  # {1, 2, 3, 4, 5}

# Intersección
print("\nIntersección (&): conjunto1 & conjunto2")
interseccion = conjunto1 & conjunto2
print("Resultado:", interseccion)  # {3}

# Diferencia
print("\nDiferencia (-): conjunto1 - conjunto2")
diferencia = conjunto1 - conjunto2
print("Resultado:", diferencia)  # {1, 2}

# Diferencia simétrica
print("\nDiferencia simétrica (^): conjunto1 ^ conjunto2")
diferencia_simetrica = conjunto1 ^ conjunto2
print("Resultado:", diferencia_simetrica)  # {1, 2, 4, 5}

print("\nResumen:")
print("- Los conjuntos no tienen elementos repetidos.")
print("- Son útiles para operaciones matemáticas de conjuntos.")
print("- Se pueden modificar agregando o quitando elementos con métodos como add(), remove() o discard().")

