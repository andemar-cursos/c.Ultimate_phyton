class Ave:
    def __init__(self):
        self.volador = "Volador"

    def vuela(self):
        print("Volando")


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = "Nadador"

    def vuela(self):
        print("No puedo volar")


mi_pato = Pato()
mi_pato.vuela() # No puedo volar
print(f"{mi_pato.volador} {mi_pato.nada}")

