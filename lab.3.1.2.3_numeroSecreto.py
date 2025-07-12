numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
muggle = int (input("Ingrese un numero: "))
while muggle != 0:
    if muggle == numeroSecreto:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break                
    else:
        print("""
        ¡Ja, ja! ¡Estas atrapado en mi ciclo.
        Ingresa de nuevo un numero
        """)
        muggle = int (input("Ingrese un numero: "))
        
        
    