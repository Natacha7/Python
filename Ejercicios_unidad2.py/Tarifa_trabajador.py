'''
A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. Si la
cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las
horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la tarifa
ingresadas por el usuario.
'''
Tarifa_por_hora = float(input("Digite la tarifa por hora del trabajaror $ "))
Horas_trabajadas = int(input("Digite la cantidad de horas trabajadas del trabajador: "))

if Horas_trabajadas > 40:
    Valor_hora_extra = Tarifa_por_hora + (Tarifa_por_hora*0.5)
    salario_horas_extras = (Tarifa_por_hora*40) + ((Horas_trabajadas-40)*Valor_hora_extra)
    print("El salario del trabajador es de ${:,.0f}".format(salario_horas_extras))
else:
    salario = Tarifa_por_hora * Horas_trabajadas
    print("El trabajador trabajo", Horas_trabajadas, "horas, por estas horas obtuvo un salario de ${:,.0f}".format(salario))



