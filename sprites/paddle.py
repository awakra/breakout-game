import pygame
from constants import SCREEN_WIDTH, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, BLUE, SCREEN_HEIGHT

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)
        self.speed = PADDLE_SPEED
        self.pos_x = float(self.rect.x)

    def update(self, keys, dt):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.pos_x -= self.speed * dt
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.pos_x += self.speed * dt
        self.rect.x = int(self.pos_x)