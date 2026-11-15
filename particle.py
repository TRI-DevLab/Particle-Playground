# This file contains the basic details of how a particle is created 

import pygame 
import random 


class Particle:
    def __init__(self, x, y):

        # Position 
        self.x = x
        self.y = y

        # Velocity
        self.vx = random.uniform(-3, -3)            
        self.vy = random.uniform(-3, -3)

        # Appearance
        self.radius = random.randint(3, 8)

        self.color = (
            random.randint(80, 255),
            random.randint(80, 255),
            random.randint(80, 255)
        )


    def draw(self, screen):
        # integer coordinates for the center
        center = (int(self.x), int(self.y))

        pygame.draw.circle(
            screen,
            self.color,
            center,
            self.radius
        )

    def update(self):

        gravity = 0.10      # This affects vertical velocity

        self.vy += gravity      # gravity is added to the velocity 

        # position is updated by the added uniform velocity
        self.x += self.vx
        self.y += self.vy
    
