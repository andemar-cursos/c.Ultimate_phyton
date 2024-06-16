lista1 = [1, 2, 3, 4, 5]
print(lista1) # [1, 2, 3, 4, 5]
print(*lista1) # 1 2 3 4 5

lista2 = [5, 6]

combinada = None

combinada = ["Hola", lista1, "mundo", lista2, "Andemar"]
print(combinada) # ['Hola', [1, 2, 3, 4, 5], 'mundo', [5, 6], 'Andemar']
combinada = ["Hola", *lista1, "mundo", *lista2, "Andemar"]
print(combinada) # ['Hola', 1, 2, 3, 4, 5, 'mundo', 5, 6, 'Andemar']


punto1 = {"x": 19}
punto2 = {"y": 20}

nuevoPunto = None

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto) # {'x': 19, 'y': 20}
nuevoPunto = {**punto1, "lala": "hola mundo", **punto2}
print(nuevoPunto) # {'x': 19, 'lala': 'hola mundo', 'y': 20}

