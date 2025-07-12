#print("I like to be a module.")
#print(__name__)
'''counter = 0

if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

*********************************
la línea que comienza con #! tiene muchos nombres - puede llamarse shabang,
shebang, hashbang, poundbang o incluso hashpling (no nos preguntes por qué).
El nombre en sí no significa nada aquí - su función es más importante.
Desde el punto de vista de Python, es sólo un comentario, ya que comienza con #.
Para Unix y sistemas operativos similares a Unix (incluyendo MacOS) tal línea
instruye al sistema operativo cómo ejecutar el contenido del archivo
(en otras palabras, qué programa necesita ser lanzado para interpretar el texto)
. En algunos entornos (especialmente los conectados con servidores web)
la ausencia de esa línea causará problemas; una cadena (tal vez de varias
líneas) colocada antes de cualquier instrucción del módulo (incluyendo
las importaciones) se llama doc-string, y debe explicar brevemente el propósito
y el contenido del módulo; '''
#!/usr/bin/env python3

"""module.py - an example of a Python Module"""

__counter = 0

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some test for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prod(my_list) == 120)
