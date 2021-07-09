'''
3. Leer 4 números. Imprimir la sumatoria y su promedio.
'''
suma = 0
contar = 0

for i in range(4):
    nuevoNumero=int(input("Introduce un número: "))
    suma += nuevoNumero
    contar= contar + 1

promedio = round(suma/contar,2)

print("El total es: ", suma, "y el promedio es: ", promedio)

