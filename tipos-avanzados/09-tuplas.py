numeros = (1, 2, 3) + (4, 5, 6)

print(numeros)

punto = tuple([1, 2])

print(punto)

menosNumeros = numeros[:2]

print(menosNumeros)

primero, segundo, *mas = numeros
print(primero, segundo, mas)

for n in numeros:
    print(n)