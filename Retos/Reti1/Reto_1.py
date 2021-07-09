def promedio_suma(Nro_inscritos_lunes, Nro_inscritos_martes, Nro_inscritos_miercoles, Nro_inscritos_jueves, Nro_inscritos_viernes):
    promedio = (Nro_inscritos_lunes + Nro_inscritos_martes + Nro_inscritos_miercoles + Nro_inscritos_jueves + Nro_inscritos_viernes)/5
    return promedio

Nro_inscritos_lunes = int(50)
Nro_inscritos_martes = int(80)
Nro_inscritos_miercoles = int(100)
Nro_inscritos_jueves = int(45)
Nro_inscritos_viernes = int(30)

promedio_inscritos = promedio_suma(Nro_inscritos_lunes, Nro_inscritos_martes, Nro_inscritos_miercoles, Nro_inscritos_jueves, Nro_inscritos_viernes)
print("El promedio de personas inscritas al curso de dibujo de lunes a viernes es de: ", promedio_inscritos)


