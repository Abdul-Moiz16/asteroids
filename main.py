import pygame
from player import Player
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH 
from logger import log_state

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen.fill("black")

        for event in pygame.event.get():
            log_state()
            if event.type == pygame.QUIT:
                return
        for update in updatable:
            update.update(dt)
        
        for draw in drawable:
            draw.draw(screen)
        dt = clock.tick(60) / 1000.0
        pygame.display.flip()


if __name__ == "__main__":
    main()
