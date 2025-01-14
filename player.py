from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.score = 0

    def addpoints(self,val):
        self.score += val


    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self,dt ):
        forward = pygame.Vector2(0,1).rotate(self.rotation)               # unit vector in movement direction
        self.position += PLAYER_SPEED*dt*forward                          # scale based on player speed and time since last update.

    # from boot.dev:   check for key press..  
    def update(self, dt):
        if (self.timer > 0): self.timer -= dt
        
        # controls...
        keys = pygame.key.get_pressed()        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:   
            self.move(dt)
        if keys[pygame.K_s]:   
            self.move(-dt)     
        if keys[pygame.K_SPACE]:
            self.shoot(dt)       
        

    def shoot(self,dt):
        if (self.timer <= 0):
            self.timer = PLAYER_SHOT_COOLDOWN
            bullet = Shot(self.position.x,self.position.y,SHOT_RADIUS)
            direction = pygame.Vector2(0,1).rotate(self.rotation)
            bullet.position = bullet.position + (self.radius+10)*direction
            bullet.velocity = direction*PLAYER_SHOOT_SPEED
        else:
            pass
    

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