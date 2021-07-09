'''
Leer un número entero de tres digitos y leer si algún digito es múltiplo de otros
'''

s = input("Digite un número entero de tres digitos: ")

if int(s[0]) % int(s[1]) == 0:
    print("El digito en la posición 0 es múltiplo del digito en la posición 1 ")
elif int(s[1]) % int(s[0]) == 0:
    print("El digito en la posición 1 es múltiplo del digito en la posición 0 ")
elif int(s[0]) % int(s[2])==0:
    print("El digito en la posición 0 es múltiplo del digito en la posición 2 ")
elif int(s[1]) % int(s[2])==0:
    print("El digito en la posición 1 es múltiplo del digito en la posición 2 ")
elif int(s[2]) % int(s[0])==0:
    print("El digito en la posición 2 es múltiplo del digito en la posición 0 ")
elif int(s[2]) % int(s[1])==0:
    print("El digito en la posición 2 es múltiplo del digito en la posición 1 ")

