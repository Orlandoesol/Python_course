""" miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# coloca tu código aquí
#
lista2 = set (miLista)
miLista=lista2
print("La lista solo con elementos únicos:")
print(miLista) """
'''
dos = [2 ** i for i in range(8)]
print(dos)
cuadrados = [x ** 2 for x in range(10)]
probabilidades = [x for x in cuadrados if x % 2 != 0] 
print(probabilidades)
'''
""" EMPTY = "-"
TORRE = "TORRE"
tablero  = []
for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append(fila)
tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE

print(tablero) """
Lst_dif = ['Esteban',False, 123, 4.6]
print (Lst_dif)