import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH 
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")
    pygame.display.flip()

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        for event in pygame.event.get():
            log_state()
            if event.type == pygame.QUIT:
                return
            dt = clock.tick(60) / 1000.0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
