class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre}: Guau Guau!")


mi_perro = Perro("Firulais", 2)
print(Perro.patas)
