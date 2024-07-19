import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(lista)

# print(
#     random.random(),
#     random.randint(1, 100),
#     lista,
#     random.choice(lista2),
#     random.choices(lista2, k=4),
#     random.choices("asfefsadc3e434243rwfe", k=4),
#     "".join(random.choices("asfefsadc3e434243rwfe", k=4)),
# )

chars = string.ascii_letters
digitos = string.digits
selection = random.choices(chars + digitos, k=10)
print(selection)

password = "".join(selection)
print(password)
