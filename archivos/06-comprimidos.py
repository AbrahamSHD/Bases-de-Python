from pathlib import Path
from zipfile import ZipFile

# * Crear archivos comprimidos
# with ZipFile("archivos/comprimidos.zip", "w") as zip:
# Python-HM
# for path in Path().rglob("*.*"):
#     print(path)
#     if str(path) != "archivos/comprimidos.zip":
#         zip.write(path)

# * Leer archivos comprimidos
with ZipFile("archivos/comprimidos.zip") as zip:
    # print(zip.namelist())
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall("archivos/descomprimidos")
