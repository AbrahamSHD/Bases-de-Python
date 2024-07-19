from pathlib import Path
import os
import sys


def cli(args):
    if len(args) == 1:
        print("No se pasaron argumentos")
        return
    if len(args) != 3:
        print("Se necesitan dos argumentos")

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("Destino no puede existir")
        return

    os.rename(str(origen), str(destino))
    print("Archivo renombrado con Exito")


cli(sys.argv)
