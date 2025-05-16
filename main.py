import pygame
import sys
from constants import *
from metrics import Metrics
from sprites.paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
metrics = Metrics(screen)

font = pygame.font.Font(None, 30)

paddle = Paddle()
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle)

running = True
while running:
    # Sets maximum framerate to constant.py FPS and gets delta time
    dt = metrics.tick(FPS)
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    all_sprites.update(keys, dt) 
            
    screen.fill(BLACK)

    metrics.draw_fps()  # Draw FPS in the top left corner of the screen
    
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
# Exit the program