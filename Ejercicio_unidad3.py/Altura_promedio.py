'''
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio
de las personas.
'''
n=int(input("Digite el valor de n: "))
altura = 0
promedio = 0
suma_alturas = 0
conteo_alturas = 0
while conteo_alturas < n:
    altura= int(input("Digite la altura: "))
    conteo_alturas += 1
    suma_alturas = altura + suma_alturas
    promedio = round(suma_alturas/ conteo_alturas,2)

print("La altura promedio de las personas es: ", promedio)
