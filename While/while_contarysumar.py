'''
Diseñe un algoritmo que permita contar y sumar los números pares e impares existentes en una
 serie de 1 a n, siendo n un número digitado por
 un usuario. 

A) Imprimir Contador de impares y pares.
b) Imprimir Suma de impares y pares.
'''

def contar_pares_impares(lista):
    pares, impares = 0, 0
        
    for x in lista:
        if x % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

n=int(input("Digite el valor de n: "))
numeros = range(1, n)

resultado = contar_pares_impares(numeros)

suma_pares = 0
suma_impares = 0
while suma_pares <= n:
    numero = int(input("Digite un número: "))
    if (numero > 0) and (numero % 2 == 0):
        if numero <= n:
            suma_pares = suma_pares+numero #acumulador
    else:
        if suma_impares <= n:
            suma_impares = suma_impares+numero

print("La cantidad de pares es: %i" %resultado[0])
print("La cantidad de impares es: %i" %resultado[1])
print("La suma de pares es: ", suma_pares)
print("La suma de impares es: ", suma_impares)
    
