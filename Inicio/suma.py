#Algoritmo de la suma de dos numero
'''
Se desea la suma de dos numeros enteros y presentar en pantalla su resultado

ENTRADAS : Num1, Num2
PROCESO : La suma de los numeros --> Suma = Num1 + Num2
SALIDAS : La suma de los numeros --> Suma
INICIO
 Num1, Num2, Suma: Enteros
 ESCRIBA "Diga dos Numeros:"
 LEA Num1, Num2
 Suma <-- Num1 + Num 2
 ESCRIBA "La suma de los dos numeros es:", Suma
FIN

'''

#Suma dos numeros
numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))

suma= numero1+ numero2

# Resultado de la suma

print("La suma de dos numeros es :", suma)

