class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, id):
        print(f"Buscando por id {id}")


class Usuario(Model):
    tabla = "Usuario"


mi_usuario = Usuario()
mi_usuario.guardar() # Guardando Usuario en BBDD
Usuario.buscar_por_id("123") # Buscando por id 123

