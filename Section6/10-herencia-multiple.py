class Animal:
    def pasear(self):
        print("Paseando animales")


class Perro(): #
    def pasear(self):
        print("Paseando perros")


class PerroProgramador(Animal, Perro): # Paseando animales
    def programar(self):
        print("Programando")


mi_perro = PerroProgramador()
mi_perro.pasear()

# ----------------------------------------------------------------------


class Caminador:
    def caminar(self):
        print("Caminando")


class Volador:
    def volar(self):
        print("Volando")


class Nadador:
    def nadar(self):
        print("Nadando")


class Pato(Animal, Caminador, Volador, Nadador):
    def quack(self):
        print("QUACK!")


mi_pato = Pato()
mi_pato.pasear() # Paseando animales
mi_pato.quack() # QUAKK!

