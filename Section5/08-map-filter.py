usuariosWithoutIndex = [
  ["Martinez", 4],
  ["Andemar", 3],
  ["Felipe", 2],
  ["Pulga", 1]
]

# Transformacion
nombres = list(map(lambda usuario: usuario[0], usuariosWithoutIndex)) # ['Martinez', 'Andemar', 'Felipe', 'Pulga']
print(nombres)

# Filtros
nombresPar = list(filter(lambda usuario: (usuario[1] % 2) == 0, usuariosWithoutIndex)) # [['Martinez', 4], ['Felipe', 2]]
print(nombresPar)

