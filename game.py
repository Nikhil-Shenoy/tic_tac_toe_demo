import pygame

def within(x, a, b):
  return a <= x and x <= b

def getsquareid(pos):
  # we know the height to be 480 and width to be 480
  # 480 / 3 = 160
  realx = pos[0] / 160
  realy = pos[1] / 160
  inx = pos[0] % 160
  iny = pos[1] % 160
  if not within(inx, 20, 140) or not within(iny, 20, 140):
    return -1
  # column major order
  return realx * 3 + realy

def main():
  pygame.init()
  screen = pygame.display.set_mode((480, 480))
  clock = pygame.time.Clock()
  
  ## initial variables
  mousedown = False
  mousepos = (0, 0)
  boardimage = pygame.image.load("img/board2.png").convert_alpha()
  ximage = pygame.image.load("img/x2.png").convert_alpha()
  oimage = pygame.image.load("img/o2.png").convert_alpha()
  board = [[ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ]]
  turn = 1

  while True:
    screen.fill((255, 255, 255))
    
    # event handler
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
        mousepos = event.pos
      elif event.type == pygame.MOUSEBUTTONUP:
        mousedown = False
        mousepos = event.pos

    # get the id of the clicked square and place it
    if mousedown:
      squareid = getsquareid(mousepos)
      if squareid != -1 and board[squareid % 3][squareid / 3] == 0:
        board[squareid % 3][squareid / 3] = 1
      mousedown = False

    # draw board
    screen.blit(boardimage, boardimage.get_rect())
    # draw the squares
    for i in range(9):
      xoid = board[i%3][i/3]
      if xoid == 1:
        screen.blit(ximage, pygame.Rect((i/3*160 + 20, i%3*160 + 20), (120, 120)))
      if xoid == -1:
        screen.blit(oimage, pygame.Rect((i/3*160 + 20, i%3*160 + 20), (120, 120)))
    pygame.display.flip()
    clock.tick(30)

if __name__ == "__main__":
  main()
