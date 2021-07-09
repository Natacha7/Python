'''
Elabora un algoritmo que permita ingresar el monto de la venta alcanzada por un vendedor durante un mes, 
se debe calcular la bonificación (%) que tiene derecho de acuerdo a la siguiente tabla:
VENTA REALIZADA EN EL MES ($)	BONIFICACION (%)
0 – 1.000.000	0
1.000.100 – 2.500.000	4
                       2.500.100 a más	8
	
Imprimir Venta realizada en el mes y la bonificación obtenida.
'''
Venta_vendedor = int(input("Digite el valor de la venta alcanzada por el vendedor: "))

if Venta_vendedor <= 1000000:
    Bonificacion= int(Venta_vendedor*0)
else:
    if (Venta_vendedor>=1000100) and (Venta_vendedor<= 2500000):
        Bonificacion= int(Venta_vendedor*0.04)
    else:
        if (Venta_vendedor>=2500100):
            Bonificacion = int(Venta_vendedor*0.08)

print("La venta realizada en el mes es: ", Venta_vendedor)
print("La bonificación obtenida es: ", Bonificacion)


