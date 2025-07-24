print("CONTROL DE BUCLES EN PYTHON")
print("""
Python proporciona instrucciones especiales para controlar el flujo dentro de los bucles:
break, continue y pass.
""")

print("1. BREAK")
print("""
La instrucción break se usa para salir inmediatamente de un bucle, sin importar la condición.

Ejemplo:
""")

contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

print("\n2. CONTINUE")
print("""
La instrucción continue salta el resto del bloque dentro del bucle y pasa a la siguiente iteración.

Ejemplo: imprimir solo números impares del 0 al 9
""")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("\n3. PASS")
print("""
La instrucción pass es un marcador de posición que no hace nada.
Se usa cuando se necesita una sentencia pero no se quiere ejecutar código aún.

Ejemplo:
""")

for i in range(5):
    pass  # Aquí podrías agregar código después

print("El bucle for anterior itera pero no realiza ninguna acción.")

