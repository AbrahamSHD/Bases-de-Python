# lista = list([1, 2, 3, 4])

# lista.append(5)
# lista.insert(0, 0)

# print(lista)

class Lista(list):
    def prepent(self, item):
        self.insert(0, item)


lista = Lista([1, 2, 3, 4])
lista.append(5)
lista.prepent(0)

print(lista)
