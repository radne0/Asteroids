from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self,dt ):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += PLAYER_MOVE_SPEED*dt*forward  

    # from boot.dev:   check for key press..  
    def update(self, dt):
        keys = pygame.key.get_pressed()
        print(f"A: {keys[pygame.K_a]}, D: {keys[pygame.K_d]}, W: {keys[pygame.K_w]}")
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:   
            self.move(dt)

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