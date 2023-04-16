alfabeto= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def cifrar(cadena, clave):
    textoCifrado = ''

    i = 0
    for letra in cadena:
        suma = alfabeto.find(letra) + alfabeto.find(clave[i % len(clave)])
        modulo = int(suma) % len(alfabeto)
        textoCifrado = textoCifrado + str(alfabeto[modulo])
        i = i+1

    return textoCifrado

def descifrar(cadena2, clave2):
    textoDesCifrado = ''

    i = 0
    for letra in cadena2:
        suma = alfabeto.find(letra) - alfabeto.find(clave[i % len(clave)])
        modulo = int(suma) % len(alfabeto)
        textoDesCifrado = textoDesCifrado + str(alfabeto[modulo])
        i = i+1

    return textoDesCifrado
cadena = str (input('Cadenaque se va a cifrar: '))
clave = str(input('introduzca la clave: '))
print (cifrar(cadena, clave))
cadena2 = str (input('Cadenaque se va a cifrar: '))
clave2 = str(input('introduzca la clave: '))
print (descifrar(cadena2, clave2))

