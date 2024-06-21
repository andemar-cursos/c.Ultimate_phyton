class Perro:
  patas = 4

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  @classmethod
  def habla(cls):
    print("Guau!")

  @classmethod
  def factory(cls):
    return cls("Default Name", 0)


Perro.habla()
mi_perro = Perro.factory()
print(mi_perro.nombre, mi_perro.edad)
