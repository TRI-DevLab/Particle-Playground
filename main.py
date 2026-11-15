# The main file where the program meets all the ideas and runs everything.

import pygame 
import config
from sys import exit
from particle import Particle
from simulation import Simulation
import random




def main():
    pygame.init()           # Initiate Pygame 


    screen = pygame.display.set_mode(
        (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    )

    pygame.display.set_caption(config.WINDOW_TITLE)

    clock = pygame.time.Clock()

    simulation = Simulation()


    # Create a some particles 


    for _ in range(50):
        simulation.add_particle(
            random.randint(100, 1000), 
            random.randint(100, 500)
        )

    running = True

    while running:

        clock.tick(config.FPS)

        # Event handling 
        for event in pygame.event.get():

            # Exiting the Program 
            if event.type == pygame.QUIT:
                running = False

            # Mouse 
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Adding particles with mouse left click
                if event.button == 1:
                    x, y = event.pos        
                    simulation.add_particle(x, y)

                # Remove nearest particles with mouse right click
                elif event.button == 3:
                    x, y = event.pos
                    simulation.remove_particle(x, y)

            # Keyboards
            elif event.type == pygame.KEYDOWN:

                # Clears the screen (R key)
                if event.key == pygame.K_r:
                    simulation.clear()

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

