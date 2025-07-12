""" 
Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. Hay 20 habitaciones en cada piso. 
Para esto, necesitas un arreglo que pueda recopilar y procesar información sobre las habitaciones ocupadas/libres.

Primer paso - El tipo de elementos del arreglo. En este caso, sería un valor Booleano (True/False).

Paso dos - análisis de la situación. Resume la información disponible: tres edificios, 15 pisos, 20 habitaciones.

 """
#habitaciones = pisos = edificios
#rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms = [[[False for r in range(10)] for f in range(2)] for t in range(3)]

#edif-piso-hab
rooms[1][1][8] = True#ocupado
print(rooms)
rooms[0][0][1] = False#desocupado
print(rooms)

vacancy = 0

for room_number in range(10):
    if not rooms[0][1][room_number]:
        vacancy += 1



