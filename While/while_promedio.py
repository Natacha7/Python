'''
Algoritmo que permita obtener el promedio de la cantidad de números 
que el  usuario desee digitar, preguntando además si desea continuar o no.
'''
suma_numeros = 0
numero = 0
continuar = ""
cantidad_numeros = 0

while continuar != "no":
    continuar = input("Desea continuar? (si/no)): ")
    if continuar == "si":
        numero = float(input("Digite un número: "))
        cantidad_numeros = cantidad_numeros + 1
        suma_numeros = suma_numeros + numero
        
promedio = suma_numeros / cantidad_numeros 

print(("El promedio de los números digitados es: " ), round(promedio))
print("La cantidad de numeros digitados es: ", cantidad_numeros)