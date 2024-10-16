import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity= pygame.Vector2(0,0)
       

    def draw(self,screen):
         pygame.draw.circle(screen,"White",self.position,self.radius,2)


    def update(self,dt):
        self.position += self.velocity*dt 

if __name__ == "__main__":
    print("Asteroid module loaded successfully")