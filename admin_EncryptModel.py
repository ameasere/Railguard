from Cryptodome.Cipher import AES
import base64
from Cryptodome.Util.Padding import pad
from hashlib import sha256

with open('model.h5', 'rb') as f:
    model = f.read()
f.close()
print("SHA256: ", sha256(model).hexdigest())

cipher = AES.new('2FNJh1Yyii88G0jNFKLJR9yNjVQn7nm6'.encode(), AES.MODE_ECB)
encrypted = cipher.encrypt(pad(model, AES.block_size))
encrypted = base64.b64encode(encrypted)
with open('model.enc', 'wb') as f:
    f.write(encrypted)
f.close()
print("Finished encrypting!")