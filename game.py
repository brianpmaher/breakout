#!/usr/bin/env python3

import os
import sys

import pygame
import pygame.image
import pygame.time
import pygame.font

from helpers.load_image import load_png
from models.paddle import Paddle
from models.brick import Brick
from models.ball import Ball

VERSION = 0.1


def game_over(background, paddle, ball, bricks, message):
    """Displays the win/loss message and ends the game.

    Args:
        background (pygame.Surface): The game background.
        paddle (Paddle): The game paddle.
        ball (Ball): The game ball.
        bricks (List(Brick)): List of game bricks.
        message (str): The end game display message.
    """
    paddle.kill()
    ball.kill()
    for brick in bricks:
        brick.kill()
    font = pygame.font.Font(None, 100)
    text = font.render(message, 1, (255, 255, 255))
    textpos = text.get_rect(centerx=background.get_width() / 2,
                            centery=background.get_height() / 2)
    background.blit(text, textpos)

def game():
    """Main game function. Initializes and loads game assets and handles
    events."""
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Breakout')

    # Initialize background
    background_path = os.path.join('assets', 'backgrounds', 'space.png')
    background = load_png(background_path)

    # Initialize player Paddle
    paddle = Paddle()
    paddle_sprite = pygame.sprite.Group(paddle)

    # Initialize the ball
    ball = Ball()
    ball_sprite = pygame.sprite.Group(ball)

    # Initialize the bricks
    bricks = Brick.init_bricks()
    brick_sprites = pygame.sprite.Group(bricks)

    # Blit everything onto the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialize cock
    clock = pygame.time.Clock()

    # Event loop
    while True:
        # Make sure the game doesn't run at more than 60 fps
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle.move_left()
                elif event.key == pygame.K_RIGHT:
                    paddle.move_right()
                if event.key == pygame.K_SPACE:
                    ball.fire()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddle.stop(event.key)

        # Blit all objects onto background.
        screen.blit(background, paddle.rect, paddle.rect)
        screen.blit(background, ball.rect, ball.rect)
        for brick in bricks:
            screen.blit(background, brick.rect, brick.rect)
        screen.blit(background, (0, 0))

        # Update all sprites.
        paddle_sprite.update()
        ball_sprite.update(paddle, bricks)
        brick_sprites.update()

        # Check for win
        if len(bricks) == 0:
            game_over(background, paddle, ball, bricks, 'You Win!')

        # Check for loss
        if ball.state == 'deleted':
            game_over(background, paddle, ball, bricks, 'Game Over.')

        # Draw all sprites.
        paddle_sprite.draw(screen)
        ball_sprite.draw(screen)
        brick_sprites.draw(screen)

        # Flip the display.
        pygame.display.flip()

if __name__ == '__main__':
    game()
