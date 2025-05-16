import pygame
from constants import *
import sys


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

running = True

while running:
    # Sets maximum framerate to 60 and gets delta time
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
    

        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(BLACK)
    # Cleans the screen using the black color
    
    pygame.display.flip()

pygame.quit()
sys.exit()
# Exit the program