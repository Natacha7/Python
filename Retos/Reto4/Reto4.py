import locale
from statistics import mean

def promedio(a,b,c):
    return round(mean([a,b,c]))

metaVenta = 500000000
vendedores = ['Mario Correa', 'Martha Ramírez', 'Sandra Peña', 'Hugo López']
ventasEnero = [200000000, 300000000, 500000000, 100000000]
ventasFebrero = [120000000, 450000000, 600000000, 800000000]
ventasMarzo = [350000000, 300000000, 500000000, 700000000]

promedioVentasCarros = list(map(promedio, ventasEnero, ventasFebrero, ventasMarzo))
promedio_Trimestre = mean(promedioVentasCarros)

def imprimir_resultados() -> str:
    for x in range(0, len(vendedores)):
        print("\nVendedor: {}".format(vendedores[x]))
        print("\n{} {:,}".format('Ventas Enero :'.ljust(14), ventasEnero[x]))
        print("{} {:,}".format('Ventas Febrero :'.ljust(14), ventasFebrero[x]))
        print("{} {:,}".format('Ventas Marzo :'.ljust(14), ventasMarzo[x]))
        print("{} {:,}".format('Promedio Ventas Trimestre :'.ljust(
            14), promedioVentasCarros[x]))
        print("Meta: {}".format(
            'Se alcanzó la meta del promedio de ventas en el Trimestre' if promedioVentasCarros[x] > metaVenta 
            else 'No se alcanzó la meta del promedio de ventas en el Trimestre'))

        print("\n{}".format(''.ljust(54, '=')))

imprimir_resultados()

