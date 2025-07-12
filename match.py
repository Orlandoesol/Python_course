# match, lo que en otro lenguaje se conoce como "switch"
while True:

    score = int(input("Introduce tu nota, entre 1 y 10: "))

    if score < 1 or score > 10:
        print("Nota fuera de rango")
    else:
        match score:
            case 10:
                print("Perfecto, has sacado un 10")
            case 9 | 8:
                print(f"Muy bien, has aprobado con {score}")
            case 7 | 6:
                print(f"Aprobaste, has sacado un {score}")
            case _:
                print(f"Has sacado un {score}, necesitas mejorar; No has aprobado")
