def consolidar_ventas(datos: list) -> dict:
    
    ventas_credito: str = "credito"
    ventas_contado: str = "contado"
    total_ventas = 0 
    total_ventas_credito = 0
    total_ventas_contado = 0

    for item in datos:
        total_ventas += item['total_factura']
        if item['tipo_venta'] == ventas_contado:
            total_ventas_contado +=  item['total_factura']
        elif item['tipo_venta'] == ventas_credito:
            total_ventas_credito +=  item['total_factura']
    resultado: dict = {
        "total_ventas": total_ventas,
        "total_ventas_contado": total_ventas_contado,
        "total_ventas_credito": total_ventas_credito

            }
    return resultado

datos: list = [

    {
        "tipo_venta": "credito",
        "total_factura": 85000
    },
    {
        "tipo_venta": "contado",
        "total_factura": 100000
    },
    {
        "tipo_venta": "credito",
        "total_factura": 20000
    },
    {
        "tipo_venta": "contado",
        "total_factura": 30000
    },
    {
        "tipo_venta": "credito",
        "total_factura": 1000000
    },
    {
        "tipo_venta": "contado",
        "total_factura": 300000
    },
    {
        "tipo_venta": "contado",
        "total_factura": 10000
    }   
]