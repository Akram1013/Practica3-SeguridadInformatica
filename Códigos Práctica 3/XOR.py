print("Introducir frase: ")
desencrip = input()
print("Introducir clave: ")
key = input()

result = []

for i in range (len(desencrip)):
    j = i%len(key)
    result.append((ord(desencrip[i]) ^ ord(key[j])))

for i in range(len(result)):
    print(chr(result[i]), end="")

print("")