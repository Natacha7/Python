'''
Pida al usuario la edad y el sexo, para que la computadora le indique si ya puede jubilarse.
Tome en cuenta que un Hombre se puede jubilar cuando tenga 62 años o más, en cambio, 
una mujer mayor se jubilara si tiene más de 57 años.
'''
def jubilarse(sexo,edad):

    if (sexo == str("Femenino")) and (edad > 57):
        print("Ya puede jubilarse")
    elif (sexo == str("Femenino")) and (edad <= 57):
        print("No puede jubilarse")
    elif (sexo == str("Masculino") and (edad >= 62)):
        print("Ya puede jubilarse")
    elif (sexo == str("Masculino") and (edad < 62)):
        print("No puede jubilarse")

sexo=input("Diga si su sexo es Femenino o Masculino: ")
edad=int(input("Diga su edad: "))
jubi=jubilarse(sexo,edad)










