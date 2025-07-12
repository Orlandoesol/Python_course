""" for i in range(10):
    print("El valor de i es actualmente", i)
print("______________________________________")
for i in range(2, 8):
    print("El valor de i es actualmente", i)
print("______________________________________")
for i in range(1, 11):
    print("El valor de i es actualmente", i)
 """

#Lab.3.1.2.6
import time

    # Escribe un ciclo for que cuente hasta cinco.
    # Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    # Cuerpo del ciclo - uso: time.sleep (1)

# Escribe una función de impresión con el mensaje final.
for i in range(1,6):
    print(i,"Mississippi")
    time.sleep (1)
print("¡Listo o no, ahí voy")

''' numeroMayor = -99999999
contador = 0

numero = int (input("Ingtesa un número o escribe -1 para finalizar el programa:"))

while numero != -1:
    if numero == -1:
        continue
    contador = 1
    if numero > numeroMayor:
        numeroMayor = numero
    numero = int (input("Ingtesa un número o escribe -1 para finalizar el programa:"))
if contador:
    print("El numero mas grande es", numeroMayor)
else:
    print("No ha ingresado ningún numero") '''

""" pow = 1
for exp in range(16):
    print ("2 a la potencia de", exp, "es", pow)
    pow * = 2  """

for i in range(5):
    print(i)
else:
    print("else:", i)