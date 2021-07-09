'''
Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares
'''
n = input("Digite un número de 4 digitos: ")

if int(n[0]) % 2 == 0 and int(n[1]) % 2 == 0 and int(n[2]) % 2 == 0 and int(n[3]) % 2 == 0:
        print("El número tiene más dígitos pares ")
elif int(n[0]) % 2 == 0 and int(n[1]) % 2 == 0 and int(n[2]) % 2 == 0:
        print("El número tiene más dígitos pares ")
elif int(n[0]) % 2 == 0 and int(n[1]) % 2 == 0 and int(n[3]) % 2 == 0:
        print("El número tiene más dígitos pares ")
elif int(n[0]) % 2 == 0 and int(n[2]) % 2 == 0 and int(n[3]) % 2 == 0:
        print("El número tiene más dígitos pares ")
elif int(n[1]) % 2 == 0 and int(n[2]) % 2 == 0 and int(n[3]) % 2 == 0:
        print("El número tiene más dígitos pares ")
elif int(n[0]) % 2 != 0 and int(n[1]) % 2 != 0 and int(n[2]) % 2 == 0 and int(n[3]) % 2 == 0:
        print("El número tiene igual número de dígitos pares e impares ")
elif int(n[0]) % 2 != 0 and int(n[1]) % 2 == 0 and int(n[2]) % 2 != 0 and int(n[3]) % 2 == 0:
        print("El número tiene igual número de dígitos pares e impares ")
elif int(n[0]) % 2 != 0 and int(n[1]) % 2 == 0 and int(n[2]) % 2 == 0 and int(n[3]) % 2 != 0:
        print("El número tiene igual número de dígitos pares e impares ")
elif int(n[0]) % 2 == 0 and int(n[1]) % 2 != 0 and int(n[2]) % 2 != 0 and int(n[3]) % 2 == 0:
        print("El número tiene igual número de dígitos pares e impares ")
elif int(n[0]) % 2 == 0 and int(n[1]) % 2 != 0 and int(n[2]) % 2 == 0 and int(n[3]) % 2 != 0:
        print("El número tiene igual número de dígitos pares e impares ")
elif int(n[0]) % 2 == 0 and int(n[1]) % 2 == 0 and int(n[2]) % 2 != 0 and int(n[3]) % 2 != 0:
        print("El número tiene igual número de dígitos pares e impares ")
elif int(n[0]) % 2 != 0 and int(n[1]) % 2 != 0 and int(n[2]) % 2 != 0 and int(n[3]) % 2 == 0:
        print("El número tiene mas dígitos impares ")
elif int(n[0]) % 2 != 0 and int(n[1]) % 2 != 0 and int(n[2]) % 2 == 0 and int(n[3]) % 2 != 0:
        print("El número tiene mas dígitos impares ")
elif int(n[0]) % 2 == 0 and int(n[1]) % 2 != 0 and int(n[2]) % 2 != 0 and int(n[3]) % 2 != 0:
        print("El número tiene mas dígitos impares ")
else:
      print("error")
    


