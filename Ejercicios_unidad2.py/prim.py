def es_primo():
    rta = 0
    num = int(input('Dígite un número de dos cifras: '))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                #return False
                rta = 'no es primo'
                return f"El número {num} {rta}"
        else:
            #return True
            rta = 'es primo'
            return f"El número {num} {rta}"
    else:
        if num < 0:
            return f"Los números negativos no son primos"
    
print(es_primo())