while True:
    ingreso=float(input("Ingrese el ingreso anual:"))
    #
    # Coloca tu código aquí.    
    #
    if ingreso < 85528:
        # n sera la variable del valor del impuesto
        n=(ingreso*0.18)
        ipi=(n-556.2)
        impuesto=ipi
    elif ingreso > 85528:
        n=(ingreso-85528)*0.32
        ipi=14839.2+n
        impuesto=ipi
    if impuesto < 0:
        impuesto=0.0
    impuesto=round(impuesto, 0)
    print("El impuesto es: ", impuesto, "pesos")
'''
while True:
    income = float(input("Enter the annual income: "))

    #
    # Write your code here.
    #
    if income < 85528:
        # n sera la variable del valor del impuesto
        n=(income*0.18)
        ipi=(n-556.2)
        tax=ipi
    elif income > 85528:
        n=(income-85528)*0.32
        ipi=14839.2+n
        tax=ipi
    if tax < 0:
        tax=0.0

    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")
'''
