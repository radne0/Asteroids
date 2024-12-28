from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self,dt ):
        forward = pygame.Vector2(0,1).rotate(self.rotation)               # unit vector in movement direction
        self.position += PLAYER_SPEED*dt*forward                          # scale based on player speed and time since last update.

    # from boot.dev:   check for key press..  
    def update(self, dt):
        keys = pygame.key.get_pressed()
        #print(f"A: {keys[pygame.K_a]}, D: {keys[pygame.K_d]}, W: {keys[pygame.K_w]},S: {keys[pygame.K_s]}")
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:   
            self.move(dt)
        if keys[pygame.K_s]:   
            self.move(-dt)     
        if keys[pygame.K_SPACE]:
            self.shoot()       

    def shoot(self):
        bullet = Shot(self.position.x,self.position.y,SHOT_RADIUS)
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        bullet.position = bullet.position + (self.radius+10)*direction
        bullet.velocity = direction*PLAYER_SHOOT_SPEED

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