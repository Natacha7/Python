'''
Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al
penúltimo
'''
def numero(n):
    if int(n) >= 1000 and int(n) <= 9999:
        if int(n[1]) == int(n[-2]):
            return True
    else:
        return False

Cuatrodigitos = input("Ingrese un número: ")
respuesta = numero(Cuatrodigitos)

if respuesta == True:
    print("El número tiene cuatro digitos y el segundo dígito es igual a penúltimo")
else:
    print("El número no cumple las condiciones")


