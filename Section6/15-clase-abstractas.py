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
    def buscar_por_id(self, id):
        print(f"Buscando por id {id}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f"Guardando Usuario en BBDD")


mi_usuario = Usuario()
mi_usuario.guardar() # Guardando Usuario en BBDD
Usuario.buscar_por_id("123") # Buscando por id 123

