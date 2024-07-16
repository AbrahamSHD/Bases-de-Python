from abc import ABC, abstractmethod


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando usuario por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("Guardando Usuario")


usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(212)
