import pygame

class Board:

	def __init__(self,config):
		self.utility = 0
		self.config = config
		self.children = list()
		self.minimax_value = 0
		self.minimax_node = None

		self.visited = False

	def clearvisit(self):
		self.visited = False
		for child in self.children:
			child.clearvisit()

	def get_value(self,x,y):
		return self.config[x][y]

	def set_value(self,x,y,val):
		self.config[x][y] = val

	def display(self, screen, boardimage, ximage, oimage):
		size = len(self.config)

		screen.blit(boardimage, boardimage.get_rect())
		for i in range(size):
			for j in range(size):
				if self.config[i][j] == "x":
					screen.blit(ximage, pygame.Rect((j * 160 + 20, i * 160 + 20), (120, 120)))
				elif self.config[i][j] == "o":
					screen.blit(oimage, pygame.Rect((j * 160 + 20, i * 160 + 20), (120, 120)))
