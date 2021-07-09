'''
Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y
5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó
o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro
del rango permitido.
'''
nota = 0
suma_notas = 0
cantidad_notas= 0
promedio_notas = 0

while nota >= 0 and cantidad_notas < 3:
    nota = float(input("digite el valor de la nota: "))
    if (nota>= 0) and (nota <= 5):
        cantidad_notas += 1
        suma_notas = suma_notas + nota
        promedio_notas = round((suma_notas/cantidad_notas),2)

if promedio_notas > 3:
    print("El promedio del estudiante es: ", promedio_notas, "el estudiante aprobó")
else:
    print("El promedio del estudiante es: ", promedio_notas, "el estudiante no aprobó")
   

    


