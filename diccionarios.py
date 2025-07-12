# Un diccionario en python es un conjunto de pares de claves (key) y valor
print("-------Diccionarios---------\n","--------Ejemplo 1----------\n")
#nombre -> clave : valor
'''
La lista de todos los pares es encerrada con llaves, mientras que los pares son separados
por comas, y las claves y valores por dos puntos.
'''
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)
print("------Ejemplo 2-----------")
print(dict['gato'])# Llamando la clave, trae el valor
print(numerosTelefono['Suzy'])
print("------Ejemplo 3-----------")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")
print("\n--------Metodo Keys---------\n")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])
print("\n--------Funcion Sorted, para que la salida sea ordenada---------\n")
# Orden alfabetico de las claves
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in sorted(dict.keys()):
    print(key, "->", dict[key])

print("\n--------metodos item() y values()---------\n")
# items(). Este método regresa una lista de tuplas 
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print("\n----Metodo item()----\n")
for spanish, french in dict.items():
    print(spanish, "->", french)
print("\n----Metodo values()----\n")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dict.values():
    print(french)
print("\n----Modificar, agregar y eliminar valores de un diccionario----\n","----Modificar-------\n")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print("Diccionario original",dict)
dict['gato'] = 'minou'
print("Diccionario modificado",dict,"\n\n-----Agregar claves--------------\n")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print("Diccionario original",dict)
dict['cisne'] = 'cygne'# Clave nueva mas valor
print("Diccionario modificado",dict,"\n\n-----Metodo update()--------------\n")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print("Diccionario original",dict)
dict.update({"pato" : "canard"})
print("Diccionario modificado",dict,"\n\n-----Eliminar Claves, del --------------\n")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print("Diccionario original",dict)
del dict['perro']# palabra del, para borrar
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print("Diccionario modificado",dict,"\n\n-----Eliminar el ultimo elemento del diccionario, popitem --------------\n")
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
print("Diccionario original",dict)
dict.popitem()
print("Diccionario modificado",dict,"\n\n-----Diccionarios y tuplas --------------\n")    # outputs: {'gato' : 'chat', 'perro' : 'chien'}
""" grupo = {}# nombre diccionario

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)# si el valor ya existe, suma los valores y da el promedio
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador) """

print("---Puntos claves---")
miTupla = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(miTupla)

miLista = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(miLista)

'''
Puedes navegar a través de los elementos de una tupla con un bucle (Ejemplo 1), 
verificar si un elemento o no esta presente en la tupla (Ejemplo 2), 
emplear la función len() para verificar cuantos elementos existen en la tupla (Ejemplo 3), 
o incluso unir o multiplicar tuplas (Ejemplo 4):
'''
print("Ejemplo 1")
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

print("Ejemplo 2")
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

print("Ejemplo 3")
t3 = (1, 2, 3, 5)
print(len(t3))

print("Ejemplo 4")
t4 = t1 + t2
t5 = t3 * 2

print(t4)
print(t5)
'''
También se puede crear una tupla utilizando la función integrada 
de Python tuple(). Esto es particularmente útil cuando se desea 
convertir un iterable (por ejemplo, una lista, rango, cadena, etcétera) en una tupla:
'''
print("------tuple()---------")
miTup = tuple((1, 2, "cadena"))
print(miTup)

lst = [2, 4, 6]
print(lst)    # salida: [2, 4, 6]
print(type(lst))    # salida: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'>
'''
De la misma manera, cuando se desea convertir un iterable en una liste, se puede emplear la función integrada de Python denominada list():
'''
tup = 1, 2, 3, 
lst = list(tup)
print(type(lst))    # outputs: <class 'list'>