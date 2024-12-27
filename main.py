import pygame
from constants import * 
from time import sleep

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while(True):
        screen.fill( (255,255,255)  )
        pygame.display.flip()
    





# only excute when this file is ran directly, not imported.
if __name__ == "__main__":
    main()
