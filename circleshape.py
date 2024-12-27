import pygame
from constants import *

# Base class for game objects
# game objects represents as circle with a center position, radius and velocity (vector in the direction of movement.)
# from boot.dev
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):

        verts = self.triangle()
        if (SHOW_PLAYER_HB):
            pygame.draw.circle(screen, "red"  ,  (self.position.x,self.position.y)   ,self.radius,3)      
            pygame.draw.circle(screen,"blue" ,   (self.position.x,self.position.y)   ,10) 
            pygame.draw.circle(screen,"green" ,   verts[0],10) 
            pygame.draw.circle(screen,"teal" ,   verts[1],10)                         
            pygame.draw.circle(screen,"orange" ,  verts[2],10) 

        pygame.draw.polygon(screen, "white", verts,3)


    def update(self, dt):
        # sub-classes must override
        pass