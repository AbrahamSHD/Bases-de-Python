import csv
import os

# * Escribir
# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([12244, 1, "Mi twit"])
#     writer.writerow([1223, 2, "Otro"])

#  * Leer
# with open("archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# * Actrualizar CSV
with open("archivos/archivo.csv", "r") as r, open("archivos/archivo_temp.csv", "w", newline='') as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if len(linea) > 0 and linea[0] == "1000":
            writer.writerow([1000, 1, "Texto super ultra modificado"])
        else:
            writer.writerow(linea)
os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
