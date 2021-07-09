'''
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar
un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados
cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá
informar el importe que gasta la empresa en sueldos al personal.
'''
n=int(input("Digite el número de empleados: "))
sueldo = 0
empleados_100_300 = 0
empleados_mas_300 = 0
gasto_sueldos = 0
numero_empleados = 0
while numero_empleados < n:
    sueldo=int(input("Ingrese el sueldo del empleado $"))
    numero_empleados +=1
    gasto_sueldos = gasto_sueldos +sueldo
    if  sueldo >= 100 and sueldo <= 300:
        empleados_100_300 += 1
    elif sueldo > 300:
        empleados_mas_300 += 1

print("La cantidad de empleados que cobran entre $100 y $300 son: ", empleados_100_300)
print("La cantidad de empleados que cobran más de $300 son: ", empleados_mas_300)
print("El importe que gasta la empresa en sueldos del personal es $", gasto_sueldos)