from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

# initial code from boot.dev
# rewritten slightly
    def triangle(self):

        #orthonormal basis.  unit vector in direction of ship  and one perpendicular to that.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)                       #<-- unit vector in direction of ship
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90)                    #<-- perpendicular to ship


        # front of ship placed on the circle away from the center in the direction the ship if facing
        # back of ship vertices:  start by placing on the circle away from the center in the direction OPPOSITE from the direction of ship
        # shift along the perpendicular "right" or "left" to a desired thickness.   
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right*self.radius/1.5
        c = self.position - forward * self.radius + right*self.radius/1.5
        return [a, b, c]