import pygame
from constants import *
def game_start():
    print("Starting asteroids!")


game_start()
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()