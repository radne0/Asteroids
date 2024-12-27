import pygame
from constants import * 
from time import sleep
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize pygame.
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # Framerate handling..
    game_clock = pygame.time.Clock()
    dt = 0

    #Game Loop.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)

    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill( "black"  )
        
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60)/1000                           # time between frame updates.  upper limit capped at 60 FPS  (no faster than ~16.7 ms between updates)
    

# only excute when this file is ran directly, not imported.
if __name__ == "__main__":
    main()
