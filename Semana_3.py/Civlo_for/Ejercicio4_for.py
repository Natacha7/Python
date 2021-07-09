'''
4. Leer 10 números e imprimir la sumatoria de los pares, impares y la suma total de los 10 números. 
'''
total=0
pares=0
impares=0

for i in range(10):
    nuevoNumero=int(input("Introduce un número: "))
    total += nuevoNumero
    if nuevoNumero % 2 ==0:
        pares = pares + nuevoNumero
    else:
        impares = impares + nuevoNumero

print("La suma de los número es: ", total, "la suma de los pares es: ", pares, "y la suma de los impares es: ", impares)

