from io import open

# * Escritura
# texto = "Hola Mundo!"

# archivo = open("archivos/hola.txt", "w")
# archivo.write(texto)
# archivo.close()

# * Lectura
# archivo = open("archivos/hola.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# * Lectura como Lista
# archivo = open("archivos/hola.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# * With y Seek
# with open("archivos/hola.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# * Agregar
# archivo = open("archivos/hola.txt", "a+")
# archivo.write("\nChao Mundo")
# archivo.close()

# * Lectura y Escritura
with open("archivos/hola.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Tal vez"
    archivo.writelines(texto)
