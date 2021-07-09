
def bonificacion(n):
        
    if n <= 1000000:
       bonificacion=float(0)
    else:
     if n <= 2500000:
        bonificacion=float(n*0.04)
     else:
       if n > 2500000:
          bonificacion=float(n*0.08)
    return bonificacion

print('\n')
numero1=float(input("Diga las ventas realizadas: "))
x=bonificacion(numero1)
print('la bonificacion es: $ {:,.0f}'.format(x))
print('\n')