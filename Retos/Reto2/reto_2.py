def reportarBonificacion(dicReporte: dict) -> str:
    return dicReporte["empleado"]+" - "+"Bonificación: "+dicReporte["bonificacion"]

def generarReporteBonificacion(dicEmpleado: dict) -> str:
    if dicEmpleado['antiguedad'] < 1:
        boni = "Tiene una Bonificación equivalente al 5 por ciento de su salario mensual"
    else:
        if dicEmpleado['antiguedad'] >= 1 and dicEmpleado['antiguedad'] < 2:
            boni = "Tiene una Bonificación equivalente al 7 por ciento de su salario mensual"
        else:
            if dicEmpleado['antiguedad'] >= 2 and dicEmpleado['antiguedad'] < 5:
                boni = "Tiene una Bonificación equivalente al 10 por ciento de su salario mensual"
            else:
                if dicEmpleado['antiguedad'] >= 5 and dicEmpleado['antiguedad'] < 10:
                    boni = "Tiene una Bonificación equivalente al 16 por ciento de su salario mensual"
                else:
                    boni = "Tiene una Bonificación equivalente al 20 por ciento de su salario mensual"
    reporteBonificacion = {
        "bonificacion": boni,
        "empleado": dicEmpleado["empleado"]
    }
    return reporteBonificacion



# Esta función emite el reporte de la Bonificación

dicEmpleado: dict = {
    "Id_empleado":"id_001",
    "empleado":"Sandra Peña",
    "antiguedad": 1,
}

print('\n')
print(reportarBonificacion(generarReporteBonificacion(dicEmpleado)))

