miLista = [8, 10, 6, 2, 4] # lista para ordenar
print("Lista inicial",miLista)
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

""" print(miLista,"\n****Metodo burbuja interactivo****")
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista) """

print("****Metodo sort()****")
#lst = [5, 3, 1, 2, 4]
#lst = ["D","F","A","Z"]
a = 3
b = 1
c = 2

lst = [a,b,c]
#print(lst)

lst.sort ()
print(lst) # salida: [1, 2, 3, 4, 5]
print("****Metodo reverse()****")
""" lst = [5, 3, 1, 2, 4]
print(lst) """
a = "A"
b = "B"
c = "C"
d = ""

lst = [a,b,c,d]
    
lst.reverse()
print (lst) # salida: [4, 2, 1, 3, 5]