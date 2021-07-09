'''
Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.
'''


def es_primo(numero): 
    for i in range (2,numero):
        if numero > 0:
            if numero % i == 0:
                return True
            else:
                return False

numero = int(input("Digite un número de dos dígitos: "))

if es_primo(numero) == True:
    print("El número", numero, "es positivo y es primo")
elif es_primo(numero) == False:
    print("El número", numero, "es positivo y no es primo")
elif numero < 0:
    print("El número", numero, "es negativo y no es primo")





      