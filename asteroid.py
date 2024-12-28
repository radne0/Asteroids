import pygame
from circleshape import CircleShape
from constants import *
import random



# (x,y) center of asteroid
# radius - radius of asteroid
# split - how many times has this asteroid split.
# value - how much is this asteroid worth?  smaller asteroids = more points,  split asteroids more points.

class Asteroid(CircleShape):
    def __init__(self,x,y,radius,state=0):
        super().__init__(x,y,radius)
        self.state = state
        self.value = (ASTEROID_KINDS-(self.radius / ASTEROID_MIN_RADIUS)+1) * 10 #+ self.state*5
        

    def split(self):
        if (self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
            return
        else:
            rangle = random.uniform(20,70)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            vel = self.velocity
            print(f"{self.position.x} :  {self.position.y} : {new_radius} :  {vel}")
            a1 = Asteroid(self.position.x,self.position.y,new_radius,self.state +1)
            a1.velocity = self.velocity.rotate(rangle)*random.uniform(1.1,1.3)       
            a2 = Asteroid(self.position.x,self.position.y,new_radius,self.state+1)
            a2.velocity = self.velocity.rotate(-rangle)*random.uniform(1.1,1.3)
            self.kill()


    def draw(self,screen):
        pygame.draw.circle(screen, "white", (self.position.x,self.position.y),self.radius)

    def update(self,dt):
        self.position += self.velocity*dt
        
