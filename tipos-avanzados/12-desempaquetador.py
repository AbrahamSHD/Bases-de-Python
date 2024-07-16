lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(*lista)

lista2 = [5, 6]

combinada = ["dsankj", *lista, *lista2]
print(combinada)

combinada2 = ["asdwa", lista, lista2]
print(combinada2)

punto1 = {"x": 12}
punto2 = {"y": 43}

nuevoPunto = {**punto1, **punto2, "z": 453}
print(nuevoPunto)
