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

        # Adjustment for Control Panel
        panel_x = self.panel_rect.x + 20 

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

        self.screen.blit(title, (panel_x, 30))

        # Count Text
        count_text = self.small_font.render(
            f"Particles: {particle_count}",
            True, 
            config.MUTED_COLOR
        )

        self.screen.blit(count_text, (panel_x, 80))

        # Status
        if paused:
            status = "PAUSED"
        else:
            status = "RUNNING"

        status_text = self.small_font.render(
            status,
            True,
            config.ACCENT_COLOR
        )

        self.screen.blit(status_text, (panel_x, 110))
        


