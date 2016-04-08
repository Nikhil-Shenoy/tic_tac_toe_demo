import pprint
import board
import copy

def is_win(b):

		config = b.config

		if config[0][0] == config[0][1] == config[0][2]:
			if config[0][0] == "x" or config[0][0] == "o":
				return True
		if config[1][0] == config[1][1] == config[1][2]:
			if config[1][0] == "x" or config[1][0] == "o":
				return True
		if config[2][0] == config[2][1] == config[2][2]:
			if config[2][0] == "x" or config[2][0] == "o":
				return True
		if config[0][0] == config[1][0] == config[2][0]:
			if config[0][0] == "x" or config[0][0] == "o":
				return True
		if config[0][1] == config[1][1] == config[2][1]:
			if config[0][1] == "x" or config[0][1] == "o":
				return True
		if config[0][2] == config[1][2] == config[2][2]:
			if config[0][2] == "x" or config[0][2] == "o":
				return True
		if config[0][0] == config[1][1] == config[2][2]:
			if config[0][0] == "x" or config[0][0] == "o":
				return True
		if config[0][2] == config[1][1] == config[2][0]:
			if config[0][2] == "x" or config[0][2] == "o":
				return True
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
			if b.config[i][j] == 'u':
				spaces.append((i,j))

	return spaces

def generate_tree(b,player):

	if is_win(b): # Win
		return
	elif not is_win(b) and is_full(b): # Stalemate
		return

	open_spaces = find_open_spaces(b)

	for space in open_spaces:
		child = board.Board(copy.deepcopy(b.config))
		# child.display()
		# print '\n\n'
		child.set_value(space[0],space[1],player)
		# child.display()
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


if __name__ == '__main__':

	pp = pprint.PrettyPrinter()

	root = [['u' for i in range(3)] for j in range(3)]
	player = 'x'

	tree = board.Board(root)
	tree.display()

	generate_tree(tree,player)

