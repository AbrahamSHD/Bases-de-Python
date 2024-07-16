class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito", 4)


Perro.habla()
perro1 = Perro("Firulais", 3)
perro2 = Perro("Firulais", 3)
perro3 = Perro.factory()

print(perro3.edad, perro3.nombre)
