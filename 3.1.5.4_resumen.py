vehiculosUno = ['carro', 'bicicleta', 'moto']
print(vehiculosUno) # salida: ['carro', 'bicicleta', 'moto']

vehiculosDos = vehiculosUno
del vehiculosUno[0] # borra 'carro'
print(vehiculosDos) # salida: ['bicicleta', 'moto']
print("**********************")
colores = ['rojo', 'verde', 'naranja']

copiaTodosColores = colores[:] # copia la lista completa
copiaParteColores = colores[0:2] # copia parte de la lista
print(copiaTodosColores,"\n",copiaParteColores)

print("**********************")
listaMuestra = ["A", "B", "C", "D", "E"]
nuevaLista = listaMuestra[2:-1]
print(listaMuestra,"\n", nuevaLista) # salida: ['C', 'D']

print("**********************")
miLista = [1, 2, 3, 4, 5]
rodajaUno = miLista [2:]
rodajaDos = miLista [:2]
rodajaTres = miLista [-2:]
print(miLista)
print(rodajaUno) # salidas: [3, 4, 5]
print(rodajaDos) # salidas: [1, 2]
print(rodajaTres) # salidas: [4, 5]
print("**********************")
miLista2 = [1, 2, 3, 4, 5]
print(miLista2)
del miLista2 [0:2]
print(miLista2) # salida: [3, 4, 5]

del miLista2[:]
print(miLista2) # elimina el contenido de la lista, genera: []

print("**********************")
miLista = ["A", "B", 1, 2]

print("A" in miLista) # salida: True
print("C" not in miLista) # salida: False
print(2 not in miLista) # salidas: False
print("**********************")
print("Ejercicio 1")
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[0]

print(l3)
print("**********************")
print("Ejercicio 2")
l1 = ["A", "B", "C"]
l2 = l1 # ["A", "B", "C"]
l3 = l2 # ["A", "B", "C"]

del l1[0] # ["B", "C"]
del l2

print(l3)
print("**********************")
print("Ejercicio 3")
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[:]

print(l3)
print("**********************")
print("Ejercicio 4")
l1 = ["A", "B", "C"]
l2 = l1[:]
l3 = l2[:]

del l1[0]
del l2[0]

print(l3)

print("**********************")
print("Ejercicio 5")
miLista = [1, 2, "in", True, "ABC"]

print(1 in miLista) # salida True
print("A" not in miLista) # salida True
print(3 not in miLista) # salida True
print(False in miLista) # salida False