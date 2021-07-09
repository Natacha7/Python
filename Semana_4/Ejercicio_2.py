'''
problema #2
Crear una función que tome una lista de digitos y devuelva al número que corresponden. Por ejemplo [1,2,3] corresponde al número (123).
Utilizar la función reduce
'''

from functools import reduce
lista = [1,3,5,7]
def lista_digitos(digitos):
    return reduce(lambda x,y:x*10+y,digitos)

print(lista_digitos(lista))

lista = ['1','2','3']
cadena = ''.join(lista)
print(cadena)

