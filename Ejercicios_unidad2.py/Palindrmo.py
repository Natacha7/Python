'''
Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es
palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor
a roma”.
'''

def es_palindromo(frase):
    #pasa todas las letras a minuscula
    frase = frase.lower()
    #quita los espacios de la frase
    frase = frase.replace(' ', '')
    longitud = len(frase)
    if longitud % 2 == 0:
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2:]
    else:
        izquierda = frase[:longitud//2]
        derecha = frase[longitud // 2+1:]
    return izquierda == derecha[::-1]

print(es_palindromo('Roma Amor'))


