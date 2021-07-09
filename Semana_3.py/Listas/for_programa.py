'''
EJERCICIOS 
En una Universidad existen tres programas académicos, que son: Licenciatura Matemáticas, Tecnología en Electrónica y Tecnología de Sistemas, los cuales tienen un costo de inscripción de $120.000 para Tecnología Electrónica, $150.000 para Matemáticas y $110.000 para Tecnología de Sistemas, Se desea conocer el numero de inscritos en cada programa y el total recaudado por concepto de inscripción en cada programa.
Se debe procesar n cantidad de inscritos con la siguiente información:
1.	Código del programa
2.	Valor Inscripción

Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
1.	cod_programa: “01 - Licenciatura Matemáticas” o “02 - Tecnología en Electrónica” o “03 - Tecnología de Sistemas”
2.	valor_inscripcion: int

EJEMPLO diccionario
datos: list = [
    {
        "cod_progrma": "01",
        "valor_inscripcion": 120000
    },
    {
        "cod_progrma": "02",
        "valor_inscripcion": 150000
    },
    {
        "cod_progrma": "03",
        "valor_inscripcion": 110000
    },
    
]
La respuesta debe retornar un diccionario con la siguiente información:
1.	Total inscriptos por programa
2.	Recaudo_total por programa
'''
def inscritos_programa(datos: list) -> dict:
    total_inscritos_electronica = 0
    total_inscritos_matematicas = 0
    total_inscritos_sistemas = 0
    recaudo_electronica = 0
    recaudo_matematicas = 0
    recaudo_sistemas = 0
    
    # Iterar los datos a procesar
    for item in datos:
        if item['cod_progrma'] == "01":

            # Total inscritos licenciatura matemáticas y recaudo matemáticas
            total_inscritos_matematicas += 1
            recaudo_matematicas += item["valor_inscripcion"]
        elif item['cod_progrma'] == "02":

            # Total inscritos tecnología electrónica y recaudo electrónica
            total_inscritos_electronica += 1
            recaudo_electronica += item["valor_inscripcion"]
        elif item['cod_progrma'] == "03":

            # Total inscritos Tecnología de sistemas
            total_inscritos_sistemas += 1
            recaudo_sistemas += item["valor_inscripcion"]
            
            # Diccionario guarda total de inscritos y contador por tipo de codigo

    resultado: dict = {
        "inscritos_matematicas": total_inscritos_matematicas,"Total recaudo matemáticas":recaudo_matematicas,
        "inscritos_electronica": total_inscritos_electronica,"Total recaudo electronica":recaudo_electronica,
        "inscritos_sistemas": total_inscritos_sistemas,"Total recaudo sistemas":recaudo_sistemas

    }
    return resultado


datos: list = [
    {
        "cod_progrma": "01",
        "valor_inscripcion": 120000
    },
    {
        "cod_progrma": "02",
        "valor_inscripcion": 150000
    },
    {
        "cod_progrma": "03",
        "valor_inscripcion": 110000
    },
    
]
print(inscritos_programa(datos))
