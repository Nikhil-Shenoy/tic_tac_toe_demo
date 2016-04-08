import pprint
import os, sys
import board, logic

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

if __name__ == "__main__":
  #print "Welcome to Tic-Tac-Toe!\nWe\'ll fill in more description about usage here"

  pygame.init()
  screen = pygame.display.set_mode((480, 480))
  clock = pygame.time.Clock()
  mousedown = False
  mousepos = (0, 0)

  won = False
  won_by_user = False
  won_by_ai = False
  stalemate = False

  config = [['u' for j in range(3)] for i in range(3)]
  boardgame = board.Board(config)

  while not won or not stalemate:
    #print "This is the current state of the board:\n"
    screen.fill((255, 255, 255))

    # get the input from mouse input
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(1)
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
        mousepos = event.pos
      elif event.type == pygame.MOUSEBUTTONUP:
        mousedown = False
        mousepos = event.pos

    # get the id of the clicked square and place it
    if mousedown:
      squareid = getsquareid(mousepos)
      if squareid != -1 and boardgame.get_value(squareid % 3, squareid / 3) == 'u':
        boardgame.set_value(squareid % 3, squareid / 3, 'x')
      mousedown = False

    # display the state of the game
    boardgame.display(screen)
    boardgame.display(screen)
    pygame.display.flip()
    clock.tick(30)

    win = logic.is_win(boardgame)
    full = logic.is_full(boardgame)
    if win:
      won_by_user = True
      break
    if not win and full:
      stalemate = True
      break
    
    # AI makes move here. We will write this using our knowledge of adversarial search.

    # display the state of the game
    boardgame.display(screen)
    boardgame.display(screen)
    pygame.display.flip()
    clock.tick(30)

    win = logic.is_win(boardgame)
    full = logic.is_full(boardgame)
    if win:
      won_by_ai = True
      break
    if not win and full:
      stalemate = True
      break

  if won_by_user:
    print "Congratulations! You win!"
  elif won_by_ai:
    print "Sorry. The AI won this round"
  elif stalemate:
    print "You played the AI to a stalemate"
