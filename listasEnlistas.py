row = []

for i in range(8):
    row.append("WHITE_PAWN")
print(row)
print("*************************")
row = ["WHITE_PAWN" for i in range(8)]
print(row)

#comprension de listas
#El fragmento de código genera una lista de diez elementos y la rellena con cuadrados de diez números enteros 
# que comienzan desde cero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
squares = [x ** 2 for x in range(10)]
print(squares)

#El fragmento crea un arreglo de ocho elementos que contiene las primeras ocho potencias del numero dos (1, 2, 4, 8, 16, 32, 64, 128)
twos = [2 ** i for i in range(8)]
print(twos)

#El fragmento crea una lista con solo los elementos impares de la lista squares.
odds = [x for x in squares if x % 2 != 0 ]
print(odds)



