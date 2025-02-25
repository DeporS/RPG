# File for loading resources

import pygame
from settings import TILE_SIZE

# Loading assets
player_img = pygame.image.load("Assets/player.png") 
player_img = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))
entity_img = pygame.image.load("Assets/enemy.png")
entity_img = pygame.transform.scale(entity_img, (TILE_SIZE, TILE_SIZE))
fireball_img = pygame.image.load("Assets/fireball.png")
fireball_img = pygame.transform.scale(fireball_img, (20, 20))