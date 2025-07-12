# Ejemplo simple de decorador en Python

def mi_decorador(func):
    def nueva_funcion():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return nueva_funcion

@mi_decorador
def saludar():
    print("¡Hola, mundo!")

# Al llamar saludar(), en realidad se ejecuta nueva_funcion
saludar()

'''
mi_decorador es un decorador que recibe una función, la envuelve y agrega mensajes antes y después de ejecutarla.
El símbolo @mi_decorador se usa para aplicar el decorador a la función saludar.
Al llamar saludar(), se imprime:
"Antes de ejecutar la función"
"¡Hola, mundo!"
"Después de ejecutar la función"

'''