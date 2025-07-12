import os
os.system("cls")

print("Triangulo con asteriscos alineado a la izquierda\n")

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print()

print("------------\n")
print("Triangulo con asteriscos alineado a la derecha\n")

rows = 5
for k in range(rows):
    for l in range(2*(rows - k)):
        print(" ", end="")
    for l in range(k + 1):
        print("*", end=" ")
    print()

print("------------\n")