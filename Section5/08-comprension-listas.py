usuariosWithoutIndex = [
  ["Martinez", 4],
  ["Andemar", 3],
  ["Felipe", 2],
  ["Pulga", 1]
]

# Transformacion
nombres = [valor[0] for valor in usuariosWithoutIndex] # ['Andemar', 'Felipe', 'Pulga']
print(nombres)

# Filtros
nombresPar = [valor for valor in usuariosWithoutIndex if (valor[1] % 2) == 0] # [['Martinez', 4], ['Felipe', 2]]
print(nombresPar)

