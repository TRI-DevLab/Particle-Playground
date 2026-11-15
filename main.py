# The main file where the program meets all the ideas and runs everything.

import pygame 
import config
from sys import exit
from particle import Particle
from simulation import Simulation




def main():
    pygame.init()           # Initiate Pygame 


    screen = pygame.display.set_mode(
        (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    )

    pygame.display.set_caption(config.WINDOW_TITLE)

    clock = pygame.time.Clock()

    simulation = Simulation()


    # Create a some particles 
    simulation.add_particle(500, 250)
    simulation.add_particle(600, 100)
    simulation.add_particle(400, 125)
    simulation.add_particle(100, 350)

    running = True

    while running:

        clock.tick(config.FPS)

        # Event handling 
        for event in pygame.event.get():

            # Exiting the Program 
            if event.type == pygame.QUIT:
                running = False


        # Rendering 
        screen.fill(config.BACKGROUND_COLOR)

        # This changes the particles positioning in real time and establishes walls for each particle
        simulation.update(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

        simulation.draw(screen)

        pygame.display.flip()               # Update constantly 


    pygame.quit()
    exit()


if __name__ == "__main__":
    main()

