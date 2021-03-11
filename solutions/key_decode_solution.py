import base64

f = open("key.skey", "r")
img = f.read()

with open("key.png", "wb") as fh:
    fh.write(base64.b64decode(img))

