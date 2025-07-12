import os
os.system("cls")

print("Triangulo con asteriscos alineado a la izquierda\n")

for i in range(1, 6):
    print("* " * i)

print("------------\n")

print("Triangulo con asteriscos alineado a la derecha\n")

for k in range(6):
    print(" " * (2 * (6 - k)) + "* " * (k + 1))

print("------------\n")

print("Triangulo con asteriscos invertido\n")

for i in range(5, 0, -1):
    print("* " * i) #imprime el asterisco i veces   

print("------------\n")

print("Triangulo con asteriscos invertido y centrado\n")

for i in range(6, 0, -1):
    print(" " * (6 - i) + "* " * i)

print("------------\n")

print("Triangulo con asteriscos centrado\n")

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

print("------------\n")
