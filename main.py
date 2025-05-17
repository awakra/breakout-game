import pygame
import sys
from constants import *
from metrics import Metrics
from sprites.paddle import Paddle
from sprites.brick import Brick

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
metrics = Metrics(screen)

font = pygame.font.Font(None, 30)

all_sprites = pygame.sprite.Group()
bricks_group = pygame.sprite.Group()

paddle = Paddle()
all_sprites.add(paddle)

# Calculate total width of bricks and padding to center them
total_width = (BRICK_WIDTH * BRICK_COLS) + (BRICK_PADDING * (BRICK_COLS - 1))
start_x = (SCREEN_WIDTH - total_width) / 2  # Starting x position for centering

for row in range(BRICK_ROWS):
    y = row * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_OFFSET_TOP
    color = BRICK_COLORS[row % len(BRICK_COLORS)]
    for col in range(BRICK_COLS):
        x = start_x + col * (BRICK_WIDTH + BRICK_PADDING)
        brick = Brick(x, y, color)
        bricks_group.add(brick)
        all_sprites.add(brick)

running = True
while running:
    # Set maximum framerate to constant.py FPS and get delta time
    dt = metrics.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    all_sprites.update(keys, dt)
    screen.fill(BLACK)
    all_sprites.draw(screen)

    metrics.draw_fps()  # Draw FPS in the top left corner of the screen

    pygame.display.flip()

pygame.quit()
sys.exit()