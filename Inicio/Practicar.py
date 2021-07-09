'''
var1 = 10
var2 = 30
var3 = 120
var4 = 500

maximo= max(var1, var2, var3, var4)
print(maximo)

minimo= min(var1, var2, var3, var4)
print(minimo)

x = range(5)
print(x)



def repetir_funciones():
    imprime_cosas()
    imprime_cosas()

def imprime_cosas():
    print("La clase esta genial")
    print('Python es lo máximo')

repetir_funciones()

def consultar_nombre_genero(letra_genero): pass
type(consultar_nombre_genero)
consultar_nombre_genero("M")

def otra_suma(numero1, numero2):
    print(numero1 + numero2)
    print("\n")
    return numero1 + numero2

resultado = otra_suma(5,6)
print(resultado)

def mi_funcion(nombre , apellido):
    nombre_completo = nombre + apellido
    print(nombre_completo)

mi_funcion('David' , 'Alvarez')

def saludar1(nombre, mensaje='Hola'):
    print(mensaje, nombre)

saludar1('Pepe Grillo')

def saludar(nombre, mensaje="Hola"):
    print(mensaje, nombre)

saludar(mensaje="Buen día", nombre="Juancho")

var1 = 1.20
print(var1)

var1 = int(var1)
print(var1)

print('\n')
var1 = 120
var2 = var1
print(var2)
print('\n')

var1 = 120
var2 = 200
print(var1)
print(var2)

var1 = var2 = var3 = 200
print('\n')

numero1 = 2
numero2 = 3
numero3 = numero1 ** numero2
print(numero3)
type(numero3)
print('\n')

x = 15 + 18
sqrt = x**(1/2)
print(sqrt)

y = 2*(3-1)
print(y)

w = (1+1)**(5-2)
print(w)

q = 2**1+1
print(q)

r = 3*1**3
print(r)

k = 2*3-1
print(k)

l = 6+4/2
print(l)

g = 43
g = g+1
print(g)

print('\n')

var1 = 10
var2 = 4
var3 = 5.5
var4 = 67

promedio = (var1 + var2 + var3 + var4)/4
print(promedio)
print(("El promedio de esos numeros es: ")+str(promedio))
'''
cadena = "Este es un atributo"
nuevaCadena = cadena + "nuevo"
print("Flujo: ", nuevaCadena)
print(nuevaCadena[0:4])














