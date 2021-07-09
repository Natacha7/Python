'''
Leer un número entero menor que mil y determinar cuántos dígitos tiene
'''
def menor_mil(n):
    if int(n) < 1000:
        return True
    return False

numero = input("Digite un numero: ")

Menor_mil = menor_mil(numero)

len(numero)

if Menor_mil == True:
    print("El número es menor que mil y tiene:",len(numero), "digitos")
else:
    print("El número no cumple con las condiciones")

