import pygame
from circleshape import CircleShape
from constants import *
  # Add this at the top of your file
print(dir())  # This will print all variables in the current namespace

class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__(self, x, y, direction):
        super().__init__(x, y, self.SHOT_RADIUS)
        self.velocity = direction * PLAYER_SHOOT_SPEED
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)