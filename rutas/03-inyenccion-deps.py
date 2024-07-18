from pathlib import Path

dependecias = {
    "db": "Postgres",
    "api": "BlogApi",
    "graphql": "Graphql",
}

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]


def load(pack):
    paquete = __import__(str(pack).replace("/", "."))
    try:
        paquete.init(**dependecias)
    except:
        print("El paquete no tiene funciones init")


list(map(load, paths))
