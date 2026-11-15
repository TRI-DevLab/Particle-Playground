# This file contains the basic details of how a particle is created 

import pygame 
import random 
import config


class Particle:
    def __init__(self, x, y):

        # Position 
        self.x = x
        self.y = y

        # Velocity
        self.vx = 2
        self.vy = 2

        # Appearance
        self.radius = 5

        self.color = config.PARTICLE_DEFAULT_COLOR


    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )
    
