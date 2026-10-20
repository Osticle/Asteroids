from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
    
    def split(self) -> None:
        pygame.sprite.Sprite.kill(self)     # kill itself
        
        # check if the asteroid can split or not
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            rotated_vector_1 = self.velocity.rotate(new_angle)
            rotated_vector_2 = self.velocity.rotate(-(new_angle))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

            asteroid_1.velocity = rotated_vector_1 * 1.2
            asteroid_2.velocity = rotated_vector_2 * 1.2