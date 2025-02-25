import pygame
from bullet import Bullet
from settings import TILE_SIZE
from assets import player_img

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.bullets = []
        self.hp = 100

    def move(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
    
    def shoot(self, target_x, target_y):
        bullet = Bullet(self.x + TILE_SIZE // 2, self.y + TILE_SIZE // 2, target_x, target_y)
        self.bullets.append(bullet)

    def draw(self, screen):
        screen.blit(player_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)