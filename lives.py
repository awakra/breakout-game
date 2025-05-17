import pygame
from constants import WHITE

class Lives:
    def __init__(self, screen, initial_lives=3, font_size=30, position=(150, 10), color=WHITE):
        self.screen = screen
        self.lives = initial_lives
        self.position = position
        self.color = color
        self.font = pygame.font.Font(None, font_size)

    def lose_life(self):
        self.lives -= 1

    def reset(self, value=3):
        self.lives = value

    def draw(self):
        lives_text = self.font.render(f"Lives: {self.lives}", True, self.color)
        self.screen.blit(lives_text, self.position)