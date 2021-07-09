'''
1. Introducir 10 números y sumar solo los números pares. Imprimir la sumatoria
'''

suma=0

for i in range(10):
    Numero=int(input("Introduce un número: "))
    if Numero % 2 ==0:
        suma += Numero

print("La suma de los número pares es: ", suma)


