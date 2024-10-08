import pygame
from circleshape import CircleShape
import constants
class Shot(CircleShape):
    
    def __init__(self, x, y, direction):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity= direction * PLAYER_SHOOT_SPEED
        
    
    def update(self,dt):
        self.position += self.velocity * dt