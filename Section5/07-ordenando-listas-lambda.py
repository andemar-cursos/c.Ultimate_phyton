usuariosWithoutIndex = [
  ["Andemar", 3],
  ["Felipe", 2],
  ["Pulga", 1]
]

usuariosWithoutIndex.sort(key=lambda el: el[1]) # [['Pulga', 1], ['Felipe', 2], ['Andemar', 3]]
print(usuariosWithoutIndex)


