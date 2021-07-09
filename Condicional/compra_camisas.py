'''
Permita calcular el total a pagar por la compra de N camisas. Si se compran entre 1 a 4 camisas 
se aplica un descuento del 12.5%, si se compra una cantidad comprendida entre 5 y 8 camisas 
se aplica un descuento del 20% y si se compran cantidades mayores, se aplica un descuento del 31.5% 
sobre el total de la compra. Debe imprimirse en pantalla la compra final sin descuento, monto del descuento 
y la compra con descuento.
'''
def Descuento(A_pagar,N_camisas):
        
    if (N_camisas>=1) and (N_camisas<=4):
        Descuento = int(A_pagar*0.125)
    elif (N_camisas>=5) and (N_camisas<9):
        Descuento = int(A_pagar*0.20)
    elif (N_camisas>=9):
        Descuento = int(A_pagar*0.315)
    return Descuento

N_camisas=int(input("Diga el número de camisas a comprar: "))
A_pagar=int(input("Diga la compra final sin descuento: "))

x = Descuento(A_pagar,N_camisas)
y = A_pagar - x
print("La compra final sin descuento es de: ", A_pagar)
print("El monto del descuento es: ",x)
print("La compra con descuento es de: ",y)










    






