n1 = input("Ingresa primer número")
n2 = input("Ingresa segundo número")

n1 = int(n1)
n2 = int(n2)

print(n1 + n2)

suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

message = f"""
  Para los números {n1} y {n2},
  el resultado de la suma es {suma}
  el resultado de la resta es {resta}
  el resultado de la multiplicación es {mult}
  el resultado de la división es {div}
"""

print(message)
