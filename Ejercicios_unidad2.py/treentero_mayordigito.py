'''
leer tres números enteros de dos digitos cada uno y determinar en cuál de ellos se encuentra el 
mayor digito
'''
s = input("Digite un número entero de dos digitos: ")
q = input("Digite un número entero de dos digitos: ")
r = input("Digite un número entero de dos digitos: ")

lista = (int(s[0]), int(s[1]), int(q[0]), int(q[1]), int(r[0]), int(r[1]))

maximo= max(lista)
print("El mayor digito es: ", maximo)


