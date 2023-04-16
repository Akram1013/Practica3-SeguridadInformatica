abc = 'abcdefghijklmnopqrstuvwxyz'
def cifrar(cadena,clave):

    texto_cifrado =''
    for letra in cadena:
        suma = abc.find(letra) + clave
        modulo = int(suma) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[modulo])
    return texto_cifrado


def descifrar(cadena, clave):

    texto_descifrado = ''
    for letra in cadena:
        suma = abc.find(letra) - clave
        modulo = int(suma) % len(abc)
        texto_descifrado = texto_descifrado + str(abc[modulo])
    return texto_descifrado


print('Quieres cifrar o descifrar un texto \n1)cifrar\n2)descifrar')
opcion = int(input())
if opcion == 1 :
    c = str(input('cadena a cifrar: ')).lower().strip()
    n = int(input('clave numerica: '))
    print(cifrar(c, n))
elif opcion== 2:
    cc = str(input('cadena a descifrar: ')).lower().strip()
    print('¿Sabes la clave numerica? s/n')
    m = input()
    while m != 's' and m != 'n':
        print('seleccione una opcion valida')
        m =input()
    if m == 's':
        cn = int(input('clave numerica: '))
        print(descifrar(cc, cn))
    else:
        for i in range(1,26):
            print('rot ', i, ': ',descifrar(cc,i))
else:
    print('Esa opcion no es correcta')




