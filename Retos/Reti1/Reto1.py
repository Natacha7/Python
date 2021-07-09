'''
La academia de dibujo profesional Leonardo da vinci desea conocer el promedio de personas inscriptas al curso
de dibujo de lunes a viernes

'''
#Promedio de personas inscriptas en el curso de dibujo de lunes a viernes:
def promedio_suma(Nro_inscritos_lunes: int, Nro_inscritos_martes: int, Nro_inscritos_miercoles: int, Nro_inscritos_jueves: int, Nro_inscritos_viernes: int) ->str:
    promedio = (Nro_inscritos_lunes + Nro_inscritos_martes + Nro_inscritos_miercoles + Nro_inscritos_jueves + Nro_inscritos_viernes)/5
    return promedio

print('El promedio de personas inscritas al curso de dibujo de lunes a viernes es:', promedio_suma(50, 80, 100, 45, 30))

