from pathlib import Path
from zipfile import ZipFile

with ZipFile("comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "comprimidos.zip":
            zip.write(path)

