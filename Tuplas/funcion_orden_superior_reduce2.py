#Concatenar todos los elementos de la lista
from functools import reduce
lista=['Python', 'Java', 'Ruby', 'Elixir' ]
resultado = reduce(lambda acumulador= ' ', elemento = ' ': acumulador+' - '+elemento, lista)
print(resultado)
