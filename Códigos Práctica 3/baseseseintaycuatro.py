import base64

#CODIFICACION
print()
cadena = b"2023_SeguridadInformaticaBase64"
cifras_hex= base64.b64encode(cadena)
print(cifras_hex)

print()

#DECODIFICACION
cadena = base64.b64decode(cifras_hex)
print(cadena)
