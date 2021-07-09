'''
Leer un número entero y determinar si tiene 3 digitos
'''
def numero_entero(entero):
    
    if (entero>=100) and (entero<=999):
        print("El número tiene 3 digitos")
    else:
        print("El número no tiene 3 digitos")
    return numero_entero

entero = int(input("Digite un número: "))
ent = numero_entero(entero)


