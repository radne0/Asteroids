import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "green", (self.position.x,self.position.y),SHOT_RADIUS)

    def update(self,dt):
        self.position =self.position + dt*self.velocity