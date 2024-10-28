import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity= pygame.Vector2(0,0)
       

    def draw(self, surface):
        print(f"Drawing asteroid at {self.position} with radius {self.radius}")
        pygame.draw.circle(surface,"White", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self,dt):
        old_pos = self.position.copy()
        self.position += self.velocity*dt 
        print(f"Asteroid moved from {old_pos} to {self.position}")
        

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2


if __name__ == "__main__":
    print("Asteroid module loaded successfully")