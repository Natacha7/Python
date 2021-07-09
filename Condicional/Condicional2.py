'''
Condicional doble

Estructura algoritmica de la condicional doble
si <condicion> entonces
      Acción (es)
sino
      Acción (es)
fin - si

Determinar si un alumno aprueba o reprueba una asignatura aprueba si el promedio de tres
calificaicones es mayor o igual a 3, en caso contrario reprueba.

'''
calificacion1 = float(input("Digite calificacion 1: "))
calificacion2 = float(input("Digite calificacion 2: "))
calificacion3 = float(input("Digite calificacion 3: "))

promedio = (calificacion1+calificacion2+calificacion3)/3

if promedio >= 3:
     print("El alumno aprobó")
else:
     print("El alumno reprobó")

