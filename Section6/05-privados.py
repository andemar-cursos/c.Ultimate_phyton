class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.__nombre} te dice Guau!")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Default Name", 0)


mi_perro = Perro.factory()
mi_perro.habla() # Default Name te dice Guau!

mi_perro.set_nombre("Chanchito")
mi_perro.habla() # Chanchito te dice Guau!
print(mi_perro._Perro__nombre) # Chanchito | Accediendo a los metodos usando el dict (Dictionary)
