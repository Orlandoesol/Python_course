EMPTY = "-"
TORRE = "TORRE"
CABALLO = "CABALLO"
ALFIL = "ALFIL"
REINA = "REINA"
REY = "REY"
PEON = "PEON"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][1] = CABALLO
tablero[0][2] = ALFIL
tablero[0][3] = REINA
tablero[0][4] = REY
tablero[0][5] = ALFIL
tablero[0][6] = CABALLO
tablero[0][7] = TORRE
tablero[3][4] = PEON
tablero[4][2] = PEON
tablero[7][0] = TORRE
tablero[7][7] = TORRE

print(tablero)

print("******************")
board = []
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)#

print(board)
print("******************")

board = [[EMPTY for i in range(8)] for j in range(8)]
print(board)
print("******************")


""" i = 2
while i >= 0:
    print("*")
    i -= 2 """

print("******************")

""" for i in range(-1,1):
    print("#") """

print("******************")
""" z = 10
y = 0
x = y < z and z > y or y > z and z < y

print(x) """

""" print("******************")
lst = [3,1,-1]
lst[-1]=lst[-2]
print(lst)

print("******************")
vals = [0,1,2]
vals[0],vals[1]=vals[1],vals[2]
print(vals)

print("******************")
nums = []
vals = nums
vals.append(1)
print(nums,"\n",vals)

print("******************")
nums = []
vals = nums[:]
vals.append(1)
print(nums,"\n",vals)
print(len(nums),len(vals))

print("******************+++++")
lst = [0 for i in range(1,3)]
print(lst)

print("++++++++++++++++")
lst = [0,1,2,3]
x = 1
for elem in lst:
    x *= elem
print(x)
 """
#print("mmmmmmmmmmmm")

""" i = 0
while i <= 5:
    i += 1
    if i%2==0:
        break """
""" for i in range(1):
    print("#")
else: """

""" var = 1
while var < 10:
    print("#")
    var = var << 1 """
""" a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c+d+e) """
""" lst = [1,2,3,4]
print(lst[-3:-2]) """
""" lst = [[0,1,2,3] for i in range (2)]
print(lst[2][0]) """