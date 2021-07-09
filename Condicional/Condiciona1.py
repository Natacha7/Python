'''
Para escribir programas Útiles, casi siempre necesitamos la capacidad de comprobar
ciertas condiciones y cambiar el comportamiento del programa. 
Las sentencias condicionales nos dan esta capacidad. La forma más
sencilla es la sentencia if
'''

'''
Algoritmo que pide un color, si se digita el color 
rojo en minúscula, imprime en pantalla “Tiene buen gusto !”,
 si no, simplemente imprime “Le gusta el color” y el nombre 
 del color digitado:
Inicio
     LEER color
     Si color==“rojo”
         IMPRIMIR “Tiene Buen gusto!”
     Fin Si
     IMPRIMIR “Le gusta el color:  ”, color
Fin
'''
color = input("Digite el color: ")

if color == "rojo":
    print("tiene buen gusto!")

print("Le gusta el color:", color)


