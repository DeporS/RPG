# File for settings

import pygame

NAME = "MY RPG"
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 32
FPS = 60

HEALTHBAR_WIDTH = 196
HEALTHBAR_HEIGHT = 32
HEALTHBARPOS_X = WIDTH // 2 - HEALTHBAR_WIDTH // 2

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 153, 51)

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)
