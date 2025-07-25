# Solicitar al usuario su nombre y su edad utilizando la función input()
# input() muestra un mensaje y espera que el usuario escriba algo por teclado

# Ingreso de nombre
nombre = input("Ingresa tu nombre: ")  # El usuario escribe su nombre

# Ingreso de edad (como string)
# edad_str = input("Ingresa tu edad: ")  # También sería válido así, pero a continuación usamos directamente int()

# Ingreso de edad y conversión a número entero
edad = int(input("Ingresa tu edad: "))  # Convertimos la entrada a número usando int()

# Mostrar un saludo personalizado utilizando print() y concatenación de cadenas
print("Hola, " + nombre + "!")  # Se muestra un saludo con el nombre del usuario
print("Tienes " + str(edad) + " años.")  # Se muestra la edad (convertida nuevamente a string)

# Evaluar si el usuario es mayor o menor de edad utilizando una estructura condicional if
if edad >= 18:
    print("Eres mayor de edad.")  # Si edad es 18 o más, se imprime este mensaje
else:
    print("Eres menor de edad.")  # Si edad es menor a 18, se imprime este mensaje

# Mostrar el mismo mensaje usando f-strings (formato moderno y más claro de cadenas)
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")  # Aquí usamos f-string para insertar variables en la cadena

