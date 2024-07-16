class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao perro {self.nombre}")

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre}: Guau Guau!")


perro = Perro("Chanchito", 3)
del perro
