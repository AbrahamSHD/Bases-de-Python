class Caminante:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadando(self):
        print("nadando")


class Pato(Caminante, Nadador):

    def programando(self):
        print("Programando")


chancho = Pato()
