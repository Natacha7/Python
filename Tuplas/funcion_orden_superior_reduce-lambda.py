from functools import reduce

#Forma tradicional
valores = [2,4,6,5,4]
suma = 0
for el in valores:
    suma += el
print(suma)
#21

print('================================')

#Con reduce y lambda
valores = [2,4,6,5,4]
suma = reduce(lambda x,y: x+y, valores)
print(suma)
#21