from PyQt5.QtCore import QFile, QTextStream
import base64
import os


def get_path(path):
    base_path = os.getcwd()
    return os.path.join(base_path, path)


def load_style_sheet(stylesheet, obj):
    file = QFile(stylesheet)
    file.open(QFile.ReadOnly)
    obj.setStyleSheet(QTextStream(file).readAll())
    file.close()


def encode_image(image_path, target_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    f = open(target_path, "w")
    f.write(encoded_string)
    f.close()
