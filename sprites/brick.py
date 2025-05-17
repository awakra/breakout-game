import pygame
from constants import BRICK_WIDTH, BRICK_HEIGHT

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()  # Initialize base Sprite class
        # Create the brick surface with specified width and height
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(color)  # Fill the brick with the given color
        self.rect = self.image.get_rect()  # Get the rectangle for positioning
        self.rect.topleft = (x, y)  # Set the top-left position of the brick