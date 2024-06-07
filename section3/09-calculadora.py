print("""
Bienvenidos a la calculadora
Para salir escribe Salir
Las operaciones son suma, multi, div y resta
""")

sInput = input("Ingresa numero: ")
operation = ""
principalNumer = int(sInput)
secondaryNumber = 0

while True:
  operation = input("Ingresa operacion: ")

  if operation.lower() == "salir":
    break

  secondaryNumber = int(input("Ingresa siguiente numero: "))

  if operation == "suma":
    principalNumer += secondaryNumber
  elif operation == "multi":
    principalNumer *= secondaryNumber
  elif operation == "div":
    principalNumer /= secondaryNumber
  elif operation == "resta":
    principalNumer -= secondaryNumber

  print(f"El resultado es: {principalNumer}")
