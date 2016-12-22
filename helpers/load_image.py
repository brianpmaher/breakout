import os
import pygame
import pygame.image
from pygame.locals import *

def load_png(path):
    """Load an image and return the image object
    Args:
        path (str): The image file path to load.

    Returns:
        Surface: The loaded image.
    """
    try:
        image = pygame.image.load(path)
        if image.get_alpha() is None:
            image.convert()
        else:
            image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image: ', path)
        raise SystemExit(message)
    return image
