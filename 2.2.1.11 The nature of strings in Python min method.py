# Demonstrating min() - Example 1:
print(min("aAbByYzZ")) # Output: 'A'

# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']') # Output: [ ]

t = [0, 1, 2]
print(min(t)) # Output: 0

'''
¿Cómo funciona?

La función min() devuelve el elemento más pequeño en un iterable (como una cadena, lista o tupla).
Cuando se aplica a una cadena, min() compara los caracteres lexicográficamente, lo que significa que los
compara en función de sus puntos de código Unicode.

En la cadena dada "aAbByYzZ", los caracteres se comparan de la siguiente manera:

Las letras mayúsculas vienen antes que las letras minúsculas (por ejemplo, 'A' viene antes que 'a')
Las letras se comparan alfabéticamente (por ejemplo, 'a' viene antes que 'b')
¿Cuál es la salida?
El carácter más pequeño en la cadena es 'A', por lo que la salida del código es: A

Si la cadena contiene caracteres no alfabéticos (por ejemplo, números, puntuación),
la función min() todavía funcionará, pero la comparación se basará en los puntos de código Unicode
de esos caracteres.

Ejemplo de Caso de Uso

Este código se puede utilizar para encontrar el carácter más pequeño en una cadena, lo que puede ser útil
en diversas aplicaciones, como:

Ordenar cadenas alfabéticamente
Encontrar el carácter más pequeño en una contraseña o nombre de usuario
Validar la entrada del usuario (por ejemplo, comprobar si una cadena contiene solo letras mayúsculas)
'''