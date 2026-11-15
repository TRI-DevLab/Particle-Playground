# This file contains the code the governs how the panel is is going to look and work 

import pygame
import config

class ControlPanel:

    def __init__(self, screen):

        self.screen = screen

        self.font = pygame.font.SysFont("Arial", 22)
        self.small_font = pygame.font.SysFont("Ariel", 16)

        # Set the dimensions of the panel
        self.panel_rect = pygame.Rect(
            config.WINDOW_WIDTH - config.PANEL_WIDTH,
            0,
            config.PANEL_WIDTH,
            config.WINDOW_HEIGHT 
        )

    def draw(self, particle_count, paused):

        # Draw the panel
        pygame.draw.rect(
            self.screen,
            config.PANEL_COLOR,
            self.panel_rect
        )

        # Title 
        title = self.font.render(
            "Particle Playground",
            True,
            config.WHITE
        )

        self.screen.blit(title, (870, 30))


