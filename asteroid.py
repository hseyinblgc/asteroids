import pygame
from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    ASTEROID_MIN_RADIUS,
    )
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH
            )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        A1 = Asteroid(
            self.position.x, self.position.y,
            self.radius - ASTEROID_MIN_RADIUS)
        A2 = Asteroid(
            self.position.x, self.position.y,
            self.radius - ASTEROID_MIN_RADIUS)
        A1.velocity = pygame.math.Vector2.rotate(self.velocity, angle)*1.2
        A2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle)*1.2
