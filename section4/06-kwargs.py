def get_product(**datos):
  print(f"Id: {datos['id']} Nombre: {datos['name']} Description: {datos['desc']}")
  print(datos["id"], datos["name"], datos["desc"])


get_product(id="23", name="iPhone", desc="Esto es un iPhone")
