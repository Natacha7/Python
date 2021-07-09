def promedio_suma(Nro_inscritos_lunes: int, Nro_inscritos_martes: int, Nro_inscritos_miercoles: int, Nro_inscritos_jueves: int, Nro_inscritos_viernes: int) ->str:
    promedio = (Nro_inscritos_lunes + Nro_inscritos_martes + Nro_inscritos_miercoles + Nro_inscritos_jueves + Nro_inscritos_viernes)/5
    promedioRedondeado = round(promedio)
    promedio_resultado = str(promedioRedondeado)
    return "El promedio de personas inscritas al curso de dibujo de lunes a viernes es: {}". format(promedio_resultado)

Nro_inscritos_lunes = int(50)
Nro_inscritos_martes = int(80)
Nro_inscritos_miercoles = int(100)
Nro_inscritos_jueves = int(45)
Nro_inscritos_viernes = int(30)

promedio = promedio_suma(Nro_inscritos_lunes, Nro_inscritos_martes, Nro_inscritos_miercoles, Nro_inscritos_jueves, Nro_inscritos_viernes)
print(promedio)



