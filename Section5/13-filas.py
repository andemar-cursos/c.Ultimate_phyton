from collections import deque

fila = deque([1, 2])
fila.append(3)
print(fila) # deque([1, 2, 3])

fila.popleft()
print(fila) # deque([2, 3])

fila.popleft()
fila.popleft()
if not fila:
    print('FILA EMPTY') # FILA EMPTY



