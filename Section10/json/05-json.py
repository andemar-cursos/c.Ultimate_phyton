import json
from pathlib import Path

# Escribir Json
productos = [
  {"id": 1, "name": "Surfboard"},
  {"id": 2, "name": "Bicicleta"},
  {"id": 3, "name": "Skate"}
]
data = json.dumps(productos)
Path("productos.json").write_text(data)


# Leer
data = Path("productos.json").read_text(encoding="UTF-8")
productos = json.loads(data)
print(productos)


#Modificar
productos[0]["name"] = "Chanchito Feliz"
Path("productos.json").write_text(json.dumps(productos))

