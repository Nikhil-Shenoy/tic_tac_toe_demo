
import board

root = [['u' for i in range(3)] for j in range(3)]

player = 'x'

def is_win(b):

		config = b.config

		if config[0][0] == config[0][1] == config[0][2]:
			return True
		elif config[1][0] == config[1][1] == config[1][2]:
			return True
		elif config[2][0] == config[2][1] == config[2][2]:
			return True
		elif config[0][0] == config[1][0] == config[2][0]:
			return True
		elif config[0][1] == config[1][1] == config[2][1]:
			return True
		elif config[0][2] == config[1][2] == config[2][2]:
			return True
		elif config[0][0] == config[1][1] == config[2][2]:
			return True
		elif config[0][2] == config[1][1] == config[2][0]:
			return True
		else:
			return False

def is_full(b):

	for i in range(3):
		for j in range(3):
			if b.config[i][j] == "u":
				return False

	return True

def find_open_spaces(b):

	spaces = list()

	for i in range(3):
		for j in range(3):
			if b[x][y] == 'u':
				spaces.append((x,y))

	return spaces

tree = board.Board(root)

def generate_tree(b,player):

	if is_win(b): # Win
		return
	elif not is_win(b) and is_full(b): # Stalemate
		return

	open_spaces = find_open_spaces(b)

	for space in open_spaces:
		child = board.Board(b.config)
		child.set_val(space[0],space[1],player)
		b.children.append(child)

	if player == "x":
		opposing_player = "o"
	elif player == "o":
		opposing_player = "x"

	for child in b.children:
		generate_tree(child,opposing_player)


	'''
	for each open space on the current board:
		generate a new board
		mark each new board with the opposing player's piece
		add the new board to the list of children

	for each child
		generate tree

	'''


