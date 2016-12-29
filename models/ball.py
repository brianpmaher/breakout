import os
import math

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
        angle (int): The current angle the ball is moving.
    """

    def __init__(self):
        super(Ball, self).__init__()  # init Sprite
        ball_path = os.path.join('assets', 'sprites', 'ball_red.png')
        self.image = load_png(ball_path)
        self.rect = self.image.get_rect()
        self.area = pygame.display.get_surface().get_rect()
        self.speed = 10
        self.state = 'stopped'
        self.angle = 90

    def update(self, paddle, bricks):
        """Updates the ball.

        Args:
            paddle (Paddle): The player paddle.
            bricks (List(Brick)): The bricks in the game.
        """
        if self.state == 'stopped':
            self.rect.x = \
                paddle.rect.x + (paddle.rect.width / 2) - (self.rect.width / 2)
            self.rect.y = paddle.rect.y - self.rect.height
            return

        new_pos = self.__calc_pos()

        # Check for collision with walls
        if not self.area.contains(new_pos):
            self.angle = -self.angle
            new_pos = self.__calc_pos()
        else:
            # Check for collision with paddle
            if paddle.rect.colliderect(new_pos):
                self.angle = -self.angle
                new_pos = self.__calc_pos()

            # Check for collision with bricks
            for brick in bricks:
                if brick.rect.colliderect(new_pos):
                    self.angle = -self.angle
                    new_pos = self.__calc_pos()
                    brick.kill()
                    bricks.remove(brick)

        self.rect = new_pos

    def fire(self):
        """Fires the ball from the paddle."""
        if self.state == 'stopped':
            self.state = 'moving'
            self.angle = 90

    def __calc_pos(self):
        new_x = int(math.cos(math.radians(self.angle))) * self.speed
        new_y = -int(math.sin(math.radians(self.angle))) * self.speed
        return self.rect.move(new_x, new_y)
