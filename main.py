import pygame
import sys
from constants import *
from metrics import Metrics
from scoreboard import Scoreboard
from collision_manager import CollisionManager
from sprites.paddle import Paddle
from sprites.brick import Brick
from sprites.ball import Ball

pygame.init()
# Set up the game window with defined width and height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
metrics = Metrics(screen)  # Initialize FPS metrics display

# Create sprite groups for managing game objects
all_sprites = pygame.sprite.Group()
bricks_group = pygame.sprite.Group()

# Create the paddle and add it to the all_sprites group
paddle = Paddle()
all_sprites.add(paddle)

# Calculate total width of bricks and padding to center them horizontally
total_width = (BRICK_WIDTH * BRICK_COLS) + (BRICK_PADDING * (BRICK_COLS - 1))
start_x = (SCREEN_WIDTH - total_width) / 2

# Create bricks in rows and columns, position them centered horizontally
for row in range(BRICK_ROWS):
    y = row * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_OFFSET_TOP
    color = BRICK_COLORS[row % len(BRICK_COLORS)]  # Cycle through colors per row
    for col in range(BRICK_COLS):
        x = start_x + col * (BRICK_WIDTH + BRICK_PADDING)
        brick = Brick(x, y, color)
        bricks_group.add(brick)  # Add brick to bricks group for collision detection
        all_sprites.add(brick)   # Add brick to all_sprites for drawing

# Create the ball and add it to all_sprites
ball = Ball()
all_sprites.add(ball)

# Initialize the scoreboard to display the player's score
scoreboard = Scoreboard(screen)

# Initialize the collision manager with references to ball, paddle, and bricks
collision_manager = CollisionManager(ball, paddle, bricks_group)

running = True
while running:
    # Limit the frame rate and get delta time (seconds since last frame)
    dt = metrics.tick(FPS)

    # Handle events such as window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of keyboard keys
    keys = pygame.key.get_pressed()

    # Update paddle with keyboard input and delta time
    paddle.update(keys, dt)
    # Update ball position with delta time
    ball.update(dt)
    # Update bricks if they have any update logic (optional)
    bricks_group.update()

    # Handle collisions and get list of bricks hit this frame
    hit_blocks = collision_manager.handle_collisions()
    if hit_blocks:
        # Add points to scoreboard based on number of bricks hit
        points = len(hit_blocks) * 10
        scoreboard.add_points(points)

    # Clear the screen with black color
    screen.fill(BLACK)
    # Draw all sprites (paddle, ball, bricks)
    all_sprites.draw(screen)
    # Draw FPS counter on screen
    metrics.draw_fps()
    # Draw the current score on screen
    scoreboard.draw()

    # Update the full display surface to the screen
    pygame.display.flip()

# Quit pygame and exit the program cleanly
pygame.quit()
sys.exit()