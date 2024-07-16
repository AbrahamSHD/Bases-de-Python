mascotas = ["Pelusa", "Chanchito", "Wolfgang", "Juan", "Felipe", "Feliz"]

nombre = "Wolfgang"

if nombre in mascotas:
    print(f"{nombre} aparece {mascotas.count(nombre)} veces")
    print(f"{nombre} está en el index {mascotas.index(nombre)}")
else:
    print(f"{nombre} is not in list")
