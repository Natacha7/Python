'''
CONDICIONAL DOBLE
Diseñar un algoritmo que imprima el nonbre del artículo, código, precio y precio con
descuento.
Si el artpiculo tiene código 01 el descuento es del 10%, si el código es 02 el descuento es 
del 20% (solo existen dos artpiculos)

ALGORITMO
inicio
   precio, precio_desc: Real
   Leer nomb_articulo, codigo, precio
  Si codigo = 01 entonces
     precio_desc = precio - precio*0.10
  sino
     precio_desc = precio - precio*0.20
   fin si
   imprimir nom_articulo, codigo,
      precio, precio_desc
fin
'''
print('\n')
cod_articulo = input("Digite el código del artículo ")
nom_articulo = input("Digite el nombre del artículo ")
precio = float(input("Digite el precio del artículo "))

if cod_articulo == "01":
    precio_desc = precio-precio*0.10
else:
    precio_desc = precio-precio*0.20
print('\n')
print("codigo articulo: ", cod_articulo)
print("nombre articulo: ", nom_articulo)
print("precio articulo: ", precio )
print("precio articulo con descuento: ", precio_desc)
print('\n')


