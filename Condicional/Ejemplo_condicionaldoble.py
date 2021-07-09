'''
CONDIONAL DOBLE
Desarrolle un algoritmo que permita leer un valor cualquiera N y escriba si dicho número es par o impar.

ALGORITMO
Inicio
     Digite un valor N
    Si N/2=entero entonces  
           El numero es par
           
        Si No
           El numero es impar
     Fin Si
     
Fin

'''
a = int(input("Digite un número: "))

if a % 2 ==0:
    print('El número', a,'es par')
else:
    print('El número', a, 'es impar')

