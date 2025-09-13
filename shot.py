import pygame #type: ignore
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        x, y = int(self.position.x), int(self.position.y) 
        pygame.draw.circle(screen, "white", (x, y), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        