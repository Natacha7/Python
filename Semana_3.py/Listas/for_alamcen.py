'''
Un almacén desea saber el total de ventas por mes durante el primer trimestre del año, además desea conocer el promedio de ventas alcanzado durante este periodo de tiempo.
Se debe procesar n cantidad de facturas del periodo antes señalado, con la siguiente información:
1.	Mes factura
2.	Valor factura

Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
3.	Mes_factura: Puede ser de enero, febrero o marzo
4.	valor_factura: int

Ejemplo Datos
datos: list = [
    {
        "mes_factura": "enero",
        "valor_factura": 1200000
    },
    {
        "mes_factura ": "febrero",
        "valor_factura ": 3000000
    },
    {
        "mes_factura ": "enero",
        "valor_factura ": 10000000
    },
    
]
La respuesta debe retornar un diccionario con la siguiente información:
a.	Total - Ventas de enero
b.	Total - Ventas de febrero
c.	Total - Ventas de marzo
d.	Promedio de ventas en el trimestre
'''
def ventas_mes(datos: list) -> dict:
    Total_ventas_enero = 0
    Total_ventas_febrero = 0
    Total_ventas_marzo = 0
    Total_ventas = 0
    promedio = 0
    numero_ventas = 0
    enero = 0
    febrero = 0
    marzo = 0
   
    for item in datos:
        Total_ventas += item['valor_factura']
        if item['mes_factura'] == "enero":
            Total_ventas_enero += item['valor_factura']
            enero += 1
        elif item['mes_factura'] == "febrero":
            Total_ventas_febrero += item['valor_factura']
            febrero += 1
        elif item['mes_factura'] == "marzo":
            Total_ventas_marzo += item['valor_factura']
            marzo += 1
    numero_ventas = enero + febrero + marzo
    promedio = round((Total_ventas / numero_ventas), 2)

    resultado: dict = {
        "Total_ventas_enero": Total_ventas_enero,
        "Total_ventas_febrero": Total_ventas_febrero,
        "Total_ventas_marzo": Total_ventas_marzo,
        "Total_ventas_trimestre": Total_ventas,
        "Numero_ventas_trimestre": numero_ventas,
        "El_promedio_trimestre": promedio
    }
    return resultado

datos: list = [
    {
        "mes_factura": "enero",
        "valor_factura": 120000
    },
    {
        "mes_factura": "febrero",
        "valor_factura": 100000
    },
    {
        "mes_factura": "marzo",
        "valor_factura": 50000
    },
    {
        "mes_factura": "enero",
        "valor_factura": 130000
    }
]

print(ventas_mes(datos))



