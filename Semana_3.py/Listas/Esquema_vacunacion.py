'''
La Secretaría de Salud municipal desea conocer el número de adultos vacunad@s de acuerdo al siguiente esquema:
 
 
Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
1.	Cod_tipo_vacuna: str
2.	edad: int
3.	sexo: str         (f/m)
4.	gestante str   (s/n)
5.	viajero: str     (s/n)
Ejemplo Datos
datos: list = [
    {
        "cod_tipo_vacuna": 01
        "edad": 4
        "sexo": f
        "gestante": s
        "viajero ": s
 
    },
    
    {
        "cod_tipo_vacuna": 02
        "edad": 4
        "sexo": f
        "gestante": s
        "viajero ": s
    },

]


La respuesta debe retornar un diccionario con la siguiente información:
# Vacunas aplicadas contra el VPH
# Vacunas aplicadas contra el Td -Toxoide Diftérico
# Vacunas aplicadas contra el DPTa – Difteria, Tétanos, Tosferina Aceluar.
# Vacunas aplicadas contra la Fiebre Amarilla.
# Vacunas aplicadas contra la Influenza Estacional.
# Vacunas aplicadas contra Neumo 23 Adultos.
# Vacunas aplicadas a mujeres Gestantes
# de viajeros vacunad@s
'''
def Esquema_vacunacion(datos:list ) ->dict:
    Vacunas_VPH = 0
    Vacunas_Td = 0
    Vacunas_DPTa = 0
    Vacunas_fiebre_amarilla = 0
    Vacunas_influenza_estacional = 0
    Vacunas_neumo23 = 0
    Vacunas_gestantes = 0
    Vacunas_viajeros = 0

    for item in datos:
        if item['edad'] >= 9 and item['edad'] <= 20 and item['sexo'] == "f":
            Vacunas_VPH += 1
        elif item['sexo'] == "f" and item['edad'] >= 10 and item['edad'] <= 49 or item['gestante'] == "s":
            Vacunas_Td += 1

        if item['gestante'] == "s":
            Vacunas_DPTa += 1
        
        if item['gestante'] == "s" or item['edad'] >= 60:
            Vacunas_influenza_estacional += 1

        if item['edad'] >= 60:
            Vacunas_neumo23 += 1

        if item['gestante'] == "s":
            Vacunas_gestantes += 1

        if item['viajero'] == "s":
            Vacunas_viajeros += 1
        
        if item['edad'] <= 59 and item['viajero'] == "s":
            Vacunas_fiebre_amarilla += 1

    resultado: dict = {
        "Vacunas_aplicadas_contra_el_VPH" : Vacunas_VPH,
        "Vacunas_aplicadas_contra_el_Td_Toxoide_Diftérico" : Vacunas_Td,
        "Vacunas_aplicadas_contra_el_DPTa_Difteria_Tétanos_Tosferina_Aceluar": Vacunas_DPTa,
        "Vacunas_aplicadas_contra_la_Fiebre_Amarilla": Vacunas_fiebre_amarilla,
        "Vacunas_aplicadas_contra_la_Influenza_Estacional": Vacunas_influenza_estacional,
        "Vacunas_aplicadas_contra_Neumo_23_Adultos": Vacunas_neumo23,
        "Vacunas_aplicadas_a_mujeres_Gestantes": Vacunas_gestantes,
        "viajeros_vacunados": Vacunas_viajeros
    }
    return resultado
import pprint
datos: list = [
    {
        "viajero": "n",
        "cod_tipo_vacuna": "01",
        "edad": 4,
        "sexo": "f",
        "gestante": "n",
    },
    {
        "viajero": "s",
        "cod_tipo_vacuna": "02",
        "edad": 11,
        "sexo": "f",
        "gestante": "n",
    },
    {
        "viajero": "n",
        "cod_tipo_vacuna": "03",
        "edad": 25,
        "sexo": "f",
        "gestante": "s",
    },
    {
        "viajero": "s",
        "cod_tipo_vacuna": "04",
        "edad": 20,
        "sexo": "m",
        "gestante": "n",
    },
    {
        "viajero": "n",
        "cod_tipo_vacuna": "05",
        "edad": 22,
        "sexo": "f",
        "gestante": "s",
    },
    {
        "viajero": "n",
        "cod_tipo_vacuna": "05",
        "edad": 60,
        "sexo": "m",
        "gestante": "n",
    },
    {
        "viajero": "n",
        "cod_tipo_vacuna": "06",
        "edad": 60,
        "sexo": "m",
        "gestante": "n"
    }
]
pprint.pprint(Esquema_vacunacion(datos))


