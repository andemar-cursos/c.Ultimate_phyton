class Perro:
    patas = 4

    def __init__(self, nombre):
        self.nombre = nombre

    def habla(self):
        print(f"{self.__nombre} te dice Guau!")

    @property
    def nombre(self):
        print("getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("setter")
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Default Name")


mi_perro = Perro("Test") # setter
mi_perro.nombre = "Chanchito" # setter
print(mi_perro.nombre) # getter

