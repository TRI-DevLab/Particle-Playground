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

    def remove_particle(self, x, y):

        # if there are not particles account for that
        if not self.particles:
            return 

        # Going to remove the closest particle to the pointer

        # initial particle and distance
        nearest_particle = self.particles[0]
        min_dist_sq = (nearest_particle.x - x) ** 2 + (nearest_particle.y - y) ** 2

        # Iterate from second particle
        for particle in self.particles[1:]:
            dist_sq = (particle.x - x) ** 2 + (particle.y - y) ** 2
            # check which is smaller
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq           # if distance is smaller assign it to min variable 
                nearest_particle = particle     # assign it to the min variable


        # remove the closest distance
        self.particles.remove(nearest_particle)

    
    def clear(self):

        # removes all particles
        self.particles.clear()

    def attract_particles(self, mouse_x, mouse_y):

        strength = 0.05

        # for each particle
        for particle in self.particles:

            # get distance between particle and mouse
            dx = mouse_x - particle.x
            dy = mouse_y - particle.y

            # update the velocity to to move towards the distance by the strength
            particle.vx += dx * strength
            particle.vy += dy * strength