import pygame
from constants import *
import sys


pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()