# =====================================
# Listas de comprensión en Python
# =====================================

# Las listas de comprensión permiten crear listas nuevas
# de forma concisa a partir de una secuencia existente.

# Sintaxis general:
# nueva_lista = [expresión for elemento in secuencia if condición]

# Ejemplo práctico:
numeros = [1, 2, 3, 4, 5]

# Se crea una nueva lista con los cuadrados de los números pares
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]

# Muestra el resultado
print("Cuadrados de los números pares:", cuadrados)  # Imprime: [4, 16]

# Explicación paso a paso:
# 1. Recorre cada número 'x' en la lista 'numeros'
# 2. Aplica la condición: x % 2 == 0 (números pares)
# 3. Si la condición se cumple, eleva x al cuadrado (x ** 2)
# 4. El resultado se agrega a la nueva lista 'cuadrados'

