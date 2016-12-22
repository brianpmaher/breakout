#!/usr/bin/env python3

import os
import sys
import pygame
import pygame.image

def game():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Breakout')

    # Initialize background
    background_path = os.path.join('assets', 'backgrounds', 'space.png')
    background = pygame.image.load(background_path)

    # Blit everything onto the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    game()
