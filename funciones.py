print("Las funciones son bloques de código reutilizables que nos permiten encapsular tareas específicas y ejecutarlas cuando sea necesario.")
print("Las funciones nos ayudan a organizar nuestro código, evitar la repetición y hacer que nuestros programas sean más modulares y fáciles de mantener.\n")

print("Definición y llamada de funciones")
print("Para definir una función en Python, utilizamos la palabra clave 'def' seguida del nombre de la función y paréntesis.")
print("El bloque de código de la función se indenta después de los dos puntos.\n")

def saludo():
    print("¡Hola, mundo!")

print("Llamamos a la función saludo():")
saludo()

print("\nParámetros y argumentos")
print("Las funciones pueden aceptar parámetros, que son valores que se pasan a la función cuando se la llama.")
print("Los parámetros se especifican dentro de los paréntesis en la definición de la función.\n")

def saludo_con_nombre(nombre):
    print(f"¡Hola, {nombre}!")

print("Llamamos a la función saludo_con_nombre('Juan'):")
saludo_con_nombre("Juan")

print("Llamamos a la función saludo_con_nombre('María'):")
saludo_con_nombre("María")

print("\nValores de retorno")
print("Las funciones pueden devolver valores utilizando la palabra clave 'return'.")
print("El valor de retorno puede ser utilizado por el código que llama a la función.\n")

def suma(a, b):
    return a + b

resultado = suma(3, 4)
print("Resultado de suma(3, 4):", resultado)

print("\nFunciones anónimas (lambda)")
print("Python permite crear funciones anónimas o funciones lambda, que son funciones sin nombre definidas en una sola línea.")
print("Se utilizan comúnmente para funciones pequeñas y concisas.\n")

cuadrado = lambda x: x ** 2
print("Resultado de cuadrado(5) usando lambda:", cuadrado(5))

print("\nAlcance de las variables (local vs. global)")
print("Las variables definidas dentro de una función tienen un alcance local, lo que significa que solo son accesibles dentro de la función.")
print("Las variables definidas fuera de cualquier función tienen un alcance global y pueden ser accedidas desde cualquier parte del programa.\n")

def funcion():
    variable_local = 10
    print("Dentro de funcion(): variable_local =", variable_local)

variable_global = 20

def funcion2():
    print("Dentro de funcion2(): variable_global =", variable_global)

print("Llamamos a funcion():")
funcion()

print("Llamamos a funcion2():")
funcion2()

print("Fuera de las funciones: variable_global =", variable_global)

print("Intentamos acceder a variable_local fuera de la función...")
try:
    print(variable_local)  # Esto debería dar error
except NameError as e:
    print("Error:", e)

