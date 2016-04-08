import pygame

class Board:

	def __init__(self,config):
		self.utility = 0
		self.config = config
		self.children = list()
		self.boardimage = pygame.image.load("img/board2.png").convert_alpha()
		self.ximage = pygame.image.load("img/x2.png").convert_alpha()
		self.oimage = pygame.image.load("img/o2.png").convert_alpha()

	def get_value(self,x,y):
		return self.config[x][y]

	def set_value(self,x,y,val):
		self.config[x][y] = val

	def display(self, screen):
		size = len(self.config)

		screen.blit(self.boardimage, self.boardimage.get_rect())
		for i in range(size):
			for j in range(size):
				if self.config[i][j] == 1:
					screen.blit(self.ximage, pygame.Rect((j * 160 + 20, i * 160 + 20), (120, 120)))
				elif self.config[i][j] == -1:
					screen.blit(self.oimage, pygame.Rect((j * 160 + 20, i * 160 + 20), (120, 120)))

	def win(self):
		'''
			Return:
				0 = not won
				1 = won by user
				2 = won by ai
		'''

		b = self.config

		if b[0][0] == b[0][1] == b[0][2]:
			if b[0][0] == 'x':
				return 1
			elif b[0][0] == 'u':
				return 2
		elif b[1][0] == b[1][1] == b[1][2]:
			if b[1][0] == 'x':
				return 1
			elif b[1][0] == 'u':
				return 2
		elif b[2][0] == b[2][1] == b[2][2]:
			if b[2][0] == 'x':
				return 1
			elif b[2][0] == 'u':
				return 2
		elif b[0][0] == b[1][0] == b[2][0]:
			if b[0][0] == 'x':
				return 1
			elif b[0][0] == 'u':
				return 2
		elif b[0][1] == b[1][1] == b[2][1]:
			if b[0][1] == 'x':
				return 1
			elif b[0][1] == 'u':
				return 2
		elif b[0][2] == b[1][2] == b[2][2]:
			if b[0][2] == 'x':
				return 1
			elif b[0][2] == 'u':
				return 2
		elif b[0][0] == b[1][1] == b[2][2]:
			if b[0][0] == 'x':
				return 1
			elif b[0][0] == 'u':
				return 2
		elif b[0][2] == b[1][1] == b[2][0]:
			if b[0][2] == 'x':
				return 1
			elif b[0][2] == 'u':
				return 2
		else:
			return 0

	def stalemate(self):
		'Insert logic for stalemate conditions'
