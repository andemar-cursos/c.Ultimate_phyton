lista = {1, 1, 2, 2, 3, 4} # {1, 2, 3, 4}
print(lista)

# -------------------------

lista = {1, 1, 2, 2, 3, 4}
lista.add(5)
lista.remove(1)
print(lista) # {2, 3, 4, 5}

# -------------------------

lista2 = set([5, 6, 6, 7, 8]) # {6, 7, 8}
print(lista2)

# -------------------------
print(lista | lista2) # {2, 3, 4, 5, 6, 7, 8} Union
print(lista & lista2) # {5} Interseccion
print(lista - lista2) # {2, 3, 4} Diferencia
print(lista ^ lista2) # {2, 3, 4, 6, 7, 8} Diferencia Simetrica

# -------------------------

if 5 in lista:
    print("Existe el 5 en la lista")

