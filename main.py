import pygame
import sys
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def game_start():
    print("Starting asteroids!")


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable,drawable)
asteroid_group = pygame.sprite.Group()
Shot_group = pygame.sprite.Group()
Asteroid.containers = (asteroid_group, updatable, drawable)
print("Asteroid class imported successfully")
AsteroidField.containers = (updatable,)
asteroid_field = AsteroidField()
Shot.containers = (Shot_group,updatable,drawable)
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    print("Starting main function")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()    
    dt = 0

    
    try:
        print(f"Attempting to create Player with: x={SCREEN_WIDTH/2}, y={SCREEN_HEIGHT/2}")
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        print("Player created successfully")
    except Exception as e:
        print(f"Error creating Player: {e}")
        return

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroid_group:
            if player.collisions(asteroid):
                print("Game Over")
                sys.exit()
        for shot in list(Shot_group):
            for asteroid in list(asteroid_group):
                if shot.collide_with(asteroid):
                    print("Collision detected!")        
                    shot.kill()
                    new_asteroids = asteroid.split()
                    print(f"Split returned: {new_asteroids}")
                    if new_asteroids:
                        for new_ast in new_asteroids:
                            print(f"New asteroid created at {new_ast.position} with radius {new_ast.radius}")
                        asteroid_group.add(new_asteroids)
                        print(f"Asteroid group size after adding: {len(asteroid_group)}")
                    break

        for sprite in drawable:
            
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
    
    
    print("Exiting main function")    


if __name__ == "__main__":
    main()