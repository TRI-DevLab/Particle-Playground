# This file contains the basic details of how a particle is created 

import pygame 
import random 
from collections import deque

class Particle:
    def __init__(self, x, y):

        # Position 
        self.x = x
        self.y = y

        # Velocity
        self.vx = random.uniform(-3, 3)            
        self.vy = random.uniform(-3, 3)

        # Appearance
        self.radius = random.randint(3, 8)

        self.color = (
            random.randint(80, 255),
            random.randint(80, 255),
            random.randint(80, 255)
        )

        # Trail
        self.trail = deque(maxlen=15)

        # LifeSpan
        self.max_lifespan = 600
        self.lifespan = self.max_lifespan                 # changes   


    def draw(self, screen):

        # calculate alpha transparency 
        # alpha = max(0, min(225, int(255 * (self.lifespan / self.max_lifespan)) ))

        # creates transparent surface 
        #particle_surface = pygame.Surface(
            #(self.radius * 2, self.radius * 2),
            #pygame.SRCALPHA
        #)

        # Draw particle with alpha 
        # particle_color = (*self.color, alpha)

        #pygame.draw.circle(
            #particle_surface,
            #particle_color,
            #(self.radius, self.radius),
            #self.radius
        #)


        # Display particle surface
        #screen.blit(
            #particle_surface,
            #(int(self.x - self.radius), int(self.y - self.radius))
        #)


        # life_ratio = max(0, self.lifespan / self.max_lifespan)

        pygame.draw.circle(
            screen, 
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )


        # Draw Trail

        positions = list(self.trail)

        for i in range(1, len(positions)):

            start = positions[i - 1]
            end = positions[i]

            # calculate fading intensity 
            intensity = i / len(positions)

            # Draw trail segment 
            trail_color = []

            # each iteration the color gets dimmed 
            for channel in self.color:
                dimmed_channel = int(channel * intensity)
                trail_color.append(dimmed_channel)

            # from list to tuple
            trail_color = tuple(trail_color)

            pygame.draw.line(
                screen,
                trail_color,
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1])),
                max(1, int(self.radius * intensity))
            )

        


    def update(self, gravity):

        self.vy += gravity      # gravity is added to the velocity 

        # position is updated by the added uniform velocity
        self.x += self.vx
        self.y += self.vy

        # Record current position
        self.trail.append((self.x, self.y))

        # Reduce lifespan
        self.lifespan -= 1

    def wall_collision(self, width, height):

        # Top wall 
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.vy *= -1               # changes velocity in opposite direction to simulate bounce

        # Bottom wall
        elif self.y + self.radius >= height:
            self.y = height - self.radius
            self.vy *= -1


        # Left wall 
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx *= -1

        elif self.x + self.radius >= width:
            self.x = width - self.radius
            self.vx *= -1