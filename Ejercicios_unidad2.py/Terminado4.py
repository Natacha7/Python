'''
Leer un número entero y determinar si es un número terminado en 4
'''
def numero_entero(entero, numero):
    entero = numero % 10
        
    if entero == 4:
        print("El número termina en 4")
    else:
        print("El número no termina en 4")

numero = int(input("Digite un número: "))
entero = numero % 10
ent = numero_entero(entero, numero)









