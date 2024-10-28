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
        print(f"Splitting asteroid at position {self.position} with radius {self.radius}")
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("Asteroid too small to split")
            self.kill()
            return []

        new_size = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)
        offset = self.radius / 2
        new_position1 = self.position + vector_1 * offset
        new_position2 = self.position + vector_2 * offset
        new_asteroid1 = Asteroid(new_position1.x, new_position1.y, new_size)
        new_asteroid2 = Asteroid(new_position2.x, new_position2.y, new_size)
        new_asteroid1.velocity = vector_1 * 1.2
        new_asteroid2.velocity = vector_2 * 1.2
        print(f"New asteroids created: {new_asteroid1}, {new_asteroid2}")
        self.kill()
        return [new_asteroid1, new_asteroid2]

if __name__ == "__main__":
    print("Asteroid module loaded successfully")