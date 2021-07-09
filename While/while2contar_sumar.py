'''
Diseñe un algoritmo que permita contar y sumar los números pares e impares existentes en
 una serie de 1 a n, siendo n un número digitado por un usuario. 

A) Imprimir Contador de impares y pares.
b) Imprimir Suma de impares y pares.
'''
n=int(input("Digite el valor de n: "))
numeros = range(1, n)
suma_pares = 0
suma_impares = 0
conteo_pares = 0
conteo_impares = 0
while suma_pares <= n:
    numero = int(input("Digite un número: "))
    if (numero > 0) and (numero % 2 == 0):
        if numero <= n:
            suma_pares = suma_pares+numero #acumulador
            conteo_pares = conteo_pares + 1
    else:
        if suma_impares <= n:
            suma_impares = suma_impares+numero
            conteo_impares = conteo_impares + 1

print("La sumatoria de pares es: ", suma_pares, "y el conteo de pares es: ", conteo_pares)
print("La sumatoria de impares es: ", suma_impares, "y el conteo de impares es: ", conteo_impares)

