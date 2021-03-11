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

def encode_image(image_path):
    pass