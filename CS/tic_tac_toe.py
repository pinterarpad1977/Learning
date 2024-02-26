board = {
	1 : [' ', ' ', ' '],
	2 : [' ', ' ', ' '],
	3 : [' ', ' ', ' ']
}


def get_x_move():
	while True:
		try:
			line = int(input('X moves - input line: '))
			column = int(input('X moves - input column: '))
			position = board[line][column-1]
			if position == ' ':
				board[line][column-1] = 'X'
				return True
			else:
				print('You cannot move there')
		except ValueError:
			print('Invalid input, must be a number')
		except KeyError:
			print('Invalid line, check position')
		except IndexError:
			print('Invalid column, check position')

def print_board(board):
	print(' \\  1    2    3')
	for key, value in board.items():
		print(key,value)


def get_o_move():
	while True:
		try:
			line = int(input('O moves - input line: '))
			column = int(input('O moves - input column: '))
			position = board[line][column-1]
			if position == ' ':
				board[line][column-1] = 'O'
				return True
			else:
				print('You cannot move there')
		except ValueError:
			print('Invalid input, must be a number')
		except KeyError:
			print('Invalid line, check position')
		except IndexError:
			print('Invalid column, check position')

		

def print_board(board):
	print(' \\  1    2    3')
	for key, value in board.items():
		print(key,value)
print_board(board)

get_x_move()

print_board(board)

get_o_move()

print_board(board)
