'''
Leer tres número enteros y determinar si el último dígito de los tres números es igual
'''
def numero(n,s,r):
    if int(n[-1]) == int(s[-1]) == int(r[-1]):
        return True
    else:
        return False

n = input("Ingrese un número: ")
s = input("Ingrese un número: ")
r = input("Ingrese un número: ")

respuesta = numero(n,s,r)

if respuesta == True:
    print("El último dígito de los tres números es igual")
else:
    print("El último dígito de los tres números no son iguales")

