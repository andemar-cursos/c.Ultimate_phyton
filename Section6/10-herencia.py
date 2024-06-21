class Animal:
    def comer(self):
        print("Comiendo")


class Perro(Animal): # Herencia
    def pasear(self):
        print("Paseando")


class PerroProgramador(Perro): # Herencia multinivel (Maximo dos niveles como norma)
    def programar(self):
        print("Programando")


mi_perro = PerroProgramador()
mi_perro.comer() # Comiendo
mi_perro.pasear() # Paseando
mi_perro.programar() # Programando