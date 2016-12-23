import os
import pygame.sprite

class Brick(pygame.sprite.Sprite):
    @staticmethod
    def init_bricks():
        bricks = []
        return bricks

    def __init__(self):
        super(Brick, self).__init__()  # init Sprite
