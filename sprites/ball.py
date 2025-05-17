import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS, BALL_SPEED, WHITE

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = 0
        self.speed_y = 0
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)

    def update(self, dt):
        self.pos_x += self.speed_x * dt
        self.pos_y += self.speed_y * dt
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

    def reset(self, paddle=None):
        if paddle:
            self.rect.centerx = paddle.rect.centerx
            self.rect.bottom = paddle.rect.top
        else:
            self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        self.speed_x = 0
        self.speed_y = 0

    def attach_to_paddle(self, paddle):
        self.rect.centerx = paddle.rect.centerx
        self.rect.bottom = paddle.rect.top
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)

    def launch(self):
        self.speed_x = random.choice([-1, 1]) * BALL_SPEED
        self.speed_y = -BALL_SPEED