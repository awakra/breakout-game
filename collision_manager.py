import pygame
from constants import BALL_SPEED, SCREEN_HEIGHT

class CollisionManager:
    def __init__(self, ball, paddle, bricks_group):
        self.ball = ball
        self.paddle = paddle
        self.bricks_group = bricks_group

    def handle_collisions(self):
        # Ball and paddle collision
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.speed_y *= -1
            offset = (self.ball.rect.centerx - self.paddle.rect.centerx) / (self.paddle.rect.width / 2)
            self.ball.speed_x = BALL_SPEED * offset

        # Ball and bricks collision
        hit_blocks = pygame.sprite.spritecollide(self.ball, self.bricks_group, True)
        if hit_blocks:
            self.ball.speed_y *= -1

        # Ball out of bottom screen (missed paddle)
        if self.ball.rect.top > SCREEN_HEIGHT:
            self.ball.reset(self.paddle)
            return []

        return hit_blocks