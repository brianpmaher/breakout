from helpers.load_image import load_png

import os
import pygame.sprite
from collections import namedtuple


class Brick(pygame.sprite.Sprite):
    """A game brick object.

    Attributes:
        image (pygame.Surface): The brick sprite image.
        rect (pygame.Rect): The rectangle around the brick sprite image.
    """

    RED_BRICK_COORDS = [(16, 32), (80, 32), (144, 32), (208, 32), (272, 32),
                        (336, 32), (400, 32), (464, 32), (528, 32), (592, 32),
                        (656, 32), (720, 32)]
    ORANGE_BRICK_COORDS = [(16, 64), (80, 64), (144, 64), (208, 64), (272, 64),
                           (336, 64), (400, 64), (464, 64), (528, 64),
                           (592, 64), (656, 64), (720, 64)]
    YELLOW_BRICK_COORDS = [(16, 96), (80, 96), (144, 96), (208, 96), (272, 96),
                           (336, 96), (400, 96), (464, 96), (528, 96),
                           (592, 96), (656, 96), (720, 96)]
    GREEN_BRICK_COORDS = [(16, 128), (80, 128), (144, 128), (208, 128),
                          (272, 128), (336, 128), (400, 128), (464, 128),
                          (528, 128), (592, 128), (656, 128), (720, 128)]
    BLUE_BRICK_COORDS = [(16, 160), (80, 160), (144, 160), (208, 160),
                         (272, 160), (336, 160), (400, 160), (464, 160),
                         (528, 160), (592, 160), (656, 160), (720, 160)]
    BRICK_COORDS = {'red': RED_BRICK_COORDS, 'orange': ORANGE_BRICK_COORDS,
                    'yellow': YELLOW_BRICK_COORDS, 'green': GREEN_BRICK_COORDS,
                    'blue': BLUE_BRICK_COORDS}

    @staticmethod
    def init_bricks():
        """Initailizes the bricks with their coordinates.

        Returns:
            List(Brick): The list of game bricks.
        """
        Coord = namedtuple('Coord', ['x', 'y'])
        bricks = []

        # Initialize bricks.
        for color, coords in Brick.BRICK_COORDS.items():
            for coord in coords:
                x, y = coord
                bricks.append(Brick(Coord(x, y), color))

        return bricks

    def __init__(self, coord, color):
        """Initailizes a game brick.

        Args:
            coords (namedtuple): The coordinates for the brick.
            color (str): The brick color.
        """
        super(Brick, self).__init__()  # init Sprite
        sprite_file_name = 'brick_' + color + '.png'
        sprite_path = os.path.join('assets', 'sprites', sprite_file_name)
        self.image = load_png(sprite_path)
        self.rect = self.image.get_rect()

        # Initialize the brick location.
        self.rect.x = coord.x
        self.rect.y = coord.y
