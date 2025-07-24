print("BUCLES EN PYTHON")
print("""
Los bucles nos permiten repetir un bloque de código varias veces.

En Python, los bucles más comunes son: for y while.
""")

print("1. BUCLE FOR")
print("""
El bucle for se utiliza para iterar sobre una secuencia (lista, tupla, cadena) o cualquier objeto iterable.

Sintaxis básica:
for variable in secuencia:
    instrucciones

Ejemplo:
""")

frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

print("\n2. BUCLE WHILE")
print("""
El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera.

Sintaxis básica:
while condicion:
    instrucciones

Ejemplo:
""")

contador = 0

while contador < 5:
    print(contador)
    contador += 1

print("""
Importante: Cuidado con los bucles infinitos.
Si la condición del while nunca se vuelve falsa, el bucle se ejecutará indefinidamente.
""")

