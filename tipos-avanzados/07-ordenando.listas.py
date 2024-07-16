numeros = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 98, 9, 945, 45, 23, 3, 23, 23]

numeros.sort()
print(numeros)

# numeros.sort(reverse=True)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)

usuarios = [[1, "Hola"], [3, "asfsa"], [2, "wsdfce"], [5, "swedc"]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=lambda param: param[1])
print(usuarios)
