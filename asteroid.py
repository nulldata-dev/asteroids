import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (100, 100, 100), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.collided = True
        if self.radius <= ASTEROID_MIN_RADIUS:
            return #asteroid is smallest size
        else:
            random_angle = random.uniform(20, 50)
            asteroid_1_vector = self.velocity
            asteroid_2_vector = self.velocity
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = asteroid_1_vector * 1.2
            asteroid_2.velocity = asteroid_2_vector * 1.2

            asteroid_1.velocity.rotate_ip(random_angle)
            asteroid_2.velocity.rotate_ip(-random_angle)