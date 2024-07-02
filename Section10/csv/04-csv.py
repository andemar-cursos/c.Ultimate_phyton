import csv
import os

# Escribir
with open("archivo.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twit_id", "user_id", "text"])
    writer.writerow([1000, 1, "Este es un twit"])
    writer.writerow([1001, 2, "Otro twit"])


# Leer
with open("archivo.csv") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        print(linea)


# Actualizar
with open("archivo.csv") as r, open("archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if not linea:
            pass
        elif linea[0] == "1000":
            writer.writerow([1000, 1, "Texto modificado"])
        else:
            writer.writerow(linea)

os.remove("archivo.csv")
os.rename("archivo_temp.csv", "archivo.csv")

