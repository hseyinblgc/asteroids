import pygame
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from logger import log_state
from player import Player


def start_game(screen):
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    updatable.add(player)
    drawable.add(player)
    clocker = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clocker.tick(60) / 1000
        updatable.update(dt)


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
