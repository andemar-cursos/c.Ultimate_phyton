from io import open

# Escritura
texto = "Andemar!2"

archivo = open("archivo-prueba.txt", "w")
archivo.write(texto)
archivo.close()

# Lectura
archivo = open("archivo-prueba.txt", "r")
texto = archivo.read()
archivo.close()
print(texto)

# Lectura como lista
archivo = open("archivo-prueba.txt", "r")
texto = archivo.readlines()
archivo.close()
print(texto)

# With y Seek
with open("archivo-prueba.txt", "r") as archivo:
    print(archivo.readlines())
    archivo.seek(0)
    for linea in archivo:
        print(linea)

# Agregar
archivo = open("archivo-prueba.txt", "a+")
archivo.write("Chao mundo :(")
archivo.close()

# Lectura y escritura
with open("archivo-prueba.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito Feliz"
    archivo.writelines(texto)


