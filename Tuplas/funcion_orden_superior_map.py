'''
La funcion map nos permite aplicar una funcion 
sobre cada uno de los elementos de
una coleccion (listas, tuplas, etc ...).

Haremos uso de esta funcion siempre que
tengamos la necesidad de transformar el 
valor de cada elemento en otro.


'''

def doblar(numero):
    return numero * 2

numeros = [2,5,10,23,50,33]

resultado = list(map(doblar, numeros))

print(resultado)

def cuadrado(elemento=0):
    return elemento * elemento
lista = [1,2,3,4,5,6,7,8,9,10]
resultado=list(map(cuadrado,lista))
print(resultado)