#!/usr/bin/env python3

from helpers.load_image import load_png
from models.paddle import Paddle

import os
import sys
import pygame
import pygame.image
import pygame.time

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

    # Initialize the bricks
    # TODO

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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddle.stop(event.key)

        screen.blit(background, paddle.rect, paddle.rect)
        screen.blit(background, (0, 0))
        paddle_sprite.update()
        paddle_sprite.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    game()
