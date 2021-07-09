'''
Desarrolle un algoritmo que funcione como caja registradora. Que pare cuando el código del 
artículo se igual a *. Que lea código del articulo,nombre y Precio. 
Debe calcular subtotal,iva(15%) y total factura.
'''
#programa principal

codigo = 0

while codigo != "*":
        codigo = input("Ingrese el código: ")
        if codigo != "*":
          nombre = input("Nombre del artículo: ")
          precio = float(input("Precio del artículo: "))
          print(codigo)
          print(nombre)
          print(precio) 
          subtotal = round((precio/1.15),2)
          iva = round((subtotal * 0.15),2)
          Total_factura = round((subtotal + iva),2)
          print("El subtotal es: ", subtotal, "El IVA es: ", iva, "El total de la factura es: ", Total_factura)
            
      




    
