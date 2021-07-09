'''
FUNCIONES PARA COLECCIONES DE DATOS
Python Ofrece unas funciones , muy versatiles para trabajar con grandes 
colecciones de datos, estas son funciones de orden superior.

Las funciones más utilizadas de este tipo, para realizar operaciones sobre
listas principalmente, sin utilizar ciclos, al estilo del paradigma funcional,
son las siguientes:

* Map
* Reduce
* Filter
* Zip
--------------------------------------------------------------------------
Algo interesante de las funciones en Python es que estas pueden ser
asignadas a variables.

Las funciones pueden ser utilizadas como argumento de otras funciones

Las funciones pueden retornar otras funciones.
---------------------------------------------------------------------------
'''
#funciones de orden superior
def suma(val1, val2):
    return (val1+val2)

def resta(val1, val2):
    return (val1-val2)

def multiplicacion(val1, val2):
    return (val1*val2)

def division(val1, val2):
    return (val1/val2)

#esta es la función de orden superior
def operacion(funcion, val1, val2):
    return (funcion(val1,val2))

variable_suma = suma
variable_resta = resta
variable_multiplicacion = multiplicacion
variable_division = division

resultado = operacion(variable_suma, 10, 5)
resultado2 = operacion(variable_resta, 10,5)
resultado3= operacion(variable_multiplicacion, 10, 5)
resultado4 = operacion(variable_division, 10, 5)

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)

