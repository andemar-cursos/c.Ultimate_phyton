mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0]) # Wolfgang
mascotas[0] = "Bicho"
print(mascotas) # ['Bicho', 'Pelusa', 'Pulga', 'Copito']
print(mascotas[2:]) # ['Pulga', 'Copito']
print(mascotas[-1]) # Copito
print(mascotas[1:2:2]) # ['Pelusa']

numeros = list(range(21))
print(numeros[::2]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] Par
print(numeros[1::2]) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] Inpar