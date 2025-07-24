print("ESTRUCTURAS CONDICIONALES EN PYTHON")
print("""
Las estructuras de control nos permiten controlar el flujo de ejecución de nuestros programas.
En Python, las estructuras condicionales más comunes son: if, if-else, if-elif-else.

Estas estructuras nos permiten ejecutar bloques de código dependiendo de condiciones.
""")

print("1. IF")
print("""
La estructura if se utiliza para ejecutar un bloque de código si una condición es verdadera.

Ejemplo:
""")

edad = 18
if edad >= 18:
    print("Eres mayor de edad.")

print("\n2. IF-ELSE")
print("""
La estructura if-else nos permite ejecutar un bloque alternativo si la condición es falsa.

Ejemplo:
""")

edad_1 = 15
if edad_1 >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print("\n3. IF-ELIF-ELSE")
print("""
Esta estructura permite evaluar múltiples condiciones en orden.

Ejemplo:
""")

calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bueno")
elif calificacion >= 70:
    print("Bueno")
else:
    print("Necesita mejorar")

