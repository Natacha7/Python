'''
Tal como su nombre indica filter significa filtrar, y es una de mis 
funciones favoritas, ya que a partir de una lista o iterador y una 
función condicional, es capaz de devolver una nueva colección con 
los elementos filtrados que cumplan la condición.
'''

"""
Desarrolle un programa que reciba como parámetro una lista
de peliculas y un caracter.
Retorne una nueva lista con las películas que empiezan con 
el caracter que recibe como parámetro
"""
peliculas = ['Mivillano favorito', 'El castigador', 'El principe de Persia', 'El paseo 5', 'Busquedad implacable']

def nombre_letra(l):
    return 'E' == l[0] 

filtro_nombres = filter(nombre_letra, peliculas)

print(list(filtro_nombres))
