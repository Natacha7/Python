'''
Para ingresar al curso de Producción Cinematográfica se realizó una prueba clasificatoria. Se tienen los 
resultados de dicho examen por aspirante (una nota comprendida entre 0.0 y 5.0.
Se desea saber cuántos aspirantes aprobaron el examen, cuántos lo perdieron (nota menor que 3 0 y cuál 
fue el promedio de todo el grupo de aspirantes No sabemos cuántos aspirantes son, pero
sabemos que cuando se quiera indicar que se finalizó el ingreso de notas se digitará un valor negativo.
'''

nota = 0
suma = 0
aprobaron = 0
perdieron = 0

while nota>= 0:
    nota = float(input("digite el valor de la nota: "))
    if (nota>= 0) and (nota <= 5):
        if nota >= 3:
            aprobaron = aprobaron+1
        else:
            perdieron = perdieron+1
    suma = suma + nota

total_aspirantes =aprobaron + perdieron

def promedio_suma(n):
    promedio_notas = round(suma/(total_aspirantes),2)
    return promedio_notas

#respuesta

print(" El total de estudiantes que aprobaron el examen es de: ", aprobaron, " El total de estudiantes que perdieron el examen es de: ", perdieron, "El promedio del total de las notas es de: ",promedio_suma(nota))

