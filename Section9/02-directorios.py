from pathlib import Path

path = Path()
archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)
archivos = [p for p in path.glob("*.py")]
print(archivos)

