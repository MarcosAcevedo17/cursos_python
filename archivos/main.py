# main.py
# Programa principal que utiliza los módulos personalizados

# Importamos los módulos personalizados
import operaciones
import utilidades

# Usamos funciones del módulo operaciones
resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")

# Solicitamos el nombre al usuario y mostramos un saludo
nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

