# This file manges a the particles and how they interact with the screen it manages how a bunch of them are created, stored and updated.

from particle import Particle 


class Simulation:

    def __init__(self):
        self.particles = []     # This will hold a list of particle functions


    def add_particle(self, x, y):

        particle = Particle(x, y)

        self.particles.append(particle)

    def draw(self, screen):

        # Draws multiple particles on the screen
        for particle in self.particles:
            particle.draw(screen)

    def update(self, width, height):

        # Updates multiple particles in real time
        for particle in self.particles:
            particle.update()

            # Establishes walls for the particle
            particle.wall_collision(width, height)