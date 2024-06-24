from pathlib import Path

# Path(r"D:\archivos\promgramacion")

path = Path("andemar/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name, # mi-archivo.py
    path.stem, # mi-archivo
    path.suffix, # .py
    path.parent, # andemar
    path.absolute() # X:\repos\andemar-cursos\c.Ultimate_phyton\Section9\andemar\mi-archivo.py
)

