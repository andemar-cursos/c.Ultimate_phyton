import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)
print(
    random.random(), # 0.1109634857477888
    random.randint(1, 10), # Aleatorio 1 a 10
    lista, # [5, 7, 8, 1, 6, 2, 3, 4] (aleatorio)
    random.choice(lista2), # Aleatorio 1 a 10
    random.choices(lista2, k=3) # [5, 7, 2] Aleatorios 3 numeros
)

chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
print(seleccion) # ['K', 'd', 'Z', 'C', 't', 'o', '6', 'j', 'q', '5', 'c', 'n', 'L', 'y', 'M', 'P'] Aleatorio
password = "".join(seleccion)
print(password) # KdZCto6jq5cnLyMP Aleatorio

