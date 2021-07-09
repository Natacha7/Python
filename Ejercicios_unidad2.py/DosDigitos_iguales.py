'''
Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
'''
def numero(n):
    if int(n) >= 10 and int(n) <= 99:
        if int(n[0]) == int(n[1]):
            return True
    else:
        return False

Dosdigitos = input("Ingrese un número: ")
respuesta = numero(Dosdigitos)

if respuesta == True:
    print("El número tiene dos digitos iguales")
else:
    print("El número no tiene los dos digitos iguales")

