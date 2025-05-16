import pygame
from constants import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Initialize base Sprite class
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))  # Creates paddle image
        self.image.fill(BLUE)  # Defines paddle color
        self.rect = self.image.get_rect()  # Gets rectangle for positioning
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT )  # Starting position
        self.speed = PADDLE_SPEED
        self.pos_x = float(self.rect.x)

    def update(self, keys, dt):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.pos_x -= self.speed * dt
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.pos_x += self.speed * dt
        self.rect.x = int(self.pos_x)