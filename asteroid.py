import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        split1 = self.velocity.rotate(random_angle)
        split2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_1.velocity = split1 * 1.2
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_2.velocity = split2 * 1.2



