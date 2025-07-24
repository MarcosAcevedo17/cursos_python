print("=====================================")
print("Métodos de conjuntos en Python")
print("=====================================")

print("Los conjuntos tienen varios métodos para modificar y acceder a los datos.")
print("- add(elemento): agrega un elemento al conjunto.")
print("- remove(elemento): elimina un elemento (error si no existe).")
print("- discard(elemento): elimina si existe (sin error si no está).")
print("- clear(): elimina todos los elementos del conjunto.\n")

# Creamos el conjunto frutas
frutas = {"manzana", "banana", "naranja"}
print("Conjunto original:", frutas)

# add()
print("\nMétodo add(): agregamos 'pera'")
frutas.add("pera")
print("Resultado:", frutas)  # {"manzana", "banana", "naranja", "pera"}

# remove()
print("\nMétodo remove(): eliminamos 'banana'")
frutas.remove("banana")
print("Resultado:", frutas)  # {"manzana", "naranja", "pera"}

# discard()
print("\nMétodo discard(): intentamos eliminar 'uva' (no está en el conjunto)")
frutas.discard("uva")
print("Resultado:", frutas)  # {"manzana", "naranja", "pera"}

# clear()
print("\nMétodo clear(): eliminamos todos los elementos del conjunto")
frutas.clear()
print("Resultado:", frutas)  # set()

print("\n=====================================")
print("Resumen de estructuras de datos en Python:")
print("=====================================")
print("- Listas: colecciones ordenadas y mutables.")
print("- Tuplas: colecciones ordenadas e inmutables.")
print("- Diccionarios: pares clave-valor.")
print("- Conjuntos: colecciones no ordenadas de elementos únicos.")

