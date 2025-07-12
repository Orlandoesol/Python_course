#algo = float(input("Insertar un numero: "))
#resultado = algo ** 2.0
#print(algo, "al cuadrado es: ",resultado)

print("Ejericio funcion input\n------------------------------------\n")
""" print("Imprimir hipotenusa, pidiendo los catetos")
cateto_a = float(input("Inserte la longitud del primer cateto: "))
cateto_b = float(input("Inserte la longitud del segundo cateto: "))
hipo = (cateto_a**2 + cateto_b**2)**.5
print("La longitud de la hipotenusa es: ", hipo) """

# nom = input("¿Me puedes dar tu nombre por favor? ")
# ape = input("¿Me puedes dar tu apellido por favor? ")
# print("Gracias.")
# print("\nTu nombre es " + nom + " " + ape + ".")
# cateto_a = float(input("Ingresa la longitud del primer cateto: "))
# cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
# print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))

#2.1.6.9 LABORATORIO: Entradas y salidas simples
# ingresa un valor flotante para la variable a aquí
a = float(input("Ingrese el primer numero: "))
# ingresa un valor flotante para la variable b aquí
b = float(input("Ingrese el segundo numero: "))
3
# muestra el resultado de la suma aquí 
suma = a + b
print("El resultado de la suma es: ", suma)
# muestra el resultado de la resta aquí
resta = a-b 
print("El resultaod de la resta es: ",resta)
# muestra el resultado de la multiplicación aquí
multipilicacion = a * b
print("El resultado de la multiplicacion es: ", multipilicacion)
# muestra el resultado de la división aquí
division = a / b
print("El resultado de la division es: ",division)

print("\n¡Eso es todo, amigos!")

#2.1.6.10 LABORATORIO: Operadores y expresiones
 
x = float(input("Ingresa el valor para x: "))
#coloca tu código aquí
#y=1/(x+(1/(x+1/(x+(1/x)))))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)
