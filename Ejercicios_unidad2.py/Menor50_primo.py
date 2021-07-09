'''
Leer un número entero menor que 50 y positivo y determinar si es un número primo
'''
def num(n):
    if n >= 0 and n < 50:
        return True
    else:
        return False

def es_primo(n):
    for i in range (2, n):
        if n % i == 0:
            return False
        else: 
            return True

numero = int(input("Digite un numero: "))
numero_menor50_positivo = num(numero)
Es_primo = es_primo(numero)

if numero_menor50_positivo == True and Es_primo == True:
    print("El número es positivo, menor que 50 y es primo")
else:
    print("El número no cumple con las condiciones")



