'''
mi_diccionario = { (x, x**3) : [ y**2 for y in range(4,31,2) if y%x == 0 ] for x in range(3, 11) }
print(mi_diccionario)
mi_lista = [x**2 for x in range(4, 31, 2) if x%3 == 0]
print(mi_lista)

print( [x for x in range(4, 31, 2)] )
print( [x**2 for x in range(4, 31, 2) if x%3 == 0] )

def dijkstra(unvisited: set, distances: dict, neighbours: dict, start: str) -> tuple:

    # Let distance of start vertex from start = 0. Let distance of all other vertices = infinity.
    known = { vertex: 0 if vertex == start else float('inf') for vertex in unvisited }

    # Let the previous node be unknown(none) for every vertex
    previous = {vertex: None for vertex in unvisited}

    # Repeat until there are no vertices left to visit
    while len(unvisited) > 0:

        # Visit the unvisited vertex with the smallest known distance from the start vertex
        distance, visit = min( [ (known[candidate], candidate) for candidate in unvisited] )
        # For the current vertex, calculate the distance from the visited vertex to each of its neighbours
        calculated = {neighbour: distance + distances[visit, neighbour] for neighbour in neighbours[visit]}

        # Update previous and known distances if the calculated distance is less than the known distance.
        previous.update( {vertex: visit if calculated[vertex] < known[vertex] else previous[vertex] for vertex in neighbours[visit]} )
        known.update( {vertex: calculated[vertex] if calculated[vertex] < known[vertex] else known[vertex] for vertex in neighbours[visit] })

        # Remove the current vertex (visited) from the unvisited set.
        unvisited.remove(visit)

    # Return the best known distances and their corresponing previous nodes
    return known, previous
unvisited = {'A', 'B', 'C', 'D', 'E', 'C'}

distances = {('A', 'B'): 6, ('A', 'D'): 1, ('B', 'C'): 5, ('B', 'D'): 2, ('B', 'E'):2, ('D', 'E'): 1, ('E','C'): 5,
             ('B', 'A'): 6, ('D', 'A'): 1, ('C', 'B'): 5, ('D', 'B'): 2, ('E', 'B'):2, ('E', 'D'): 1, ('C','E'): 5}

neighbours = {
                'A': ['B', 'D'],
                'B': ['A', 'D', 'C'],
                'C': ['B', 'E'],
                'D': ['A', 'B', 'E'],
                'E': ['D', 'B', 'C']
              }

minimas, predecesores = dijkstra(unvisited, distances, neighbours, 'A')
minimas, predecesores = sorted(minimas.items()), sorted(predecesores.items())
print('Distancias minimas: \n {} \nPredecesores: \n {}'.format(minimas, predecesores))

cadena = 'hola'
lista = list(cadena)
print(lista)

cad = "hola"
cad2 = "adios"
num = 15
tupla1 = tuple(cad)
tuplaGeneral = (tupla1, num, tuple(cad2))
print(tuplaGeneral)

cadena = "hhola"
print(set(cadena))

lista = ['1','2','3']
cadena = ''.join(lista)
print(cadena)

lista = ['h', 'o', 'l', 'a', 123]
tupla = tuple(lista)
print(tupla)

lista = ['h','o','o','l','a',1,1,2]
conjunto=set(lista)
print(conjunto)

tupla =('h','o','l','a')
cadena= ''.join(tupla)
print(cadena)

tupla =('hola',111,'mundo')
lista=list(tupla)
print(lista)

tupla = ('hola', 111, 'mundo', 'hola')
conjunto = set(tupla)
conjunto.add('15')
print(conjunto)

conjunto = {'h', 'o', 'l', 'a'}
cadena =''.join(conjunto)
print(cadena)

conjunto = {'h','o','l','a'}
tupla =tuple(conjunto)
print(tupla)
lista = (list(conjunto))
print(lista)

cadena = 'hola'
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)

lista = ['h','o','l','a']
diccionario = dict(zip(range(len(lista)),lista))
print(diccionario)

tupla = ('h','o','l','a')
diccionario = dict(zip(range(len(tupla)),tupla))
print(diccionario)

conjunto = {'h','o','l','a'}
diccionario = dict(zip(range(len(conjunto)),conjunto))
print(diccionario)

diccionario = {0:'h', 1:'o', 2:'l', 3:'a'}
cadenaValores = "".join(diccionario.values())
print(cadenaValores)

diccionario = {0:'h', 1:'o', 2:'l', 3:'a'}
tuplaLlaves = tuple(diccionario.keys())
tuplaValores = tuple(diccionario.values())
tuplaItems = tuple(diccionario.items())
print(tuplaLlaves)
print(tuplaValores)
print(tuplaItems)

diccionario = {0:'h', 1:'o', 2:'l', 3:'a'}
listaLlaves = list(diccionario.keys())
listaValores = list(diccionario.values())
listaItems = list(diccionario.items())
print(listaLlaves)
print(listaValores)
print(listaItems)
'''
diccionario = {0:'h', 1:'o', 2:'l', 3:'a', 4:'a'}
conjuntoLlaves = set(diccionario.keys())
conjuntoValores = set(diccionario.values())
conjuntoItems = set(diccionario.items())
print(conjuntoLlaves)
print(conjuntoValores)
print(conjuntoItems)
