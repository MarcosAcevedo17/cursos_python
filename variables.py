print("VARIABLES EN PYTHON")
print("""
Las variables son contenedores que nos permiten almacenar y manipular datos en nuestros programas.
Puedes pensar en una variable como una etiqueta a la que asignas un valor específico.

En Python, no es necesario declarar el tipo de datos de una variable de antemano,
ya que Python infiere el tipo de datos automáticamente en función del valor asignado.
""")

print("DECLARACIÓN Y ASIGNACIÓN DE VARIABLES")
print("""
Para declarar y asignar un valor a una variable en Python, utilizamos el operador de asignación '='.
El nombre de la variable va a la izquierda del operador, y el valor que deseas asignar va a la derecha.

Ejemplo:
""")

# Ejemplo de variables
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

print(f"nombre = {nombre}")
print(f"edad = {edad}")
print(f"altura = {altura}")
print(f"es_estudiante = {es_estudiante}")

print("""
Python infiere automáticamente el tipo de datos de cada variable en función del valor asignado.
""")

print("ASIGNACIÓN MÚLTIPLE")
print("""
También puedes asignar el mismo valor a múltiples variables en una sola línea:
""")

a = b = c = 10
print(f"a = {a}, b = {b}, c = {c}")

print("NORMAS PARA NOMBRAR VARIABLES")
print("""
Al nombrar variables en Python, es importante seguir algunas reglas:

1. Los nombres solo pueden contener letras (a-z, A-Z), números (0-9) y guiones bajos (_).
   No pueden comenzar con un número.

2. Python distingue entre mayúsculas y minúsculas. Por ejemplo, 'nombre' y 'Nombre' son variables diferentes.

3. No se pueden usar palabras clave reservadas como nombres de variables (por ejemplo, if, else, for, while, etc.).

4. Se recomienda usar nombres descriptivos que indiquen claramente su propósito.

Ejemplos de nombres válidos:
    edad
    nombre_completo
    total_ventas
    _contador

Ejemplos de nombres inválidos:
    1edad          # Comienza con un número
    nombre-completo  # Contiene un guion en lugar de guion bajo
    if             # Palabra clave reservada
""")

