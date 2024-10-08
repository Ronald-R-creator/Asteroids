import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape
from shot import Shot

print(f"SHOT_RADIUS in Player: {SHOT_RADIUS}")  # This will work now

class Player(CircleShape):
    def __init__(self, x, y):
        print(f"Player.__init__ called with: x={x}, y={y}")
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
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
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, 2)
        
    
    def Rotate(self,dt):
       return PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotation += self.Rotate(dt)
        if keys[pygame.K_a]:
            self.rotation -= self.Rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt,1)
        if keys[pygame.K_s]:
            self.move(dt,-1)
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        if keys[pygame.K_SPACE] and self.shot_cooldown <= 0:
            self.shoot()
            self.shot_cooldown = SHOT_COOLDOWN 
    
    def move(self,dt,direction=1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction
    
    def shoot(self):
        shot_position = self.position.copy()
        shot_direction = pygame.Vector2(0, -1).rotate(-self.rotation)
        fired_shot= Shot(shot_position.x,shot_position.y,shot_direction)
        
