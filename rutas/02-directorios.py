from pathlib import Path

path = Path("rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("hola")

# print(path.iterdir())

# for p in path.iterdir():
#     print(p)

# archivos = [p for p in path.iterdir() if not p.is_dir()]
# archivos = [p for p in path.glob("**/*.py")]
archivos = [p for p in path.rglob("*.py")]
print(archivos)