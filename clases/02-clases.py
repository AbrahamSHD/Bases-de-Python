class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre}: Guau Guau!")


mi_perro1 = Perro('Firulais', 12)
mi_perro2 = Perro('Chanchito', 4)

print(mi_perro1.nombre)
print(mi_perro1.edad)
print(mi_perro2.nombre)

# print(type(mi_perro1))
# print(isinstance(mi_perro1, str))
