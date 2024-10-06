import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from circleshape import *

def game_start():
    print("Starting asteroids!")


game_start()
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    print("Starting main function")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()    
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
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
        print("About to draw player")
        player.draw(screen)
        print("Player drawn")
        pygame.display.flip()
        print("Display updated")
        clock.tick(60)
        dt = clock.tick(60) / 1000.0
    
    
    print("Exiting main function")    


if __name__ == "__main__":
    main()