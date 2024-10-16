import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__(self, x, y, direction):
        super().__init__(x, y, self.SHOT_RADIUS)
        self.velocity = direction * PLAYER_SHOOT_SPEED
    

    def update(self, dt):
        super().update(dt)
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    