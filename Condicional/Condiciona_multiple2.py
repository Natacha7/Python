'''
Desarrolle un algoritmo que permita convertir
calificaciones numéricas a letras, según la 
siguiente tabla: Se asume que la nota es un 
numero entero y está comprendida entre 1 y 20.

A = 19 y 20,
B = 16, 17  y 18 
C = 13, 14 y 15
D = 10, 11 y 12,
E =  1 hasta el  9.

'''
calif = int(input("Digite la calificación entre 1 y 20: "))

if (calif >= 19) and (calif <= 20):
    Calificacion = input("La calificación es: A")
else:
    if (calif < 19) and (calif >= 16):
        Calificacion = input("La calificación es: B")
    else:
        if (calif < 16) and (calif >= 13):
            Calificacion = input("La calificación es: C")
        else:
            if (calif < 13) and (calif >= 10):
                Calificacion = input("La calificación es: D")
            else:
                if (calif >= 1) and (calif < 10):
                    Calificacion = input("La calificación es: E")
                    
print("La calificación es: ", str+(Calificacion))



