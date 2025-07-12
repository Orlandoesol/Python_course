numero = input("Introduzca un número entre 1 y 10: ")

try:
    numero = int(numero)
except:
    numero = 0
while not 1 <= numero <= 10:

# El número no es válido
# Se pide volver a introducir un número
# numero = input("Introduzca un número entre 1 y 10: ")
    try:
        numero = int(numero)
    except:
        numero = 0
print("Estamos seguros de que", numero,
    "es un número comprendido entre 1 y 10 incluidos.")