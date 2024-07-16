mascotas = ["Pelusa", "Chanchito feliz", "Wolfgang", "Juan", "Felipe", "Feliz"]

mascotas.insert(1, "Melvin")
print(mascotas)

mascotas.append("Chanchito triste")
print(mascotas)

mascotas.remove("Pelusa")
print(mascotas)

mascotas.pop()
print(mascotas)

mascotas.pop(1)
print(mascotas)

del mascotas[0]
print(mascotas)

mascotas.clear()
print(mascotas)
