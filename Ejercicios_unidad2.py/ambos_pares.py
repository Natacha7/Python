'''
Leer un número entero de dos digitos y determinar si ambos digitos son pares
'''
def numero_entero(entero):
    
    if (entero>=10) and (entero<=99) and (entero%2==0):
        print("El número tiene 2 digitos y son pares")
    elif (entero>=10) and (entero<=99) and (entero%2!=0):
        print("El número tiene 2 digitos y no son pares")
    return numero_entero

entero=int(input("Digite un número: "))
ent=numero_entero(entero)
