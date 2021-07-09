#Leer dos número y decir si son iguales o no

def son_iguales(a, b):
    if (a == b):
        return("son iguales")
    else:
        return("son diferentes")

a = int(input("Digite Numero1: "))
b = int(input("Digite Numero2: "))

respuesta = son_iguales(a, b)
print("Los números son: ", respuesta)



