from pathlib import Path

archivo = Path("archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
texto.insert(0, "Andemar!")
archivo.write_text("\n".join(texto), "utf-8")

