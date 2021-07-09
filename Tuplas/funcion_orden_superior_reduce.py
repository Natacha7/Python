# FUNCIONES
'''
FUNCION REDUCE
Usaremos la función reduce cuando poseamos una colección de elementos 
y necesitemos generar un único resultado.

Reduce nos permitirá reducir los elementos de la colección.

Podemos ver a esta función como un acumulado
'''

# reduce( funcion a aplicar, objeto iterable)
'''
===================================================================================
Aquí lo importante es detallar la función a aplicar. Esta función debe poseer,
obligatoriamente, dos parámetros.

El primer parámetro hará referencia al acumulador, un variable que irá
modificando su valor por cada uno de los elementos en la colección.

Por otro lado, el segundo parámetro hará referencia a cada elemento de la
colección. La función debe retornar un nuevo valor, será este nuevo valor el
que será asignado al acumulador.
===============================================================================
'''
from functools import reduce
lista = [1,2,3,4]

def funcion_acumulador(acumulador=0, elemento=0):
    return acumulador+elemento

resultado = reduce(funcion_acumulador, lista)
print(resultado)
