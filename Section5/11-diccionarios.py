punto = {"x": 25, "y": 50}
print(punto) # {'x': 25, 'y': 50}
print(punto["x"]) # 25

punto["z"] = 75
print(punto) # {'x': 25, 'y': 50, 'z': 75}

if "lala" in punto:
    print("Encontre a lala") # ""

print(punto.get("x")) # 25
print(punto.get("lala")) # None
print(punto.get("lala", 97)) # 97

del punto["x"]
del (punto["y"])
print(punto) # {'z': 75}

for keys in punto:
    print(keys) # z


for keys in punto:
    print(keys, punto[keys]) # z 75


for keys in punto.items():
    print(keys) # ('z', 75)


for key, value in punto.items():
    print(key, value) # z 75


usuarios = [
  {"id": 1, "nombre": "John"},
  {"id": 2, "nombre": "Feliz"},
  {"id": 3, "nombre": "Nicolas"},
  {"id": 4, "nombre": "Andemar"},
]

for usuario in usuarios:
    print(usuario["nombre"]) # John Feliz Nicolas Andemar

