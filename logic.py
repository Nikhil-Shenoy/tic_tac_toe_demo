import pprint
import board
import copy
import pygame

'''
Assumptions:
	x is human
	o is ai

	o is maximizing
	x is minimizing
'''

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
		child.set_value(space[0],space[1],player)
		child.utility = heuristic(child.config,player)
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

max_depth = 0
def determine_depth(node,depth):
	global max_depth

	if not node.children:
		if depth > max_depth:
			max_depth = depth

		return
	else:
		for child in node.children:
			determine_depth(child,depth+1)

def heuristic(conf,player):
	'''
		Three in a row = +/- 100
		Two in a row = +- 10
		One piece = +/- 1
	'''

	# 8 possible lines
	r0 = conf[0]
	r1 = conf[1]
	r2 = conf[2]
	c0 = [conf[0][0],conf[1][0],conf[2][0]]
	c1 = [conf[0][1],conf[1][1],conf[2][1]]
	c2 = [conf[0][2],conf[1][2],conf[2][2]]
	d1 = [conf[0][0],conf[1][1],conf[2][2]]
	d2 = [conf[2][0],conf[1][1],conf[0][2]]

	lines = [r0,r1,r2,c0,c1,c2,d1,d2]
	score = 0
	for line in lines:
		count = 0
		for element in line:
			if element == player:
				count += 1
		
		if count == 3:
			score += 100
		elif count == 2:
			if line[0] == line[1] or line[1] == line[2]:
				score += 10
			else:
				score += 2
		elif count == 1:
			score += 1
	
	if player == 'o':
		return score
	elif player == 'x':
		return (-1) * score

def minimax(node,depth,player):
	if depth == 0 or not node.children:
		return node.utility, [node]

	if player == 'o':
		best_value = -1000000
		path = []
		for child in node.children:
			v, p = minimax(child,depth-1,'x')
			if v > best_value:
				best_value = v
				path = p

		node.minimax_value = best_value
		node.minimax_node = path[0]
		return best_value, [node] + path
	else:
		best_value = 1000000
		path = []
		for child in node.children:
			v, p = minimax(child,depth-1,'o')
			if v < best_value:
				best_value = v
				path = p

		node.minimax_value = best_value
		node.minimax_node = path[0]
		return best_value, [node] + path


if __name__ == '__main__':

	pygame.init()
	screen = pygame.display.set_mode((1,1))
	pp = pprint.PrettyPrinter()

	root = [['u' for i in range(3)] for j in range(3)]
	player = 'x'

	tree = board.Board(root)

	generate_tree(tree,player)

	determine_depth(tree,0)
	# print "The maximum depth is {0}".format(max_depth)

	best_val, path = minimax(tree,max_depth,player)
	vals = list()
	for child in tree.children:
		vals.append(child.minimax_value)	

	print "The minimax values are {0}".format(vals)
	print "The best minimax value is {0}".format(best_val)
	
