'''
La empresa “La TVE” ha decidido implementar un nuevo sistema de salarios para mejorar su clima organizacional. 
Las nuevas normas de incremento son:
•	Si es obrero, se incrementa un 10 por ciento. 
•	 Si es ingeniero y gana menos de 1’000.000, aumento del 8%.
•	 Si es ingeniero y gana entre de 1’000.001 y 2’000.000, incrementa el 6%.
•	 Si es ingeniero y gana entre de 2’000.001 y 3’000.000, el salario sube un 5%. 
•	 Si es ingeniero y gana entre de 3’000.001 y 4’000.000, hay un aumento del 3%. 
•	 Si es ingeniero y gana entre de 3’000.001 y 4’000.000 y se llama Ruperto Mena, se incrementa en 4%.
•	 Si es ingeniero y gana más de 4’000.000, un alza de 8 porciento.
•	 Si es publicista y gana más de 1’500.000, incrementa en $150.000. 
•	 Si es gerente se sube el salario un 2 %. 

Por lo anterior, debe desarrollarse un algoritmo que implemente estas modificaciones al sistema de salarios 
y nos muestre en pantalla el nombre, cargo, salario inicial, incremento y salario final del empleado.
'''
def incremento(Cargo,salario,Nombre):
    
    if (Cargo=="Obrero"):
        incremento=salario*0.10
    elif (Cargo=="Ingeniero") and (salario<1000000):
        incremento=salario*0.08
    elif (Cargo=="Ingeniero") and (salario>=1000000) and (salario<=2000000):
        incremento=salario*0.06
    elif (Cargo=="Ingeniero") and (salario>2000000) and (salario<=3000000):
        incremento=salario*0.05
    elif (Cargo=="Ingeniero") and (salario>3000000) and (salario<=4000000):
        incremento=salario*0.03
    elif (Cargo=="Ingeniero") and (Nombre== "Ruperto Mena") and (salario>3000000) and (salario<=4000000):
        incremento=salario*0.04
    elif (Cargo=="Ingeniero") and (salario>=4000000):
        incremento=salario*0.08
    elif (Cargo=="Publicista") and (salario>1500000):
        incremento=((150000*salario)/salario)
    elif (Cargo=="Gerente"):
        incremento=salario*0.02
    return incremento

Cargo=input("Diga si su cargo es Obrero, Ingeniero, Publicista o Gerente: ")
salario=int(input("Diga su salario en números: "))
Nombre=input("Diga su nombre: ")
Incremento_salario=incremento(Cargo,salario,Nombre)
Salario_final=salario+Incremento_salario
print("Su nombre es: ",Nombre)
print("Su cargo es: ",Cargo)
print("Su salario inicial es: ",salario)
print("El incremento de su salario es de: ", Incremento_salario)
print("Su salario final es: ", Salario_final)



