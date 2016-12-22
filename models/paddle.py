from helpers.load_image import load_png

import os
import pygame.sprite
import pygame.display


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super(Paddle, self).__init__()  # init Sprite
        sprite_path = os.path.join('assets', 'sprites', 'paddle_medium.png')
        self.image = load_png(sprite_path)
        self.rect = self.image.get_rect()
        self.area = pygame.display.get_surface().get_rect()
