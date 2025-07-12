""" print("\"--Funcion Simple--\"")
def mensaje():    # definiendo una función
    print("Hola")    # cuerpo de la función

mensaje()    # invocación de la función  """


""" print("\"--Función con arbgumento--\"")
def hola(nombre): #Definiendo una función
    print("Hola", nombre) # cuerpo de la función

nombre = input("Ingrese su nombre: ")

hola(nombre) # Invocación o llamado de la función
 """

""" print("\"--Funcion con parametro numerico--\"")

def mensaje(numero):
    print("El numero ingresado por parametro es: ",numero)

#mensaje(1) # se esccribe el número o argumento en los parentesis de la función
#numero = int(input("Ingrese un número: ",))#Se pide el argumento o numero por teclado
#mensaje(numero) # con esta invoación se imprime el numero
numero = 1234 #variable completamente diferente al argumento numero de la fución
mensaje(1)
print ("Esto es una variable: ",numero) """

""" print("\"--Funcion con dos parametros--\"")
def mensaje(que,numero):
    print("Ingresa ",que,"número",numero)

mensaje("Telefono",11)
mensaje("Precio",5)
mensaje("número","número") """

""" print("\"--Función con parametros posicionales--\"")

def miFuncion(a,b,c):
    print(a,b,c)

miFuncion(1,2,3)

print("****************")

def presentar(primerNombre,segundoNombre):#orden de los parametros
    print("Hola, mi nombre es: ",primerNombre,segundoNombre)

# presentar("Luke","Skywalker")
# presentar("Jesse","Quick")
# presentar("Clarck","Kent")

presentar("Skywalker","Luke")# igual cantidad según los parametros
presentar("Quick","Jesse")
presentar("Kent","Clarck") """

""" print("\"--Función con argumentos con palabras clave--\"")

def presentar(primerNombre,segundoNombre):
    print("Hola, mi nombre es: ",primerNombre,segundoNombre)

presentar(primerNombre= "James", segundoNombre= "Bond")
presentar(segundoNombre= "Skywalker", primerNombre= "Luke") """

""" print("El combinar argumentos posicionales y de palabras clave")

#Regla: primero argumentos posicionales y después los de palabras clave.

def suma(a,b,c,):
    print(a,"+",b,"+",c,"=",a+b+c)

suma(1,2,3) # Invocacion pasando los parametros directamente
suma(c=1, a=2, b=3) # usando palabras claves
suma(3,c=1,b=2) #El argumento (3) para el parametro a es pasado utilizando la manera posicional.
                #Los argumentos para c y b son especificados con palabras clave. """


""" print("\"--Mas detalles de los parametros--\"")

def presentar(primerNombre, segundoNombre="González"):
    print("Hola, mi nombre es: ",primerNombre,segundoNombre)

#presentar("Jorge","Perez")
presentar("Enrique")
presentar(primerNombre="Roberto") """

""" def direccion(calle,ciudad,codigoPostal):
    print("Tu direcciómn es: ",calle,ciudad,codigoPostal)

c = input("Calle: ")
cp = input("Codigo Postal: ")
cd = input("Ciudad: ")

direccion(c,cd, cp) """

""" def resta(a,b):
    print(a-b)

resta(5,2)
resta(2,5) 
resta(a=5, b=2)
resta(a=2, b=5)
resta(5, b=2)
resta(5,2)
resta(a=5,2)#error de sintaxis las palabras claves siempre van de segundo """

#print("\"--Return--\"")

""" def felizAñoNuevo(deseos=True):
    print("Tres ...\nDos ...\nUno ...")
    if not deseos:
        return

    print("¡Feliz año nuevo!")

felizAñoNuevo() """

""" def funcionAburrida():
    return 123

x = funcionAburrida()

print("La funcionAburrida ha devuelto su resultado. Es: ",x) """

# valor = None # valor nulo o vacio o ninguno
# if valor == None:
#     print("Lo siento, no tienes ningún valor") 

""" def strangeFunction(n):
    if(n % 2 == 0):
        return True

print(strangeFunction(2)) # True
print(strangeFunction(1)) # None """

print("\"--Lista y funciones--\"")

""" def sumaDeLista(lst):
    suma = 0

    for elem in lst:
        suma += elem

    return suma
print(sumaDeLista([5,4,3]))# Ojo si es una lista los valores van en corchetes """

n =int(input("Ingrese un valor: "))
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList
#print(strangeListFunction(5))#puedo pasar el parametro direcamente
print(strangeListFunction(n)) #Se invoca la funcion y se pide que imprima el resultado pasandole el parametro pedido por consola
