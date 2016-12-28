import os

import pygame.sprite

from helpers.load_image import load_png


class Ball(pygame.sprite.Sprite):
    """A game ball object.

    Attributes:
        image (pygame.Surface): The ball sprite image.
        rect (pygame.Rect): The rectangle around the ball sprite image.
        area (pygame.Rect): Total suraface area for the game. Used to calculate
            positions the ball can move.
        speed (int): The speed that the ball can move.
        state (str): The state the current ball is in. Can be 'stopped' or
            'moving'.
    """

    def __init__(self):
        super(Ball, self).__init__()  # init Sprite
        ball_path = os.path.join('assets', 'sprites', 'ball_red.png')
        self.image = load_png(ball_path)
        self.rect = self.image.get_rect()
        self.area = pygame.display.get_surface().get_rect()
        self.speed = 15
        self.state = 'stopped'

    def update(self, paddle):
        """Updates the ball.

        Args:
            paddle (Paddle): The player paddle.
        """
        if self.state == 'stopped':
            self.rect.x = \
                paddle.rect.x + (paddle.rect.width / 2) - (self.rect.width / 2)
            self.rect.y = paddle.rect.y - self.rect.height
