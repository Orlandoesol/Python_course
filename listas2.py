vehicles_one = ['coche', 'bicicleta', 'motor']
print(vehicles_one) # output: ['coche', 'bicicleta', 'motor']

vehicles_two = vehicles_one
print(vehicles_two)
del vehicles_one[0] # elimina 'coche'
print(vehicles_two) # output: ['bicicleta', 'motor']

#Copiar listas
colors = ['rojo', 'verde', 'naranja']
print(colors)
copy_whole_colors = colors[:]  # copia la lista entera
print(copy_whole_colors) # output: ['rojo', 'verde', 'naran
copy_part_colors = colors[0:2]  # copia parte de la lista
print(copy_part_colors)

#Indices negativos
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # output: ['C', 'D']

#Rebanadas de lista; Los parámetros start y end son opcionales al partir en rebanadas una lista: list[start:end]
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # output: [3, 4, 5]
print(slice_two)  # output: [1, 2]
print(slice_three)  # output: [4, 5]

#Eiminar rebanadas
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # output: [3, 4, 5]

del my_list[:]
print(my_list)  # elimina el contenido de la lista, genera: []

#Comprobar existencias
my_list = ["A", "B", 1, 2]
 
print("A" in my_list)  # output: True
print("C" not in my_list)  # output: True
print(2 not in my_list)  # output: False

#Quiz
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
#list_2 = list_1[:]
#list_3 = list_2[:]
 
del list_1[0]
del list_2[0]
#del list_2
#del list_2[:]
 
print(list_3)

my_list2 = [1, 2, "in", True, "ABC"]

#Inserta in o not in en lugar de ??? para que el código genere el resultado esperado. 
print(1 in my_list2)  # output True
print("A" not in my_list2)  # output True
print(3 not in my_list2)  # output True
print(False in my_list2)  # output False