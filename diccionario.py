print("=====================================")
print("Diccionarios en Python")
print("=====================================")

print("Un diccionario es una estructura de datos mutable y no ordenada.")
print("Permite almacenar pares clave-valor.")
print("Cada elemento tiene una clave única asociada a un valor.")
print("Se definen con llaves {}, y los pares clave:valor se separan por comas.\n")

# Creación del diccionario
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print("Creación de un diccionario:")
print('persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}\n')

# Acceso a valores
print("Accediendo a los valores por clave:")
print("Nombre:", persona["nombre"])  # Imprime "Juan"
print("Edad:", persona["edad"])      # Imprime 25
print("Ciudad:", persona["ciudad"])  # Imprime "Madrid"

# Uso del método get()
print("\nUso del método get():")
print('persona.get("nombre") =', persona.get("nombre"))  # Juan
print('persona.get("altura") =', persona.get("altura"))  # None (clave no existe)
print('persona.get("altura", "No especificado") =', persona.get("altura", "No especificado"))

print("\n-------------------------------------")
print("Métodos útiles para trabajar con diccionarios")
print("-------------------------------------")

# Métodos keys(), values(), items()
print("Claves del diccionario (keys()):")
print(persona.keys())  # dict_keys(['nombre', 'edad', 'ciudad'])

print("\nValores del diccionario (values()):")
print(persona.values())  # dict_values(['Juan', 25, 'Madrid'])

print("\nPares clave-valor del diccionario (items()):")
print(persona.items())  # dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'Madrid')])

# Método update()
print("\nUso del método update() para agregar un nuevo par clave-valor:")
print('persona.update({"profesion": "Ingeniero"})')
persona.update({"profesion": "Ingeniero"})

print("\nDiccionario actualizado:")
print(persona)  # {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

print("\nResumen:")
print("- Los diccionarios almacenan información con claves únicas.")
print("- Son útiles para representar objetos, configuraciones, registros, etc.")
print("- Se pueden modificar, agregar y eliminar elementos.")

