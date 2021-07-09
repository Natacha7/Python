'''
Diseñe una calculadora que sume, reste, multiplique y divida, la cual le pida al usuario
mediante input el valor del primer número, el valor del segundo número y la operación a
realizar, hay que tener en cuenta la validación de los valores de entrada, por ejemplo:
Si el programa pide el primer valor, y el usuario ingresa una letra, combinaciones de
números y letras o caracteres no numéricos se debe mostrar un mensaje mediante otro input
requiriendo que ingrese nuevamente el numero e indicándole al usuario que el carácter
ingresado debe ser numérico.
En el caso que uno de los valores ingresados sea 0 y el usuario ingrese la opción de
División, debe imprimir un mensaje donde se indique que no se pude dividir entre cero o
que el cero no puede ser dividido.
'''
def es_numerico(numero1,numero2):
    if numero1 == str or numero2 == str:
        return False
    return True
numero1 = float(input("Digite el número 1: "))
numero2 = float(input("Digite el número 2: "))
operacion_realizar = input("Digite la operación que desea realizar: ")
numerico = es_numerico(numero1,numero2)
if numerico == True and operacion_realizar == "suma":
    suma = int(numero1) + int(numero2)
    print("La suma de los dos números es: ", suma)
elif numerico == True and operacion_realizar == "resta":
    resta = int(numero1) - int(numero2)
    print("La resta es: ", resta)
elif numerico == True and operacion_realizar == "multiplicacion":
    multiplicacion = int(numero1) * int(numero2)
    print("La multiplicación es: ", multiplicacion)
elif numerico == True and operacion_realizar == "division" and numero2 == 0 or numero1 == 0:
    print("No se puede dividir entre cero o el cero no puede ser dividido")
elif numerico == True and operacion_realizar == "division" and numero1 != 0 and numero2 != 0:
     division = int(numero1)/int(numero2)
     print("La división es: ", division)
else:
    print("Digite un número")





