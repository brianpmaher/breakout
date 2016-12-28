import os
from collections import namedtuple

import pygame
import pygame.sprite
import pygame.display

from helpers.load_image import load_png


class Paddle(pygame.sprite.Sprite):
    """A player paddle object.

    Attributes:
        image (pygame.Surface): The paddle sprite image.
        rect (pygame.Rect): The rectangle around the paddle sprite image.
        area (pygame.Rect): Total suraface area for the game. Used to calculate
            positions the paddle can move.
        speed (int): The speed that the paddle can move.
        state (str): The state the current paddle is in. Can be 'stopped',
            'move-left', or 'move-right'
        delta_x (int): The change in x value that the paddle is currently
            doing. This is set to positive or negative speed when the paddle is
            moving left or right and 0 when the paddle is stopped.
    """

    def __init__(self):
        super(Paddle, self).__init__()  # init Sprite
        sprite_path = os.path.join('assets', 'sprites', 'paddle_medium.png')
        self.image = load_png(sprite_path)
        self.rect = self.image.get_rect()
        self.area = pygame.display.get_surface().get_rect()
        self.speed = 10
        self.state = 'stopped'
        self.delta_x = 0

        # Initialize the paddle location to 20px above the bottom and centered.
        self.rect.y = self.area.bottom - self.rect.height - 20
        self.rect.x = self.area.centerx - (self.rect.width / 2)

    def move_left(self):
        """Moves the paddle left."""
        self.state = 'move-left'
        self.delta_x = -self.speed

    def move_right(self):
        """Moves the paddle right."""
        self.state = 'move-right'
        self.delta_x = self.speed

    def stop(self, key):
        """Stops the paddle only if the key that was lifted matches the
        direction that the paddle was last moving.

        Args:
            key (pygame.key): The key that was released.
        """
        if self.state == 'move-left' and key == pygame.K_LEFT:
            self.state = 'stopped'
            self.delta_x = 0
        elif self.state == 'move-right' and key == pygame.K_RIGHT:
            self.state = 'stopped'
            self.delta_x = 0

    def update(self):
        """Updates the paddle position."""
        new_pos = self.rect.move([self.delta_x, 0])
        if self.area.contains(new_pos):
            self.rect = new_pos

    def get_coords(self):
        """Returns the coordinates of the paddle as a namedtuple of the rect.

        Returns:
            namedtuple: The paddle coordinates.
        """
        Coord = namedtuple('Coord', ['x', 'y'])
        return Coord(self.rect.x, self.rect.y)
