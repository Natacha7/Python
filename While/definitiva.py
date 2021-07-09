'''
El curso de Algoritmia y programación se califica con dos
parciales (el primero tiene un peso de 30% y el segundo 35%),
una nota de laboratorios (25%) y una nota del trabajo final 
del curso (10%). Calcular la nota definitiva para un grupo 
de n estudiantes.
'''
#Función
def calcular_definitiva(p1, p2, l, t):
    defini = p1*0.3 + p2*0.35 + l*0.25 + t*0.1
    return (defini)

#programa principal
numeroEst = int(input("Ingrese el número de estudiantes: "))
j = 1
while(j<=numeroEst):
    nombre = input("Ingrese el nombre: ")
    par1 = float(input("parcial 1: "))
    par2 = float(input("parcial 2: "))
    lab = float(input("laboratorios: "))
    tra = float(input("trabajos: "))

    definitiva = calcular_definitiva(par1, par2, lab, tra)
    print(definitiva)
    print("La nota definitiva de: ", nombre, " es: ", definitiva)
    j += 1
    
