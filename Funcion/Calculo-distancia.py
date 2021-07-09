'''
Se desea calcular la distancia m recorrida por un móvil
que tiene velocidad constante (m/s) durante un tiempo T (sg)
considerar un movimiento rectilineao uniforma MRU
'''

#Calcula la distancia recorrida

def distancia(v, t):
   d = v * t
   return d


v = int(input("Digite la velocidad: "))
t = int(input("Digite el tiempo: "))

distancia = distancia(v,t)

print("v * t=", distancia)