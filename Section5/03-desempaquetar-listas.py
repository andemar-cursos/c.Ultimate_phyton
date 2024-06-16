numeros = range(0, 20)

# Forma "analoga" de harcerlo
primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]

primero, segundo, *todos, penu, ultimo = numeros
print(primero, segundo, todos, penu, ultimo) # 0 1 [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] 18 19

