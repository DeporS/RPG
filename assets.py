# File for loading resources

import pygame
from settings import TILE_SIZE, HEALTHBAR_HEIGHT, HEALTHBAR_WIDTH

# Loading assets
player_img = pygame.image.load("Assets/player.png") 
player_img = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))

entity_img = pygame.image.load("Assets/enemy.png")
entity_img = pygame.transform.scale(entity_img, (TILE_SIZE, TILE_SIZE))

fireball_img = pygame.image.load("Assets/fireball.png")
fireball_img = pygame.transform.scale(fireball_img, (20, 20))

healthbar_bg = pygame.image.load("Assets/healthbar_bg.png")
healthbar_fill = pygame.image.load("Assets/healthbar_fill.png")
healthbar_bg = pygame.transform.scale(healthbar_bg, (HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT))
healthbar_fill = pygame.transform.scale(healthbar_fill, (HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT))


# Fonts
pygame.font.init()
font = pygame.font.Font(None, 24)