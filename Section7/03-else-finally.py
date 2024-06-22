try:
    n1 = int(input("Ingresa primer numero\n"))
except Exception as e:
    print("Ocurrio un error!")
else:
    print("No ocurrio ningun error")
finally:
    print("Me ejecuto siempre")

