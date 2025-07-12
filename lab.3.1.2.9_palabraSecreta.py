palabraSecreta = "chupacabra"
palabra = input("Ingrese la palabra secreta:")

while palabra != False:
    if palabra == palabraSecreta:
        print("¡Has dejado el ciclo con éxito.")
        break
    else:
        print("""
        ¡Intentalo una vez mas!
        """)
        palabra = input("Ingrese la palabra secreta:")