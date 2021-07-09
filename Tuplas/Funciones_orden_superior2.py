# Funciones de orden superior

'''
Creamos la función crear_funcion.

Esta función tiene la capacidad
de crear nuevas funciones a
partir del valor del parámetro.
'''
# Envoltura de funciones

def crear_funcion(operador):
    if operador =='+':
        def suma(valor1=0, valor2=0):
            return valor1 + valor2
        return suma
    elif operador == '-':
        def resta(valor1=0, valor2=0):
            return valor1 - valor2
        return resta
    elif operador == "*":
        def multiplicacion(valor1= 0, valor2=0):
            return valor1 * valor2
        return multiplicacion
    elif operador == "/":
        def division(valor1= 0, valor2=0):
            return valor1 / valor2
        return division

#Función de orden superior
def operacion(funcion, valor1=0, valor2=0):
    return funcion(valor1, valor2)

funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma, 30, 10)
funcion_resta = crear_funcion("-")
resultado1 = operacion(funcion_resta, 30, 10)
funcion_multiplicacion = crear_funcion("*")
resultado2 = operacion(funcion_multiplicacion, 30, 10)
funcion_division = crear_funcion("/")
resultado3 = operacion(funcion_division, 30, 10)

print(resultado, resultado1, resultado2, resultado3)

