import os
from shutil import move
from pathlib import Path

#change format of path for linux
dir = "/home/arstech/Downloads/file"


def start():
    a = os.listdir(dir)
    pathToFile = Path(dir)

    for pdfPath in pathToFile.glob("*.pdf"):
        dirPath = pathToFile / pdfPath.stem
        dirPath.mkdir()
        move(pdfPath, dirPath / pdfPath.name)

    for i in a:
        try:
            os.mkdir(os.path.join(dir, i.split(".")[0]))
        except OSError as error:
            print(error)


if __name__ == '__main__':
    start()
