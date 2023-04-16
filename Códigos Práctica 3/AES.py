from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_CBC, key)
    ciphertext = cipher.encrypt(data)
    return ciphertext.hex()

def decrypt(key, data):
    decipher = AES.new(key, AES.MODE_CBC, key)
    
    if len(data)%16 != 0:
        data = pad(data, 16)
    
    deciphertext = decipher.decrypt(data)
    return unpad(deciphertext, 16).decode("ascii")


print("Introduzca la frase:")
frase = input()
print("Introduzca la clave:")
clave = input()

key = clave.encode("utf-8")

print("1) Encriptar\n2) Desencriptar")
mode = int(input())
if mode == 1:
    data = frase.encode("utf-8")
    data = pad(data, 16)
    print(encrypt(key, data))
elif mode == 2:
    data = bytes.fromhex(frase)
    print(decrypt(key, data))
else:
    print("El modo no es correcto")