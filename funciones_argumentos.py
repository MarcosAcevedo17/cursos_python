print("Documentación de funciones (docstrings)")
print("Es una buena práctica documentar nuestras funciones utilizando docstrings.")
print("Los docstrings son cadenas de texto que describen el propósito, los parámetros y el valor de retorno de una función.")
print("Se colocan inmediatamente después de la definición de la función y se encierran entre triples comillas dobles.\n")

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return base * altura

print("Llamamos a area_rectangulo(5, 3):")
resultado_area = area_rectangulo(5, 3)
print("Resultado:", resultado_area)

print("\nPodemos acceder a la documentación con la propiedad __doc__:")
print(area_rectangulo.__doc__)

print("\nFunciones con número variable de argumentos")
print("Python permite definir funciones que acepten un número variable de argumentos usando * antes del nombre del parámetro.\n")

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print("Llamamos a suma_variable(1, 2, 3):")
print("Resultado:", suma_variable(1, 2, 3))

print("Llamamos a suma_variable(4, 5, 6, 7):")
print("Resultado:", suma_variable(4, 5, 6, 7))

print("\nResumen final:")
print("Las funciones son una herramienta fundamental en la programación.")
print("Nos permiten estructurar y modularizar nuestro código.")
print("Con la capacidad de definir funciones personalizadas, podemos encapsular tareas específicas y reutilizarlas.")
print("Además de las funciones definidas por el usuario, Python también proporciona funciones incorporadas como:")
print("- print()")
print("- len()")
print("- range()")
print("- y muchas más que podemos usar directamente.\n")

