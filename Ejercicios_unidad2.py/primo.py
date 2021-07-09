'''
Leer un número entero de dos dígitos menor que 20 y determinar si es primo
if D%d != 0: print("No es divisor")
def es_primo(num): for n in range(2, num): if num % n == 0: print("No es primo", n, "es divisor") return False print("Es primo") return True.
'''

def num(n):
    if n >= 10 and n < 20:
        return True
    else:
        return False

def es_primo(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

numero=int(input("Digite un numero: "))

Dos_digitos= num(numero)
Es_primo= es_primo(numero)

if Dos_digitos ==True and Es_primo==True:
    print("El número es de dos digitos y es primo")
else:
    print("El número no cumple con las condiciones")



