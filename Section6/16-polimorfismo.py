from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("Guardando Usuarios...")


class Session(Model):
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidad):
    entidad.guardar()


def guardar_all(entidades):
    for entidad in entidades:
        entidad.guardar()


mi_usuario = Usuario()
mi_session = Session()

guardar(mi_usuario) # Guardando Usuarios...
guardar(mi_session) # Guardando en archivo
guardar_all([mi_usuario, mi_session]) # Guardando Usuarios... | Guardando en archivo

