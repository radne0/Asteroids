import pygame
from circleshape import CircleShape
from constants import *
import random



class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def split(self):
        if (self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
            return
        else:
            rangle = random.uniform(20,70)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            vel = self.velocity
            print(f"{self.position.x} :  {self.position.y} : {new_radius} :  {vel}")
            a1 = Asteroid(self.position.x,self.position.y,new_radius)
            a1.velocity = self.velocity.rotate(rangle)       
            a2 = Asteroid(self.position.x,self.position.y,new_radius)
            a2.velocity = self.velocity.rotate(-rangle)
            self.kill()


    def draw(self,screen):
        pygame.draw.circle(screen, "white", (self.position.x,self.position.y),self.radius)

    def update(self,dt):
        self.position += self.velocity*dt
        
