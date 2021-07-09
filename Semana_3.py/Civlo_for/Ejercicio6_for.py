'''
6. Crear un programa que reciba por teclado la edad de 10 personas e imprima por pantalla cuantos son mayores de edad y menores de edad hay en el grupo.
'''
Mayor_edad = 0
Menor_edad = 0

for i in range(10):
    Su_edad=int(input("Introduzca su edad: "))
    if Su_edad >= 18:
        Mayor_edad = Mayor_edad + 1
    elif Su_edad <= 17:
        Menor_edad = Menor_edad + 1

print("En el grupo hay: ", Mayor_edad, "mayores de edad y ", Menor_edad, "menores de edad")


