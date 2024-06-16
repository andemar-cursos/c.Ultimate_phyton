pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila) # [1, 2, 3]
ultimoElemento = pila.pop()
print(pila) # [1, 2]
print(pila[-1]) # 2

pila.pop()
pila.pop()
if not pila:
    print("EMPTY QUEUE") # EMPTY QUEUE

