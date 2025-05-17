import pygame
import sys
from constants import *
from metrics import FrameRate, Scoreboard, Lives
from collision_manager import CollisionManager
from sprites.paddle import Paddle
from sprites.brick import Brick
from sprites.ball import Ball
from utils import reset_game_state, game_loop_step

pygame.init()
# Set up the game window with defined width and height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

# Initialize HUD elements
framerate = FrameRate(screen)
scoreboard = Scoreboard(screen)
lives = Lives(screen)

# Create all game objects
paddle = Paddle()
bricks_group = Brick.create_wall()
ball = Ball()

# Add all objects to all_sprites at once
all_sprites = pygame.sprite.Group(paddle, *bricks_group, ball)

# Initialize the collision manager with references to ball, paddle, and bricks
collision_manager = CollisionManager(ball, paddle, bricks_group)

waiting_for_launch = True  # Ball waits on paddle until UP arrow is pressed

running = True
while running:
    # Use the utility function to handle one step of the game loop
    waiting_for_launch, running = game_loop_step(
        screen, framerate, scoreboard, lives, all_sprites,
        paddle, ball, collision_manager, waiting_for_launch, running, FPS
    )

    # Game Over check and retry logic
    if lives.is_game_over():
        lives.draw_game_over(scoreboard.score, show_retry=True)
        retry = False
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        retry = True
                        waiting = False
        if retry:
            # Reset all game state using the utility function
            bricks_group = reset_game_state(
                all_sprites, bricks_group, paddle, ball, scoreboard, lives
            )
            # Re-initialize the collision manager with the new bricks_group
            collision_manager = CollisionManager(ball, paddle, bricks_group)
            waiting_for_launch = True
            continue  # Restart main loop
        else:
            break  # Exit main loop

# Quit pygame and exit the program cleanly
pygame.quit()
sys.exit()