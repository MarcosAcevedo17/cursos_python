print("MÉTODOS DE LISTAS EN PYTHON")
print("""
Las listas tienen varios métodos incorporados para manipular sus elementos.
Aquí algunos comunes:
- append(elemento): agrega un elemento al final.
- insert(indice, elemento): inserta un elemento en una posición.
- remove(elemento): elimina la primera aparición de un elemento.
- pop(indice): elimina y devuelve el elemento en una posición.
- sort(): ordena los elementos ascendentemente.
- reverse(): invierte el orden de los elementos.
""")

frutas = ["manzana", "banana", "naranja"]
print("Lista original:", frutas)

# append
frutas.append("pera")
print("Después de append('pera'):", frutas)

# insert
frutas.insert(1, "uva")
print("Después de insert(1, 'uva'):", frutas)

# remove
frutas.remove("banana")
print("Después de remove('banana'):", frutas)

# pop
fruta_eliminada = frutas.pop(2)
print("Después de pop(2):", frutas)
print("Elemento eliminado:", fruta_eliminada)

# sort
frutas.sort()
print("Después de sort():", frutas)

# reverse
frutas.reverse()
print("Después de reverse():", frutas)

