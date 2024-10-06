import pygame
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        print(f"Player.__init__ called with: x={x}, y={y}")
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        print(f"Player initialized with position: {self.position}, radius: {self.radius}")

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        print(f"Triangle points: a={a}, b={b}, c={c}")
        return [a, b, c]

    def draw(self, screen):
        print(f"Drawing player at position: {self.position}")
        points = self.triangle()
        print(f"Drawing polygon with points: {points}")
        pygame.draw.polygon(screen, "white", points, 2)
        print("Polygon drawn")
    
    def Rotate(self,dt):
       return PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation += self.Rotate(dt)
        if keys[pygame.K_d]:
            self.rotation -= self.Rotate(dt)