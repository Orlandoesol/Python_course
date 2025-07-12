print("La Witsi Witsi Araña subió a su telaraña.")
print()    
print("Vino la lluvia y se la llevó.")
print("--------------------------------------------\n")
print("La Witsi Witsi Araña\nsubió a su telaraña.\n")
print()
print("Vino la lluvia\ny se la llevó.")
print("----------------------------")
'''las comas que separan los argumentos desempeñan un papel completamente diferente
a la coma dentro de la cadena. El primero es una parte de la sintaxis de Python, 
el segundo está destinado a mostrarse en la consola.
Una función print() invocada con más de un argumento genera la salida en una sola línea.
La función print() pone un espacio entre los argumentos emitidos por iniciativa propia.'''
print("La Witsi Witsi Arañar" , "subió" , "a su telaraña.")
print("----------------------------\n")
''' #La forma en que pasamos los argumentos a la función print() 
#es la más común en Python, y se denomina manera posicional 
#(este nombre proviene del hecho de que el significado del 
#argumento está dictado por su posición, por ejemplo, 
#el segundo argumento se emitirá después del primero, y no al revés).'''
print("Mi nombre es", "Python.")
print("Monty Python.")
print("\n---------------Argumento de palabra clave end=--------------------\n")
''' La función print() tiene dos argumentos de palabras clave que se pueden
utilizar para estos propósitos. El primero de ellos se llama end. 
Un argumento de palabra clave consta de tres elementos: una palabra clave que identifica el argumento (end -termina aquí); un signo de igual (=); y un valor asignado a ese argumento.
Cualquier argumento de palabra clave debe ponerse después del último argumento posicional (esto es muy importante).
El comportamiento predeterminado refleja la situación en la que el argumento de la palabra clave end se usa implícitamente de la siguiente manera: end="\n";
Pero tambien funciona con end="", es decir sin espacio entre las comillas.
'''
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")
print("Mi nombre es", "Python.", end="")#la diferencia es un espacio en la impresion
print("Monty Python.")
print("\n---------------Argumento de palabra clave sep=--------------------\n")
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")#separa las palabras con el caracter que esta entre las comillas
print("Mi", "nombre", "es", "Monty", "Python.", sep="*")
print("Mi", "nombre", "es", "Monty", "Python.", sep=" ")
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("-----------------------------------------")
print("Laboratorio funcion print() con sep y end")
print("Fundamentos","Programación","en")
print("Python")

print("Fundamentos","Programación","en",sep="***",end="...")
print("Python")

#lab 2.1.2.11 literales
print('"Estoy"\n""aprendiendo""\n"""Python"""')

#print(sep="&", "fish", "chips")#erro de sintaxis
