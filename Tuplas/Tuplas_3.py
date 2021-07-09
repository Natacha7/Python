'''
#count() recibe un elemento como argumento y cuenta la cantidad de veces que aparece en la tupla
valores = ("uva",True,"avion",10, "uva")
print("la palabra uva aparece en la tupla : ", valores.count('uva'))


#acceso a los elementos usando un indice negativo
frutas= ('uva', 'lulo', 'naranja', 'mango')
print(frutas [-1]) #mango

'''
#acceso a un subconjunto de elementos
vocales = 'a','e','i','o','u'
print(vocales [2:3]) #elementos desde el indice 2 hasta el indice 3-1 (i)
print(vocales [2:4]) #elementos desde el indice 2 hasta el indice 4-1 (i-o)
print(vocales[:]) # todos los elementos
