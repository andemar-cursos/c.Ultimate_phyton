numeros = (1, 2, 3) + (4, 5, 6) # (1, 2, 3, 4, 5, 6)
print(numeros)

punto = tuple([1, 2, 3]) # (1, 2, 3)
print(punto)

get_numbers_of_tupla = numeros[:2] # (1, 2)
print(get_numbers_of_tupla)

primero, segundo, *otros = numeros # 1 2 [3, 4, 5, 6]
print(primero, segundo, otros)

for n in numeros:  # 1 2 3 4 5 6
    print(n)

lista_numeros = list(numeros)
lista_numeros[0] = 9 # [9, 2, 3, 4, 5, 6]
print(lista_numeros)

