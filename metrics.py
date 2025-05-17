import pygame
from constants import *

class FrameRate:
    def __init__(self, screen, font_size=FONT_SIZE, position=(10, 10), color=WHITE):
        self.screen = screen
        self.position = position
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        self.clock = pygame.time.Clock()

    def tick(self, fps_limit):
        dt = self.clock.tick(fps_limit) / 1000
        return dt

    def draw(self):
        fps = self.clock.get_fps()
        fps_text = self.font.render(f"FPS: {fps:.2f}", True, self.color)
        self.screen.blit(fps_text, self.position)
        
class Scoreboard:
    def __init__(self, screen, font_size=FONT_SIZE, position=(SCREEN_WIDTH / 2, 10), color=WHITE):
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

class Lives:
    def __init__(self, screen, initial_lives=INITIAL_LIVES, font_size=FONT_SIZE, position=(SCREEN_WIDTH - 125, 10), color=WHITE):
        self.screen = screen
        self.lives = initial_lives
        self.position = position
        self.color = color
        self.font = pygame.font.Font(None, font_size)

    def lose_life(self):
        self.lives -= 1

    def reset(self, value=INITIAL_LIVES):
        self.lives = value

    def draw(self):
        lives_text = self.font.render(f"Lives: {self.lives}", True, self.color)
        self.screen.blit(lives_text, self.position)

    def is_game_over(self):
        return self.lives <= 0

    def draw_game_over(self, score, show_retry=False):
        font = pygame.font.Font(None, 100)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        if show_retry:
            retry_font = pygame.font.Font(None, 50)
            retry_text = retry_font.render("Press R to Retry", True, (255, 255, 255))
            self.screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
        pygame.display.flip()