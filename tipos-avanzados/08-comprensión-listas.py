usuarios = [
    [1, "Hola"],
    [3, "asfsa"],
    [2, "wsdfce"],
    [5, "swedc"]
]

nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[1])
# print(nombres)

# * Tranformar
# nombres = [usuario[1] for usuario in usuarios]

# * Filtar
# nombres = [usuario for usuario in usuarios if usuario[0] > 2]

# * Filtar y transformar
# nombres = [usuario[1] for usuario in usuarios if usuario[0] > 2]

# nombres = list(map(lambda usuario: usuario[1], usuarios))

nombres = list(filter(lambda usuario: usuario[0] > 2, usuarios))

print(nombres)
