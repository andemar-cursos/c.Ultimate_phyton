class Perro:
    patas = 4

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def __del__(self):
        print(f"Chao Perro :( {self.nombre}")

    def habla(self):
        print(f"{self.__nombre} te dice Guau!")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Default Name")


mi_perro = Perro("Test")
print(mi_perro) # Clase Perro: Test

texto = str(mi_perro)
print(texto) # Clase Perro: Test

del mi_perro # Chao Perro :( Test

