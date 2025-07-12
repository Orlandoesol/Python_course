print("\n-----item-1------\n")
print("el operador capaz de comprobar si dos valores no son iguales se codifica como: !=")

x = 1
y = 2
if x != y:
    print(True)  
else: print("Error")
""" elif x<>y:
    print(True) error de sintaxis 
elif x not == y:
    print(True)"""

print("\n-----item-2------\n")
#Cuantos asteriscos imprime?
#Imprime 2
i = 2 
while i >= 0:
    print("*")
    i -= 2
print("\n-----item-3------\n")
#Cuantos # se enviaran a la consola?
#Envia dos
for i in range(-1,1):
    print("#")
print("\n-----item-4------\n")
#Que valor se asigna a la variable x?
#True
z = 10
y = 0
x = z > y or z == y
# x = 10 > 0 o 10 == 0
print(x,"\n",y,"\n",z,"\n")
print("\n-----item-5-----\n")
#Cual es la salida del siguiente codigo?
#[3, 1, 1]; que el elemento que hay en la posicion -1 (ultima) de la lista sea igual al que hay en la posicion -2(1)
lst = [3, 1, -1]
lst[-1] = lst[-2]
print(lst)
print("\n-----item-6-----\n")
#La segunda asignación:
#vals[1,2,2], no cambia la longitud de la lista
vals = [0,1,2]
vals[0] , vals[1] = vals[1],vals[2]
print(vals)
print("\n-----item-7-----\n")
#Echa un vistazo al fragmento y elige la afirmación verdadera de las siguientes:
#nums y vals tienen la misma longitud
nums = []
vals = nums
vals.append(1)
print(len(vals),"\n",len(nums))
print(vals,"\n",nums)
print("\n-----item-8-----\n")
#Echa un vistazo al fragmento y elige la afirmación verdadera de las siguientes:
#vlas es mas largo que nums
nums = []
vals = nums[:]
vals.append(1)
print("vals",len(vals),"\n","nums",len(nums))
print(vals,"\n",nums)
print("\n-----item-9-----\n")
#Cuantos elementos contiene la lista lst?
#2 elementos
lst = [0 for i in range(1,3)]
print("la lista lst tiene: ",len(lst))
print("\n-----item-10-----\n")
#Cual es la salida del siguiente fragmento de codigo?
#la salida es 0. 
lst = [0,1,2,3]
x = 1
for elem in lst:
    x *= elem # x arranca en 1 y se multiplica por 0, el primer elemento de lalista y x toma ese valor por lo tanto toda lista queda en 0
print(x)