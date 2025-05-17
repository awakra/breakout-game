import pygame
from constants import WHITE, SCREEN_WIDTH

class Scoreboard:
    def __init__(self, screen, font_size=30, position=(SCREEN_WIDTH - 150, 10), color=WHITE):
        self.screen = screen
        self.position = position
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        self.score = 0

    def add_points(self, points):
        self.score += points

    def reset(self):
        self.score = 0

    def draw(self):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        self.screen.blit(score_text, self.position)