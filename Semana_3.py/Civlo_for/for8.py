total = 0
for i in range(5):
    nuevoNumero = int(input("Introduce un número: "))
    if nuevoNumero == 0:
        total += 1

print("Has introducido ", total, "ceros")


