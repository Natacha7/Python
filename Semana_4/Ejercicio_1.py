'''
problema # 1
Utilizar la funcion incorporada map() para crear una función que retorne una lista con la longitud de cada palabra (separadas por espacios)
de una frase. La función recibe una cadena de texto y retornará una lista
'''
def long_palabras(Python):
    palabra_len = list(map(len,'Python'.split()))
    return palabra_len

print(long_palabras('Python'))

print("------------------------------------")

nombres = ['Carolina', 'Juan', 'Sofia', 'Camilo']

longitud = list(map (len, nombres))
print ( longitud)