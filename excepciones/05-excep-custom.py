class MiError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - codigo {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError(f"No se puede dividir por {n}", 404)
    return 5 / n


try:
    division()
except MiError as ex:
    print(ex)
