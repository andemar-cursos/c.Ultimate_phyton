numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort(reverse=True) # [75, 45, 22, 4, 2, 1] Se modifica la lista "original"
numeros2 = sorted(numeros, reverse=True) # Se crea una nueva lista, ordenada, en base a la lista original.
print(numeros)
print(numeros2)

# ----------------------

usuarios = [
  [3, "Andemar"],
  [2, "Felipe"],
  [1, "Pulga"]
]
usuarios.sort() # [[0, 'Andemar'], [1, 'Felipe'], [2, 'Pulga']]
print(usuarios)

# ----------------------------

usuariosWithoutIndex = [
  ["Andemar", 3],
  ["Felipe", 2],
  ["Pulga", 1]
]


def ordenar(numer):
    return numer[1]


usuariosWithoutIndex.sort(key=ordenar) # [['Pulga', 1], ['Felipe', 2], ['Andemar', 3]]
print(usuariosWithoutIndex)


