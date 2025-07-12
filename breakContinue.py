'''
# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")'''

#break
numeroMayor = -99999999
contador = 0

while True:
    numero = int(input("Ingrese un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        continue
        #break
    contador = 1
    if numero > numeroMayor:
        numeroMayor = numero

if contador != 0:
    print("El número mas grande es", numeroMayor)
else:
    print("No ha ingresado ningún número")

