# Creacion de tuplas
# Nota: cada elemento de una tupla puede ser de distinto tipo (punto flotante, entero, cadena, etc.).
tupla1 = (1,2,4,8,16)
tupla2 = 1., .5, .25, .125
tupla3 = (4376540, "Orlando Espinosa Olivero",91.8)
'''
Si se desea crear una tupla de un solo elemento, se debe de considerar el hecho de que,
debido a la sintaxis (una tupla debe de poder distinguirse de un valor entero ordinario), 
se debe de colocar una coma al final:
'''
tuplaUnElemento1 = (1, )
tuplaUnElemento2 = 1., 


print(tupla1)
print(tupla2)
print(tupla3)
print(tuplaUnElemento1)
print(tuplaUnElemento2)

print("\n------Utilzando las tuplas-------\n")
miTupla = (1, 10, 100, 1000)

print(miTupla)
print(miTupla[0], "-> primer elemeto de la tupla")
print(miTupla[-1], "-> ultimo elemeto de la tupla")
print(miTupla[1:])
print(miTupla[:-2])

for elem in miTupla:
    print(elem)

print("\n------Utilzando las tuplas, ejemplo 2-------\n")
miTupla = (1, 10, 100)

t1 = miTupla + (1000, 10000)
t2 = miTupla * 3

print(len(t2))
print("t1: ",t1)
print("t2: ",t2)
print("El numero 10 esta en miTupla? ",10 in miTupla)
print("El numero -10 no esta en miTupla? ",-10 not in miTupla)
