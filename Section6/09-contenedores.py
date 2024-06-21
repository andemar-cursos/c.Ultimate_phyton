class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, productos):
        self.productos.append(productos)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)

deportes = Categoria("Deportes", [kayak, bicicleta, surfboard])
raqueta = Producto("Raqueta", 250)
deportes.agregar(raqueta)

deportes.imprimir()
# Producto: Kayak - Precio: 1000
# Producto: Bicicleta - Precio: 750
# Producto: Surfboard - Precio: 500
# Producto: Raqueta - Precio: 250

