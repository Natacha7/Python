# Función que realiza la suma de dos números

def sumar(a, b):
   s = a + b
   return s

def resta(a, b):
    r = a - b
    return r

def multiplica(a, b):
    m= a * b
    return m

def division(a, b):
    d= a / b
    return d

# Aquí inicia la aplicación

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segunfo numero: "))

suma = sumar(numero1, numero2)
restar = resta(numero1, numero2)
multiplicar = multiplica(numero1, numero2)
dividir = division(numero1, numero2)

print("a + b =" , suma)
print("a - b=", restar)
print("a * b=", multiplicar)
print("a / b=", dividir)





