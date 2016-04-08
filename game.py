import pygame

def main():
  pygame.init()
  screen = pygame.display.set_mode((480, 480))
  
  ## initial variables
  mousedown = False
  mousepos = (0, 0)

  while True:
    
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

    if mousedown:
      print mousepos
    screen.fill((0, 0, 0))
    pygame.display.flip()

if __name__ == "__main__":
  main()
