import os

os.system("cls")

def menu():
    print("\n----Menú-----")
    print("1. Suma los números de una lista")
    print("2. Contar las vocales, consonantes y otros caracteres de una frase")
    print("3. Crear una matriz n x n y llenar sus diagonales")
    print("Imprima X para salir")

#Opcion 1
def suma_lista():
    numeros = []
    while True:
        entrada = input("Ingrese un  número (o presione enter  para terminar): ")
        if entrada == '':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Error: No es un número, ingrese un número válido.")

    suma =  sum(numeros)
    print(f"La suma de los números es: {suma}")

#Opcion 2
def contar_caracteres():
    frase = input("Ingrese una frase")
    vocales = "aeiouAEIOU"
    contVocales = sum(1 for char in frase if char in vocales)
    contConsonantes = sum(1 for char in frase if char.isalpha() and char not in vocales)
    #contOtros = sum(1 for char in frase if not char.isalpha() and not char.isspace() and char.isspace())
    #contOtros =  sum(1 for char in frase if not char.isalpha())
    contOtros =  sum(1 for char in frase if not char.isalpha() and not char.isalnum())
    #contOtros = len(frase) - (contVocales + contConsonantes)
    """     
    vocales_count = 0
    consonantes_count = 0
    especiales_count = 0
    for character in frase:
         if(character in vocales):
            vocales_count += 1
         elif character.isalpha():
            consonantes_count += 1
         else:
            especiales_count += 1
    """

    #print(f"Vocales : {vocales_count}, consonantes: {consonantes_count} y otros: {especiales_count}")
    print(f"Vocales : {contVocales}, consonantes: {contConsonantes} y otros: {contOtros}")

#Opcion 3
def crear_matriz():
    n = int(input("Ingrese el tamaño de la matriz: "))
    #matriz = [[" " * n for _ in range(n)]]#5 / 3
    matriz = []

    for i in range(n):
        row = []
        for  j in range(n):
            if i == j or  i+j == n-1:
                row.append("*")
            else:
                row.append(" ", end="")
        matriz.append(row)
    print(matriz)


        


#Programa principal

while True:
    menu()

    opcion = input("Ingrese una opcion: ").strip().upper()

    if opcion == "1":
        suma_lista()
    elif opcion  == "2":
        contar_caracteres()
    elif opcion ==  "3":
        crear_matriz()
    elif opcion ==  'X':
        print("Adiós")
        break





