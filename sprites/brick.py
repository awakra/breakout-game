import pygame
from constants import *

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()  # Initialize base Sprite class
        # Create the brick surface with specified width and height
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(color)  # Fill the brick with the given color
        self.rect = self.image.get_rect()  # Get the rectangle for positioning
        self.rect.topleft = (x, y)  # Set the top-left position of the brick

    @classmethod
    def create_wall(cls):
        """
        Create and return a group of bricks arranged in rows and columns,
        centered horizontally on the screen.
        """
        bricks_group = pygame.sprite.Group()
        # Calculate total width of bricks and padding to center them horizontally
        total_width = (BRICK_WIDTH * BRICK_COLS) + (BRICK_PADDING * (BRICK_COLS - 1))
        start_x = (SCREEN_WIDTH - total_width) / 2
        # Create bricks in rows and columns
        for row in range(BRICK_ROWS):
            y = row * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_OFFSET_TOP
            color = BRICK_COLORS[row % len(BRICK_COLORS)]  # Cycle through colors per row
            for col in range(BRICK_COLS):
                x = start_x + col * (BRICK_WIDTH + BRICK_PADDING)
                brick = cls(x, y, color)
                bricks_group.add(brick)
        return bricks_group