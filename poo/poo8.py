def mi_decorador(func):
    def nueva_funcion(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return nueva_funcion

@mi_decorador
def sumar(a, b):
    """
    docstring:
    Suma dos números y muestra el resultado por pantalla.

    Args:
        a (int or float): Primer número a sumar.
        b (int or float): Segundo número a sumar.

    Returns:
        None
    """
    print(f"La suma es: {a + b}")

sumar(3, 5)

''''
El decorador mi_decorador ahora acepta cualquier cantidad de argumentos usando *args y **kwargs.
La función decorada sumar(a, b) recibe dos números y los suma.
Al llamar sumar(3, 5), se imprime:
"Antes de ejecutar la función"
"La suma es: 8"
'''