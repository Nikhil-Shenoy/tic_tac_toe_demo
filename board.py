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
				if self.config[i][j] == "x":
					screen.blit(self.ximage, pygame.Rect((j * 160 + 20, i * 160 + 20), (120, 120)))
				elif self.config[i][j] == "o":
					screen.blit(self.oimage, pygame.Rect((j * 160 + 20, i * 160 + 20), (120, 120)))
