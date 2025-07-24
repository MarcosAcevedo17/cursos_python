print("OPERADORES EN PYTHON")
print("""
Los operadores son símbolos especiales que nos permiten realizar operaciones en variables y valores.
Python proporciona diferentes tipos de operadores para realizar operaciones aritméticas, comparaciones
y operaciones lógicas.
""")

print("OPERADORES ARITMÉTICOS")
print("""
Los operadores aritméticos se utilizan para realizar operaciones matemáticas básicas:

    Suma (+)             → a + b
    Resta (-)            → a - b
    Multiplicación (*)   → a * b
    División (/)         → a / b
    División entera (//) → a // b
    Módulo (%)           → a % b
    Exponenciación (**)  → a ** b
""")

# Definimos dos variables para usar en los ejemplos
a = 10
b = 3

print(f"Valores: a = {a}, b = {b}\n")

print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División (float): {a} / {b} = {a / b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo (resto): {a} % {b} = {a % b}")
print(f"Exponenciación: {a} ** {b} = {a ** b}")
print("==========================================")
print("OPERADORES DE COMPARACIÓN EN PYTHON")
print("""
Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano (True o False)
según el resultado de la comparación.

Los principales operadores son:
    Igual a (==)
    Diferente de (!=)
    Mayor que (>)
    Menor que (<)
    Mayor o igual que (>=)
    Menor o igual que (<=)
""")


print(f"Valores: a = {a}, b = {b}\n")

igual = a == b
diferente = a != b
mayor_que = a > b
menor_que = a < b
mayor_o_igual = a >= b
menor_o_igual = a <= b

print(f"a == b: {igual}")           # False
print(f"a != b: {diferente}")      # True
print(f"a > b: {mayor_que}")       # True
print(f"a < b: {menor_que}")       # False
print(f"a >= b: {mayor_o_igual}")  # True
print(f"a <= b: {menor_o_igual}")  # False

print("===================================")
print("OPERADORES LÓGICOS EN PYTHON")
print("""
Los operadores lógicos se utilizan para combinar expresiones condicionales y evaluar múltiples condiciones.

Los principales operadores lógicos son:

    AND (and): devuelve True si ambas condiciones son verdaderas.
    OR (or): devuelve True si al menos una de las condiciones es verdadera.
    NOT (not): invierte el valor de una condición.
""")


resultado_and = (a > 5) and (b < 5)
resultado_or = (a > 15) or (b < 5)
resultado_not = not (a > 5)

print(f"Valores: a = {a}, b = {b}\n")

print(f"(a > 5) and (b < 5): {resultado_and}")   # True
print(f"(a > 15) or (b < 5): {resultado_or}")    # True
print(f"not (a > 5): {resultado_not}")            # False
            
