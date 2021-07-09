def saludo(cadena):
    return "Hola {}! ¿Cómo estás?".format(cadena)

nombre = input("Ingrese su nombre:")
texto_saludo = logica.saludo(nombre)
print(texto_saludo)




