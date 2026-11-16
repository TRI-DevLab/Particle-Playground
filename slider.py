# This file is used to create the slider system which will be use in the main program.

import pygame
import config


class Slider:
    def __init__(
            self,
            x,
            y, 
            width, 
            min_value, 
            max_value,
            initial_value,
            label
        ):

        self.x = x
        self.y = y
        self.width = width

        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value              # The current value

        self.label = label

        self.is_dragging = False                # used to determine whether the slider is selected

        self.font = pygame.font.SysFont("Arial", 16)
        self.value_font = pygame.font.SysFont("Arial", 14)

        # Dimensions
        self.track_rect = pygame.Rect(x, y -3, width, 6)


    def _update_value(self, mouse_x):
        # used to update the value of the slider when dragged

        # subtract sliders starter position to determine where the mouse is relative to the slider
        relative_x = mouse_x - self.x

        # converts the position into a number between 1 & 0
        position = relative_x / self.width

        # The boundaries 
        position = max(0.0, min(1.0, position))

        # Convert to the actual the value
        self.value = (
            self.min_value + position * (self.max_value - self.min_value)
        )


    def draw(self, screen):

        # label 
        label_surface = self.font.render(
            self.label,
            True,
            config.WHITE
        )

        screen.blit(
            label_surface,
            (self.x, self.y - 35)
        )

        # Calculate Knob position 
        percentage = (self.value - self.min_value) / (self.max_value - self.min_value)

        knob_x = self.x + percentage * self.width

        # Draw slider track
        pygame.draw.line(
            screen,
            (80, 85, 100),
            (self.x, self.y),
            (self.x + self.width, self.y),
            6
        )

        # Draw filled track
        pygame.draw.line(
            screen, 
            (70, 150, 255), 
            (self.x, self.y),
            (int(knob_x), self.y),
            6
        )

        # Draw knob
        pygame.draw.circle(
            screen, 
            config.WHITE,
            (int(knob_x), self.y),
            9
        )

        # Draw Current Value
        value_surface = self.value_font.render(
            f"{self.value:.2f}",                                     # round of them
            True, 
            (180, 185, 200)
        )

        screen.blit(value_surface, (self.x + self.width - 45, self.y -35))



    def handle_event(self, event):

        # Mouse interactions with the slider

        # On holding the mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            # One left click
            if event.button == 1:

                # to create a taller invisible hitbox so that interaction is easier
                hitbox = self.track_rect.inflate(0, 25)

                if hitbox.collidepoint(event.pos):
                    self.is_dragging = True
                    self._update_value(event.pos[0])


        # when mouse is released
        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
                self.is_dragging = False


        # When mouse is moving
        elif event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                self._update_value(event.pos[0])