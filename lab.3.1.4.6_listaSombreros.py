listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# para reemplazar el número de en medio con un número entero ingresado por el usuario.
print("La lista original es: ",listaSombrero)
numero = int(input("ingrese un numero para reemplazar el numero del medio: "))
listaSombrero[2]=numero
print("Lista actualizada: ",listaSombrero)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del listaSombrero[4]
print("Lista actualizada: ",listaSombrero)

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la lista es: ",len(listaSombrero))

print(listaSombrero)