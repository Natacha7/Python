'''
Elaborar un algoritmo que permita averiguar si una persona debe sacar cédula de ciudadanía, 
Si la persona es mayor de 17 años debe imprimir 
“Debe sacar cédula de ciudadanía” en caso contrario imprimir “No debe solicitar cédula”.
'''
Edad = int(input("Digite su edad: "))

if Edad >= 18:
     print("Debe sacar cédula de ciudadanía")
else:
     print("No debe solicitar cédula")

