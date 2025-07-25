# manejo_excepciones.py

print("=== MANEJO DE EXCEPCIONES EN PYTHON ===\n")

print("1. BLOQUE try-except CON EXCEPCIÓN INCORPORADA\n")

def funcion():
    print("Dentro de funcion()")
    condicion = True  # Puedes cambiar esto a False para evitar la excepción
    if condicion:
        print("Condición verdadera. Lanzando excepción.")
        raise Exception("Descripción del error: ocurrió un problema específico.")
    print("Fin de funcion() (esto no se verá si se lanza la excepción)")

try:
    print("Intentando ejecutar funcion()...")
    funcion()
except Exception as e:
    print(f"Se capturó una excepción: {str(e)}")

print("\n2. BLOQUE finally PARA LIMPIEZA\n")

try:
    print("Ejecutando operación arriesgada con finally...")
    resultado = 10 / 0  # Esto lanza ZeroDivisionError
except ZeroDivisionError:
    print("¡Error! División por cero detectada.")
finally:
    print("Este bloque finally se ejecuta siempre, haya o no excepción.")

print("\n3. EXCEPCIONES PERSONALIZADAS\n")

# Definimos una clase de excepción personalizada
class MiErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def verificar_dato(valor):
    print(f"Verificando el valor: {valor}")
    if valor < 0:
        raise MiErrorPersonalizado("No se permiten valores negativos.")
    print("Valor aceptado.")

try:
    print("Intentando verificar un dato negativo...")
    verificar_dato(-5)
except MiErrorPersonalizado as e:
    print(f"Excepción personalizada capturada: {str(e)}")

print("\nPrograma finalizado correctamente.")

