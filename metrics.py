import pygame
from constants import WHITE

class Metrics:
    def __init__(self, screen, font_size=24, position=(10, 10), color=WHITE):
        """
        Initializes the Metrics object.

        Args:
            screen (pygame.Surface): The surface on which the metrics will be displayed.
            font_size (int, optional): The size of the font for displaying metrics. Defaults to 24.
            position (tuple, optional): The (x, y) position where the metrics will be displayed. Defaults to (10, 10).
            color (tuple, optional): The color of the text, represented as an RGB tuple. Defaults to WHITE.
        """
        self.screen = screen
        self.position = position
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        self.clock = pygame.time.Clock()

    def tick(self, fps_limit):
        """
        Regulates the frame rate of the game loop and calculates the time delta.

        Args:
            fps_limit (int): The maximum frames per second to limit the game loop.

        Returns:
            float: The time delta (dt) in seconds since the last frame.
        """
        dt = self.clock.tick(fps_limit) / 1000
        return dt

    def draw_fps(self):
        """
        Draws the current frames per second (FPS) on the screen.

        This method retrieves the current FPS from the clock object, renders it
        as a text surface using the specified font and color, and blits it onto
        the screen at the specified position.

        Attributes:
            self.clock (pygame.time.Clock): The clock object used to track FPS.
            self.font (pygame.font.Font): The font object used to render the FPS text.
            self.color (tuple): The color of the FPS text, specified as an RGB tuple.
            self.screen (pygame.Surface): The surface on which the FPS text is drawn.
            self.position (tuple): The (x, y) position where the FPS text is displayed.

        Returns:
            None
        """
        fps = self.clock.get_fps()
        fps_text = self.font.render(f"FPS: {fps:.2f}", True, self.color)
        self.screen.blit(fps_text, self.position)