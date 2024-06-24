from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
  "db": "Base de datos",
  "api": "Esta es una API",
  "graphql": "Esto es Graphql"
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except():
        print("No tiene init()")


list(map(load, paths))

