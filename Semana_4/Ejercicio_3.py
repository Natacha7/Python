'''
Problema # 3
Crear una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Utilizar la función filter
'''
Series = ['Friends', 'The walking dead', 'La casa de papel', 'Game of trones', 'Tres chiflados']

def serie_letra(letra):
    return 'T' == letra[0] 

filtro_series = filter(serie_letra, Series)

print(list(filtro_series))

print("-----------------------------------------")

def palabras_filtro(lista_palabras,letra):
        return list(filter(lambda word:word[0]==letra,lista_palabras))
print(palabras_filtro(['Gato','Ganzo','Cocodrilo','Perro','Gusano', 'Conejo'], 'G'))