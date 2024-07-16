
buscar = 4

for numero in range(3):
    print(numero)
    if numero == buscar:
        print("Encontrado: ", numero)
        break
else:
    print('Número no encontrado: ', buscar)

for char in "Ultimate Python":
    print(char)
