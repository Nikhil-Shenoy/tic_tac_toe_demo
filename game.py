import pygame

def main():
  pygame.init()
  screen = pygame.display.set_mode((480, 480))
  
  while True:
    screen.fill((0, 0, 0))
    pygame.display.flip()

if __name__ == "__main__":
  main()
