from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(frase, aes):
    data = frase.encode("utf-8")
    data = pad(data, 16)
    ciphertext = aes.encrypt(data)
    return ciphertext.hex()

def decrypt(frase, aes):
    data = bytes.fromhex(frase)
    
    if len(data)%16 != 0:
        data = pad(data, 16)
    
    deciphertext = aes.decrypt(data)
    return unpad(deciphertext, 16).decode("ascii")


print("Introduzca la frase:")
frase = input()
print("Introduzca la clave:")
clave = input()

key = clave.encode("utf-8")
aes = AES.new(key, AES.MODE_CBC, key)

print("1) Encriptar\n2) Desencriptar")
mode = int(input())
if mode == 1:
    print(encrypt(frase, aes))
elif mode == 2:
    print(decrypt(frase, aes))
else:
    print("El modo no es correcto")
