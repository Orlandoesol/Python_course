from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+\n|       |       |       |\n|   '+board[0][0]+'   |   '+board[0][1]+'   |   '+board[0][2]+'   |\n|       |       |       |')
    print('+-------+-------+-------+\n|       |       |       |\n|   '+board[1][0]+'   |   '+board[1][1]+'   |   '+board[1][2]+'   |\n|       |       |       |')
    print('+-------+-------+-------+\n|       |       |       |\n|   '+board[2][0]+'   |   '+board[2][1]+'   |   '+board[2][2]+'   |\n|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:

        move = int(input('Enter your move: '))

        if move < 1 or move > 9:
            print('please pick a number in the range of 1 through 9')
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('Sorry, that square is already taken! Please select another square!')
            continue
 
        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == str(move):
                    board[row][column] = '0'
        break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_squares
    free_squares = [ ]

    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == 'X' or board[row][column] == '0':
                pass
            else:
                free_squares.append(([row],[column]))

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True
    else:
        return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:

        row = randrange(3)
        column = randrange(3)

        if([row],[column]) not in free_squares:
           continue
        else:
            board[row][column] = 'X'
            return

board = [[ '1', '2', '3' ],['4', 'X', '6'],[ '7', '8', '9']]
numberOfMoves = 1
player = '0'
machine = 'X'
display_board(board)

while numberOfMoves < 9:

    enter_move(board)
    numberOfMoves += 1
    #DisplayBoard(board)

    if victory_for(board, player) == True:
        print('You won!')
        display_board(board)
        break
    else:
        make_list_of_free_fields(board)
        display_board(board)

    draw_move(board)
    numberOfMoves += 1
    display_board(board)

    if victory_for(board, machine) == True:
        print('The machine won!')
        display_board(board)
        break
    else:
        make_list_of_free_fields(board)

else:
    print('We have a tie! This is a cat\'s game!!!')
        
print('Thank you for playing! please play again soon')

""" 
from random import randrange


def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):
	ok = False	# suposición falsa - la necesitamos para entrar en el bucle
	while not ok:
		move = input("Ingresa tu movimiento: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
		if not ok:
			print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. ingrésalo nuevamente
			continue
		move = int(move) - 1 	# numero de la celda, del 0 al 8
		row = move // 3 	# fila de la celda
		col = move % 3		# columna de la celda
		sign = board[row][col]	# marca el cuadro elegido
		ok = sign not in ['O','X'] 
		if not ok:	# esta ocupado, ingresa una posición nuevamente
			print("¡Cuadro ocupado, ingresa nuevamente!")
			continue
	board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado


def make_list_of_free_fields(board):
	free = []	# la lista esta vacía inicialmente
	for row in range(3): # itera a través de las filas
		for col in range(3): # iitera a través de las columnas
			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
				free.append((row,col)) # si, agrega una nueva tupla a la lista
	return free


def victory_for(board,sgn):
	if sgn == "X":	# ¿Estamos buscando X?
		who = 'me'	# Si, es la maquina
	elif sgn == "O": # ... ¿o estamos buscando O?
		who = 'you'	# Si, es el usuario
	else:
		who = None	# ¡No debemos de caer aquí!
	cross1 = cross2 = True  # para las diagonales
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # revisar la primer diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # revisar la segunda diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
	free = make_list_of_free_fields(board) # crea una lista de los cuadros vacios o libres
	cnt = len(free)
	if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primer 'X' en el centro
free = make_list_of_free_fields(board)
human_turn = True # ¿De quien es turno ahora?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("¡Has ganado!")
elif victor == 'me':
	print("¡He ganado!")
else:
	print("¡Empate!")




 """