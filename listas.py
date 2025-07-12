numeros = [10,5,7,2,1]
print("Contenido de la lista original: ",numeros)

numeros[0]=111
print("Lista actualizada: ",numeros)

numeros[1]=numeros[4]
print("Nueva lista",numeros)
print("el valor de la primera posicion es: ",numeros[0])
print("El contenido de la lista es: ",numeros)
print("El tamaño o longitud de la lista es: ",len(numeros))

###

del numeros[1] # eliminando el segundo elemento de la lista
print("\nLongitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual
###
#las siguientes lineas presentan errores
#print(numeros[4]) # no hay posicion 4
#numeros[4]=1 # excede el limite de la lista
###
#recorre de derecha a izquierda, el recorrido normal es de derecha a izquierda
print("El ultimo elemento de la lista es: ",numeros[-1])
print("El elemento de la posicion 3 es: ",numeros[-2])
print("\n***********************\nMetodo append() e insert()\n")
numeros.insert(1,333)
print("Nuevo contenido de la lista:", numeros,"\ny el tamaño de la lista ahora es: ",len(numeros))
numeros.append(4)
print("Nuevo contenido de la lista:", numeros,"\ny el tamaño de la lista ahora es: ",len(numeros))
print("**************************\n")
valor = int(input("Ingrese un valor: "))
numeros.append(valor)
print("Nuevo contenido de la lista:", numeros,"\ny el tamaño de la lista ahora es: ",len(numeros))
print("**************************\n")
valor = int(input("Ingrese un valor: "))
posicion = int(input("En que posicion: "))
numeros.insert(posicion,valor)
print("Nuevo contenido de la lista:", numeros,"\ny el tamaño de la lista ahora es: ",len(numeros))
print("**************************\n")
print("LLenar una lista con un for y el metodo insert(): ")
miLista = [] #creando la lista
miLista1 = [] #creando la lista
for i in range(5):
    miLista.insert(4,i + 1)#el indicde determina el orden
    #continue
print(miLista,"\nAhora con el metodo append():")
for i in range(5):
    miLista1.append(i+1)#en orden
print(miLista1)
""" print("Sumar elementos de una lista: ")
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
    suma += miLista[i]

print(suma) """
""" print("Intercalar valores de la lista")
miLista = [10,1,8,3,5]
print(miLista)
miLista[0],miLista[4]=miLista[4],miLista[0]
miLista[1],miLista[3]=miLista[3],miLista[1]
print("Nueva orden de lista: ",miLista)
print("Ahora para un lista mayor: ")
miLista = [10,1,8,3,5]
longitud = len(miLista)
for i in range (longitud // 2):
     miLista[i],miLista[longitud-i-1]=miLista[longitud-i-1],miLista[i]
print(miLista)  """
""" # paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("Jhon Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Paso 2:", beatles)

# paso 3

for i in range(2):
    nombre = input("Ingrese un nuevo integrante: ")
    beatles.append(nombre)
print("Paso 3:", beatles)

# etapa 4
del beatles[3]
print(beatles)
del beatles[3]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles)) """
print("Copiado de listas")
# Copiando toda la lista
# lista1 = [1]
# lista2 = lista1[:]
# lista1[0] = 2
# print(lista2)

# Copiando parte de la lista
# miLista = [10, 8, 6, 4, 2]
# nuevaLista = miLista[1:3]#a partir de la posicion 1 imprime 3 elementos
# print(nuevaLista)

#indices negativos
#miLista = [10, 8, 6, 4, 2]
# nuevaLista = miLista [1:-1]#salida es [8,6,4]
# nuevaLista = miLista [-1:1]#salida es []
# nuevaLista = miLista [:3]#salida es [10,8,6]
# nuevaLista = miLista [3:]#salida es [4,2]
#nuevaLista = miLista [:]#salida es [10,8,6,4]
#print(nuevaLista)
#del miLista[1:3]#salida [10, 4, 2]
#del miLista[:]#salida []
#print(miLista)
""" 
#Operadores in y not
miLista = [0, 3, 12, 8, 2]
print(5 in miLista)#5 en la lista false
print(5 not in miLista)#5 no esta en la lista true
print(12 in miLista)#true """
""" print("Encontrar el mayor")
print("Codigo 1")
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)
print("Codigo 2, con rodaja")
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista [1:]:
   if i > mayor:
        mayor = i

print(mayor) """
""" print("Hallar un elemento en una lista")
miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente") """
# print("Juego de loteria, cuantos aciertos")
# sorteados = [5, 11, 9, 42, 3, 49]
# seleccionados = [3, 7, 11, 42, 34, 49]
# aciertos = 0

# for numeros in seleccionados:
#     if numeros in sorteados:
#         aciertos += 1

# print(aciertos)
""" 
#elimiando duplicados de una lista
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
result = list(set(my_list))
print("La lista con elementos únicos:")
#print(my_list)
#result = [item for n, item in enumerate(my_list) if item not in my_list[:n]]
result = []
for item in my_list:
    if item not in result:
        result.append(item)
print(result)
 """