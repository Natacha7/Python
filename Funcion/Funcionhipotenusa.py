import math # import el Módulo Matemática de Phyton

#Función que calcula la Hipotenusa

def calcularHipotenusa(a, b):
    hipotenusa = math.sqrt((a*a) + (b*b))
    return hipotenusa

# Aquí inicia el programa

a = int(input("Digite el valor del cateto a: "))
b = int(input("Digite el valor del cateto b: "))

# Llamar la función

h = calcularHipotenusa(a, b)
print("El valor de la hipotenusa es:" , h)
