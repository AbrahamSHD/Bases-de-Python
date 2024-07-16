punto = {
    "x": 23,
    "y": 2133,
    "z": 43534,
}

print(punto["y"])
print(punto.get("x"))
print(punto.get("ya", 12))

del punto["x"]
print(punto)
del (punto["y"])
print(punto)

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1232143234, "nombre": "Abraham"},
    {"id": 1232134434, "nombre": "Juan"},
    {"id": 3465234564, "nombre": "Perez"},
    {"id": 7534565435, "nombre": "Suarez"},
]

for usuario in usuarios:
    print(usuario["nombre"])
