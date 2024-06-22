class MiException(ArithmeticError):

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return f"Mensaje: {self.message} - Code: {self.code}"


def division(n=0):
    if n == 0:
        raise MiException("No es posible dividir entre cero", 523)
    return 10/n


try:
    division(0)
except MiException as e:
    print(e)

