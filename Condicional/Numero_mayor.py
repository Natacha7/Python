#Condicional doble, dar dos números diferentes e indicar cuál es el mayor

def cual_es_mayor(a, b):
    if (a > b):
        return a
    else:
        return b

a = int(input("Digite Numero1: "))
b = int(input("Digite Numero2: "))

respuesta = cual_es_mayor(a, b)
print("El numero es mayor es: ", respuesta)
