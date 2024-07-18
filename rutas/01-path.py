from pathlib import Path

# Path en Windows
# Path(r"C:\Archivos del Programa\Minecraft")

# Path en LINUX/MAC
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("nice/otro/abr")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("abraham.py")
print(p)

p = path.with_suffix(".bat")
print(p)

p = path.with_stem("felixz")
print(p)
