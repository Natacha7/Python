'''
En una tienda de descuento se efectúa una promoción en la cual se hace un descuento sobre el valor de
la compra total según el color de la bolita que el cliente saque al pagar en caja. }
Si la bolita es de color blanco no se hará descuento, si es verde se le hará un descuento del 10 %, 
si es amarilla un 25 %, si es azul un 50% y si es roja un 100%. Escriba el valor total que el cliente 
debe pagar por su compra.
'''
Total_compra = int(input("Digite el valor de la compra total: "))
Color_bolita = str(input("Digite el color de la bolita que saco al pagar en caja: "))

if Color_bolita == ('blanco'):
    Valor_pagar= Total_compra-Total_compra*0
else:
    if Color_bolita == 'verde':
        Valor_pagar= int(Total_compra-Total_compra*0.10)
    else:
        if Color_bolita == 'amarilla':
            Valor_pagar= int(Total_compra-Total_compra*0.25)
        else:
            if Color_bolita == 'azul':
                Valor_pagar= int(Total_compra-Total_compra*0.50)
            else:
                if Color_bolita == 'rojo':
                    Valor_pagar= int(Total_compra-Total_compra*1)

print("El valor total a pagar es: ", Valor_pagar)





