# The main file where the program meets all the ideas and runs everything.

import pygame 
import config
from sys import exit
from particle import Particle




def main():
    pygame.init()           # Initiate Pygame 


    screen = pygame.display.set_mode(
        (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    )

    pygame.display.set_caption(config.WINDOW_TITLE)

    clock = pygame.time.Clock()

    # Create a Particle 
    particle = Particle(500, 250)

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

        particle.update()                   # This changes the particles positioning in real time 
        particle.draw(screen)

        pygame.display.flip()               # Update constantly 


    pygame.quit()
    exit()


if __name__ == "__main__":
    main()

