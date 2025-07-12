c0 = int (input("Ingrese un numero positivo diferente de cero: "))
pasos = 0
while c0 != 1:
    if c0 <= 0:
        print ("error")
        c0 = int (input("Ingrese un numero positivo diferente de cero: "))
    elif c0 % 2 == 0:
        c0 = c0 // 2
       
        print(c0)
    else:
        c0 = (3 * c0) + 1
        print(c0)
    pasos += 1
print("pasos = ",pasos)


