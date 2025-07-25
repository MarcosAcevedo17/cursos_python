# ------------------------------
# Importar módulos en Python
# ------------------------------

# 1. Importar el módulo completo
import math  # Módulo matemático con muchas funciones

# Usar una función del módulo math con el nombre del módulo
print("Usando math.sqrt() para calcular raíz cuadrada de 25:")
resultado = math.sqrt(25)  # Calcula raíz cuadrada de 25
print(f"Resultado: {resultado}\n")  # Imprime 5.0


# 2. Importar solo una función específica de un módulo
from math import sqrt  # Ahora podemos usar sqrt directamente

print("Usando sqrt() directamente sin escribir math.:")
print(f"Resultado de sqrt(36): {sqrt(36)}\n")  # Imprime 6.0


# ------------------------------
# Uso de otros módulos estándar
# ------------------------------

# 3. Módulo random
import random  # Para generar números aleatorios

print("Generando un número aleatorio entre 1 y 10:")
numero_aleatorio = random.randint(1, 10)  # Número aleatorio entre 1 y 10
print(f"Número aleatorio generado: {numero_aleatorio}\n")


# 4. Módulo datetime
import datetime  # Para trabajar con fechas y horas

print("Obteniendo la fecha y hora actual:")
fecha_actual = datetime.datetime.now()  # Fecha y hora actual
print(f"Fecha y hora actual: {fecha_actual}\n")

# También podemos formatear la fecha si queremos
print("Fecha formateada (solo día/mes/año):")
print(fecha_actual.strftime("%d/%m/%Y"))  # Ejemplo: 25/07/2025

