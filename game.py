import pprint
import os, sys
import board, logic
import copy

import pygame
import math, random

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

def display_search(screen, node, tree, boardimage, ximage, oimage):
  tree.clearvisit()
  # make the second part of the screen the display part
  subframe = pygame.Surface((480, 480))
  subframe.fill((255, 255, 255))
  queue = []
  queue.append(node)
  pos = []
  pos.append((240,240))
  to = []
  to.append((240,240))
  length = []
  length.append(120)
  node.visited = True
  # starting from the back
  while len(queue) > 0:
    curr = queue.pop()
    p = pos.pop()
    t = to.pop()
    l = length.pop()
    pygame.draw.circle(subframe, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), p, 1, 0)
    pygame.draw.line(subframe, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), p, t)
    if len(curr.children) > 0 and l > 2:
      diff = math.pi * 2 / len(curr.children)
      i = 0
      for child in curr.children:
        if child.visited:
          continue
        child.visited = True
        queue.append(child)
        angle = i * diff
        pos.append((int(p[0] + math.cos(angle) * l), int(p[1] + math.sin(angle) * l)))
        to.append(p)
        length.append(l / 2.0)
        i += 1
 
    screen.blit(subframe, pygame.Rect((480, 0), (480, 480)))
    currnode.display(screen, boardimage, ximage, oimage)
    pygame.display.flip()
  return subframe

if __name__ == "__main__":
  #print "Welcome to Tic-Tac-Toe!\nWe\'ll fill in more description about usage here"

  pygame.init()
  screen = pygame.display.set_mode((960, 480),pygame.FULLSCREEN)
  clock = pygame.time.Clock()
  mousedown = False
  mousepos = (0, 0)

  won = False
  won_by_user = False
  won_by_ai = False
  stalemate = False

  config = [['u' for j in range(3)] for i in range(3)]
  boardimage = pygame.image.load("img/board2.png").convert_alpha()
  ximage = pygame.image.load("img/x2.png").convert_alpha()
  oimage = pygame.image.load("img/o2.png").convert_alpha()

  # AI
  tree = board.Board(config)
  player = "x"
  ai = "o"
  logic.generate_tree(tree, player)
  logic.determine_depth(tree, 0)
  best_val, path = logic.minimax(tree, logic.max_depth, player)
  currnode = tree
  turn = player

  while True:
    currnode = tree # restart
    subframe = pygame.Surface((480, 480))
    subframe.fill((255, 255, 255))
    turn = player

    while not won or not stalemate:
      #print "This is the current state of the board:\n"
      screen.fill((255, 255, 255))

      # get the input from mouse input
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit(1)
        elif event.type == pygame.MOUSEBUTTONDOWN and turn == player:
          mousedown = True
          mousepos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
          mousedown = False
          mousepos = event.pos
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit(1)

      if turn == player:
      # get the id of the clicked square and place it
        if mousedown:
          squareid = getsquareid(mousepos)
          if squareid != -1 and currnode.get_value(squareid % 3, squareid / 3) == 'u':
            # move node
            for child in currnode.children:
              if child.get_value(squareid % 3, squareid / 3) == player:
                currnode = child
                break
            turn = ai
          mousedown = False
  
        # display the state of the game
        screen.blit(subframe, pygame.Rect((480, 0), (480, 480)))
        currnode.display(screen, boardimage, ximage, oimage)
        pygame.display.flip()
        clock.tick(30)
  
        win = logic.is_win(currnode)
        full = logic.is_full(currnode)
        if win:
          won_by_user = True
          break
        if not win and full:
          stalemate = True
          break

      else:
        subframe = display_search(screen, currnode, tree, boardimage, ximage, oimage)
        # AI makes move here. We will write this using our knowledge of adversarial search.
        currnode = currnode.minimax_node

        # display the state of the game
        screen.blit(subframe, pygame.Rect((480, 0), (480, 480)))
        currnode.display(screen, boardimage, ximage, oimage)
        pygame.display.flip()
        clock.tick(30)
  
        win = logic.is_win(currnode)
        full = logic.is_full(currnode)
        if win:
          won_by_ai = True
          break
        if not win and full:
          stalemate = True
          break
      
        turn = player

    if won_by_user:
      print "Congratulations! You win!"
    elif won_by_ai:
      print "Sorry. The AI won this round"
    elif stalemate:
      print "You played the AI to a stalemate"
