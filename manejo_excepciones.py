print("Manejo de excepciones en Python")
print("El manejo de excepciones nos permite capturar y manejar errores de manera controlada utilizando las declaraciones try, except y opcionalmente finally.\n")

print("Bloque TRY:")
print("El bloque try contiene el código que puede generar una excepción.")
print("Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except correspondiente.\n")

try:
    print("Intentamos hacer 10 / 0...")
    resultado = 10 / 0
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: División por cero")

print("\nBloques EXCEPT múltiples:")
print("Podemos tener múltiples bloques except para manejar distintos tipos de errores.\n")

try:
    print("Intentamos hacer 10 / 0 nuevamente...")
    resultado = 10 / 0
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

print("\nBloque FINALLY:")
print("El bloque finally se ejecuta siempre, ocurra o no una excepción.")
print("Se usa normalmente para liberar recursos, como cerrar archivos o conexiones.\n")

try:
    print("Intentamos abrir un archivo que no existe...")
    archivo = open("archivo.txt", "r")
    print("Archivo abierto con éxito.")
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    print("Este bloque finally se ejecuta siempre.")
    print("Si el archivo se abrió, deberíamos cerrarlo aquí.")
    try:
        archivo.close()
        print("Archivo cerrado correctamente.")
    except NameError:
        print("No se pudo cerrar el archivo porque no fue abierto.")

print("\nResumen:")
print("- try: se usa para intentar ejecutar código que podría fallar.")
print("- except: captura errores específicos y nos permite manejarlos.")
print("- finally: se ejecuta siempre, útil para liberar recursos.")

