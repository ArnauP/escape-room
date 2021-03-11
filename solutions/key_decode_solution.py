import base64

f = open("key", "r")
img = f.read()

with open("key.png", "wb") as fh:
    fh.write(base64.b64decode(img))

