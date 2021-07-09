'''
Leer un número entero de 3 digitos y determinar en qué posición está el mayor dígito
'''

s = input("Digite un número entero de 3 digitos: ")

if int(s[0]) > int(s[1]) and int(s[0]) > int(s[2]):
    print("El mayor digito está en la posición 0")
elif int(s[1]) > int(s[0]) and int(s[1]) > int(s[2]):
    print("El mayor digito está en la posición 1")
elif int(s[2]) > int(s[0]) and int(s[2]) > int(s[1]):
    print("El mayor digito está en la posición 2")


