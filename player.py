import pygame
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        print(f"Player.__init__ called with: x={x}, y={y}")
        super().__init__(x, y, PLAYER_)
        rotation = 0

    # in the player class
def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

def draw(self, screen):
    print(f"Drawing player at position: {self.position}")
    pygame.draw.polygon(screen, "white", self.triangle(), 2)