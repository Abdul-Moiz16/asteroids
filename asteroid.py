
from typing import override

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt 
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(rand_angle)
            velocity2 = self.velocity.rotate(-rand_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid1.velocity = velocity1 * 1.2 
            asteroid2.velocity = velocity2
            self.kill()
            