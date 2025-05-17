import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS, BALL_SPEED, WHITE

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Initialize base Sprite class
        # Create a transparent surface with diameter of the ball
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        # Draw a white circle on the surface to represent the ball
        pygame.draw.circle(self.image, WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        # Start the ball at the center of the screen
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # Set initial speed in pixels per second
        self.speed_x = random.choice([-1, 1]) * BALL_SPEED
        self.speed_y = -BALL_SPEED
        # Store position as float for smooth movement
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)

    def update(self, dt):
        # Update position based on speed and delta time
        self.pos_x += self.speed_x * dt
        self.pos_y += self.speed_y * dt
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

        # Bounce off left and right walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1

        # Bounce off the top wall
        if self.rect.top <= 0:
            self.speed_y *= -1

    def reset(self):
        # Reset ball to center and randomize horizontal direction
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        self.speed_x = random.choice([-1, 1]) * BALL_SPEED
        self.speed_y = -BALL_SPEED