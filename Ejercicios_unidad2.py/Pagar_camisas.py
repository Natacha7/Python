'''
Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%
'''
Valor_camisas = float(input("Digite el valor de cada camisa $ "))
Total_camisas = int(input("Digite el número de camisas que compro: "))

if Total_camisas >= 3:
    Descuento_20 = float((Valor_camisas*Total_camisas)*0.2)
    Total_pagar_3 = float((Valor_camisas*Total_camisas) - Descuento_20)
    print("El total a pagar por la compra de las camisas ${:,.0f}".format(Total_pagar_3))
else:
    Descuento = float((Valor_camisas*Total_camisas)*0.1)
    Total_pagar = float((Valor_camisas*Total_camisas) - Descuento)
    print("El total a pagar por la compra de las camisas ${:,.0f}".format(Total_pagar))
