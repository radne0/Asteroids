import pygame

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
        pygame.draw.polygon(screen, "white", self.triangle(),2)

    def update(self, dt):
        # sub-classes must override
        pass