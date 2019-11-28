# FILE:     Elements.py
# AUTHOR:   Margaret Perry
# DATE:     2019/11/17
# VERSION:  1.0
# PURPOSE:  Creates Background as sprites for pygame

import pygame

"""
Name:       Background
Purpose:    Generates a background sprite
Notes:      None
"""

class Background(pygame.sprite.Sprite):
    """
    Name:        __init__
    Purpose:     Initalizes a background sprite
    Arguments:   image file, x y coodinates
    Output:      None
    Modifies:    None
    Returns:     Background sprite
    Assumptions: None
    Bugs:        None
    """

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)        # Call Pygame Sprite initializer
        self.image = pygame.image.load(image_file) # Loads given image
        self.rect = self.image.get_rect()          # Draws a rectangle to fit the background
        self.rect.left, self.rect.top = location   # Positions image at given coodinates
