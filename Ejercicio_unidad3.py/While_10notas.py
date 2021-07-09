'''
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos
tienen notas mayores o iguales a 7 y cuántos menores.
'''

notas_mayores_iguales_7 = 0
notas_menores_7 = 0
notas = range(1,10)
cantidad_notas = 0

while cantidad_notas < 10:
    nota = int(input("Ingrese la nota de 1 a 10: "))
    cantidad_notas += 1
    if nota >= 7:
        notas_mayores_iguales_7 += 1
    else:
        if notas_menores_7 <= 10:
            notas_menores_7 += 1

print("La cantidad de notas mayores o iguales a 7 son: ", notas_mayores_iguales_7)
print("La cantidad de notas menores a 7 son: ", notas_menores_7)

