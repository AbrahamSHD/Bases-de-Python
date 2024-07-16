class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def obtener_nombre(self):
        return self.__nombre

    def cambiar_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre}: Guau Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito", 4)


perro1 = Perro.factory()
perro1.habla()
print(perro1.obtener_nombre())
print(perro1._Perro__nombre)
