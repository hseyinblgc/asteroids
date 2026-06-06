import pygame
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from logger import log_state


def start_game(screen):
    clocker = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clocker.tick(60) / 1000


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(
        f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}"
    )
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    start_game(screen)


if __name__ == "__main__":
    main()
