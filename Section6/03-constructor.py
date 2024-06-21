class Perro:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad


  def habla(self):
    print(f"{self.nombre} te dice Guau!")


mi_perro = Perro("Chanchito", 10)
mi_perro2 = Perro("YUI", 4)
print(mi_perro.nombre)
print(mi_perro2.nombre)

mi_perro.habla()
mi_perro2.habla()

