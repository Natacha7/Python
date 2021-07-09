'''
Una empresa recibe la información correspondiente a las ventas en pesos Colombianos de cada vendedor en el primer trimestre del año, se desea conocer el promedio de ventas en el trimestre por cada vendedor y el promedio general de ventas en el mismo periodo 

Vendedor	       Enero ($)	Febrero ($)	 Marzo ($)
Pedro López 	    2000000  	1000000	     5000000
Martha Jaramillo	1500000	    10000000	  600000
Sandra Peña     	500000	    800000       3000000
Hugo Marín      	400000  	200000  	 100000

Imprimir por pantalla la información de la siguiente manera:

Vendedor: Pedro López
Ventas Enero: $ 0000000
Ventas Febrero: $ 0000000
Ventas Marzo: $ 0000000
Promedio de ventas en el trimestre $ 0000000
============================================
Vendedor: Martha Jaramillo
Ventas Enero: $ 0000000
Ventas Febrero: $ 0000000
Ventas Marzo: $ 0000000
Promedio de ventas en el trimestre $ 0000000
============================================
'''
import locale
from statistics import mean

def promedio(a,b,c):
    return round(mean([a,b,c]),1)

vendedores = ['Pedro López', 'Martha Jaramillo', 'Sandra Peña', 'Hugo Marín']

promedio_ventas_Enero = [2000000, 1500000, 500000, 400000]
promedio_ventas_Febrero = [1000000, 10000000, 800000, 200000]
promedio_ventas_Marzo = [5000000, 600000, 3000000, 100000]

promedioVentasTrimestre = list(map(promedio, promedio_ventas_Enero, promedio_ventas_Febrero, promedio_ventas_Marzo))
promedio_general_ventas = mean(promedioVentasTrimestre)

for x in range(0, len(vendedores)):
    print("\n vendedor: {}".format(vendedores[x]))
    print("\n{} {:,.0f}".format('Ventas Enero $'.ljust(14), promedio_ventas_Enero[x]))
    print("{} {:,.0f}".format('Ventas Febrero $ '.ljust(14), promedio_ventas_Febrero[x]))
    print("{} {:,.0f}".format('Ventas Marzo $ '.ljust(14), promedio_ventas_Marzo[x]))
    print("{} {:,.0f}".format('Promedio ventas en el trimestre $ '.ljust(14), promedioVentasTrimestre[x]))
    print("\n{}".format(' '.ljust(30, '=')))

print("\x1b[1;32m"+'Promedio de ventas primer trimestre', promedio_general_ventas)



