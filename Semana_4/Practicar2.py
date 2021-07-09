'''
def suma(val1 = 0, val2 = 0):
    return val1 + val2

def operacion(funcion, val1=0, val2=0):
    return funcion(val1, val2)

funcion_suma= suma
resultado=operacion(funcion_suma,10,20)
print(resultado)

suma = lambda val1=0, val2=0: val1+val2
operacion = lambda operacion, val1=0, val2=0: operacion(val1,val2)

resultado = operacion(suma,10,20)
print(resultado)

from math import pow
pow(2,3)

numeros = [2,3,4]
potencias = [3,2,4]
potenciados=map(pow, numeros, potencias)
print(potenciados)

def mayor_a_cinco(elemento):
    return elemento > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado = tuple(filter(mayor_a_cinco, tupla))
resultado = len(resultado)
print(resultado)


pares = [ ]

for i in items:
    if i % 2 == 0:
        pares.append(i)

print(pares)

lista = [1,2,3,4]
acumulador = 0
for elemento in lista:
    acumulador += elemento

print(acumulador)

from functools import reduce
lista = ['Python', 'Java', 'Ruby', 'Elixir']
resultado = reduce(lambda acumulador = ' ', elemento = ' ': acumulador+"-"+elemento, lista) 
print(resultado)

from functools import reduce
suma10 = reduce(lambda x,y:x+y, items, 10)
print(suma10)

print(all([True, False, True]))
print(any([True, False, True]))
print(all([]))
print(any([]))

info = [int(input()),input().split(' ')]
print('True' if all (list(map(lambda x:x>0, list(map(int, info[1]))))) and any(list(map(lambda x:x[0]==x[1] or x[0] =='5'))), list(zip(info[1], list(map(lambda x:x[-1:(len(x)+1)*-1:-1], info[1])))) else 'False')

from numpy import random as r
print(r.choice(['Andres','Juan','Pedro', 'Mateo'], size= r.choice([1,2],p=[0.1,0.9]) , p=[0.5,0.2,0.2,0.1], replace=False))

import numpy as np
a = np.array([34, 25, 7])

from numpy import random as r
print(r.choice(['Andres','Juan','Pedro', 'Mateo'], size= r.choice([1,2],p=[0.1,0.9]) , p=[0.5,0.2,0.2,0.1], replace=False))

import numpy as np
a = np.array([34, 25, 7])
print(type(a)) 
print(a.shape)  
print(a[0], a[1], a[2])
a[0] = 5  
print(a) 

import numpy as np
b = np.array([[1,2,3],[4,5,6]]) 
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0]) 

import numpy as np
matriz = np.zeros((3,3))
print(matriz) 

b = np.ones((1,2)) 
print(b)

import numpy as np
c = np.full((2,2), 7)  # Crear una matriz constante
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Crear una matriz de identidad 2x2
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Crear una matriz llena de valores aleatorios
print(e)                     # Podría imprimir "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"

import numpy as np

# Crear la siguiente matriz de rango 2 con forma (3, 4)
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11 ]]
a = np.array([[1,2,3], [5,6,7], [9,10,11]])
print(a)

# Usar el rebanado para sacar el subconjunto que consiste en las 2 primeras filas
# y las columnas 1 y 2; b es el siguiente conjunto de forma (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)
print(np.fliplr(a))

# Una rebanada de una matriz es una vista en los mismos datos, por lo que modificarla
# modificará la matriz original.
print(a[0, 1])   # Prints "2"

b[0, 0] = 77     # b[0, 0] es la misma pieza de datos que a[0, 1]
print(a[0, 1])   # Prints "77"

import numpy as np

# Crear la siguiente matriz de rango 2 con forma (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

# Dos formas de acceder a los datos de la fila del medio de la matriz.
# Mezclando la indexación de enteros con rebanadas se obtiene una matriz de rango inferior,
# mientras que usando sólo rebanadas se obtiene un conjunto del mismo rango que el
# La matriz original:
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)
# Un ejemplo de indexación de arreglos enteros.
# La matriz devuelta tendrá forma (3,2) y
print(a.shape)
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
# El ejemplo anterior de indexación de arreglos enteros es equivalente a esto:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"
# Cuando se usa la indexación de arreglos enteros, se puede reutilizar el mismo
# elemento de la matriz de la fuente:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"
# Equivalente al ejemplo anterior de indexación de arreglos enteros
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"

import numpy as np

# Crear una nueva matriz de la cual seleccionaremos elementos
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print(a)  # prints "array([[ 1,  2,  3],
          #                [ 4,  5,  6],
          #                [ 7,  8,  9],
          #                [10, 11, 12]])"
          # Crear una serie de índices
b = np.array([0, 2, 0, 1])

# Selecciona un elemento de cada fila de a usando los índices de b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"
# Muta un elemento de cada fila de a usando los índices de b
a[np.arange(4), b] += 10

print(a)  # prints "array([[11,  2,  3],
          #                [ 4,  5, 16],
          #                [17,  8,  9],
          #                [10, 21, 12]])

import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)
bool_idx = (a > 2)  # Encuentra los elementos de a que son más grandes que 2; 
                    # esto devuelve un conjunto numérico de Booleans de la misma 
                    # forma que a, donde cada ranura de bool_idx dice
                    # si ese elemento de a es > 2.
print(bool_idx)      # Prints "[[False False]
                     #          [ True  True]
                     #          [ True  True]]"

# Usamos la indexación de arreglos booleanos para construir un arreglo de rango 1
# que consiste en los elementos de un correspondiente a los valores Verdaderos
# de bool_idx

print(a[bool_idx])  # Prints "[3 4 5 6]"
# Podemos hacer todo lo anterior en una sola declaración concisa:
print(a[a > 2])     # Prints "[3 4 5 6]"

import numpy as np

x = np.array([1, 2])   # Dejar que numpy elija el tipo de datos
print(x.dtype)         # Prints "int64"

import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x)
print(y)
# Suma de elementos; ambos producen la matriz
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))
# Diferencia de elementos (resta); ambos producen la matriz
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))
# Producto de elementos; ambos producen la matriz
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))
# División de elemetos; ambos producen la matriz
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Raíz cuadrada de elemtos; produce la matriz
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))
'''
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])
# Producto interno de los vectores; ambos producen 219
print(v.dot(w))
print(np.dot(v, w))