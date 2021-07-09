'''
s1 = set([1, 2, 3, 4])
s2 = set(range(10))
print(s1)
print(s2)

c = {1, 3, 2, 9, 3, 1}
print(c)

a = set('Hola Pythonista')
print(a)

unicos = set([3, 5, 6, 1, 5])
print(unicos)

mi_conjunto = {1, 3, 2, 9, 3, 1}
print(mi_conjunto)
for numero in mi_conjunto:
    print(numero)

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(set_mutable1)
set_mutable1.add(22.000001)
print(set_mutable1)
set_mutable1.clear()
print(set_mutable1)

set_mutable = set([4.0, 'Carro', True])
otro_set_mutable = set_mutable.copy()
set_mutable == otro_set_mutable
print(otro_set_mutable)
'''
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.difference(set_mutable2))
print(set_mutable2.difference(set_mutable1))