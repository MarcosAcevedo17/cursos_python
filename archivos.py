# ------------------------------
# Escritura de archivos en Python
# ------------------------------

# Usando open() y close()
# Esto crea (o sobrescribe) el archivo "datos.txt" y escribe una línea en él
print("Escribiendo archivo con open() y close()...")
archivo = open("datos.txt", "w")  # Abrimos el archivo en modo escritura ("w")
archivo.write("Hola, mundo!\nEsta es una segunda línea.")  # Escribimos texto en el archivo
archivo.close()  # Cerramos el archivo
print("Archivo escrito y cerrado con éxito.\n")

# Usando with (forma más segura y recomendada)
print("Escribiendo archivo con with...")
with open("datos.txt", "w") as archivo:
    archivo.write("Este texto sobrescribe lo anterior.\nNueva línea escrita con with.")
print("Archivo escrito y cerrado automáticamente usando with.\n")


# ------------------------------
# Lectura de archivos en Python
# ------------------------------

# Leer todo el contenido de un archivo usando open() y close()
print("Leyendo archivo con open() y close()...")
archivo = open("datos.txt", "r")  # Abrimos el archivo en modo lectura ("r")
contenido = archivo.read()  # Leemos todo el contenido del archivo
print("Contenido leído con open():")
print(contenido)
archivo.close()  # Cerramos el archivo
print("Archivo cerrado.\n")

# Leer el archivo usando with
print("Leyendo archivo con with...")
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido leído con with:")
    print(contenido)
print("Archivo leído y cerrado automáticamente con with.")

