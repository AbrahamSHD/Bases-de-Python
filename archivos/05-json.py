import json
from pathlib import Path

# * Excribir Json
productos = [
    {"id": 1, "name": "Pc"},
    {"id": 2, "name": "Tv"},
    {"id": 3, "name": "Mouse"},
]

# data = json.dumps(productos)
# Path("archivos/productos.json").write_text(data)
# print(data)

# * Leer Json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
# print(productos)

# * Modificar Json
productos[0]["name"] = "Chanchito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))
