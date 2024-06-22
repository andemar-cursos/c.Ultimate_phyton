def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return 10/n


try:
    division(0)
except ZeroDivisionError as e:
    print(e)

