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
            paddle (Paddle): The game paddle.
            bricks (List(Brick)): The game bricks.
        """
        if self.state == 'stopped':
            self.rect.x = \
                paddle.rect.x + (paddle.rect.width / 2) - (self.rect.width / 2)
            self.rect.y = paddle.rect.y - self.rect.height
            return

        new_pos = self.__calc_pos()

        # Check for collision with walls
        if not self.area.contains(new_pos):
            tl = not self.area.collidepoint(new_pos.topleft)
            tr = not self.area.collidepoint(new_pos.topright)
            bl = not self.area.collidepoint(new_pos.bottomleft)
            br = not self.area.collidepoint(new_pos.bottomright)

            if (tl and tr) or (bl and br):  # hit top or bottom wall
                self.angle = -self.angle
            elif (tl and bl) or (tr and br):  # hit left or right wall
                self.angle = 180 - self.angle
        else:
            # Check for collision with paddle
            if paddle.rect.colliderect(new_pos):
                # When colliding with the paddle, the ball's angle is changed
                # depending on where the ball collided with the paddle. This
                # angle is not dependant on the angle the ball is currently
                # traveling. The angle ranges from 26 at the right-most surface
                # of the paddle, to 154 at the left-most.
                angle = 26 + paddle.rect.right - self.rect.centerx
                if angle < 26:
                    angle = 26
                elif angle > 154:
                    angle = 154
                self.angle = angle
            else:
                # Check for collision with bricks
                for brick in bricks:
                    if brick.rect.colliderect(new_pos):
                        self.angle = -self.angle
                        brick.kill()
                        bricks.remove(brick)

        self.rect = new_pos

    def fire(self):
        """Fires the ball from the paddle."""
        if self.state == 'stopped':
            self.state = 'moving'
            self.angle = 90

    def __calc_pos(self):
        """Calculates the new position of the ball given its angle.

        Returns:
            Rect: The ball's new bounding Rectangle given the angle.
        """
        delta_x = int(math.cos(math.radians(self.angle)) * self.speed)
        delta_y = -int(math.sin(math.radians(self.angle)) * self.speed)
        return self.rect.move(delta_x, delta_y)
