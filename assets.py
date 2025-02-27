# File for loading resources

import pygame
from settings import TILE_SIZE, HEALTHBAR_HEIGHT, HEALTHBAR_WIDTH

# Loading assets
# Player
player_img = pygame.image.load("Assets/player.png") 
player_img = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))

# Mobs
entity_img = pygame.image.load("Assets/enemy.png")
entity_img = pygame.transform.scale(entity_img, (TILE_SIZE, TILE_SIZE))

# Bullets
fireball_img = pygame.image.load("Assets/fireball.png")
fireball_img = pygame.transform.scale(fireball_img, (20, 20))

# Healthbar
healthbar_bg = pygame.image.load("Assets/healthbar_bg.png")
healthbar_fill = pygame.image.load("Assets/healthbar_fill.png")
healthbar_bg = pygame.transform.scale(healthbar_bg, (HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT))
healthbar_fill = pygame.transform.scale(healthbar_fill, (HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT))

# Coins
coins_one_img = pygame.image.load("Assets/coins/coins_one.png")
coins_one_img = pygame.transform.scale(coins_one_img, (TILE_SIZE // 2, TILE_SIZE // 2))
coins_two_img = pygame.image.load("Assets/coins/coins_two.png")
coins_two_img = pygame.transform.scale(coins_two_img, (TILE_SIZE // 2, TILE_SIZE // 2))
coins_four_img = pygame.image.load("Assets/coins/coins_four.png")
coins_four_img = pygame.transform.scale(coins_four_img, (TILE_SIZE // 2, TILE_SIZE // 2))

# Fonts
pygame.font.init()
font = pygame.font.Font(None, 24)