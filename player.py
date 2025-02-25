import pygame
from bullet import Bullet
from damage_text import DamageText
from settings import TILE_SIZE, HEALTHBAR_HEIGHT, HEALTHBAR_WIDTH, HEIGHT
from assets import player_img
import math

class Player:
    def __init__(self, x, y, hp=100):
        self.x = x
        self.y = y
        self.speed = 4
        self.bullets = []
        self.hp = hp
        self.max_hp = hp
        self.damage_texts = []

    def move(self, keys):
        diagonal_speed = self.speed / math.sqrt(2)  # diagonal run

        dx, dy = 0, 0
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_d]:
            dx += self.speed
        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed

        #  while holding two keys
        if dx != 0 and dy != 0:
            dx *= diagonal_speed / self.speed
            dy *= diagonal_speed / self.speed

        self.x += dx
        self.y += dy
    
    def shoot(self, target_x, target_y):
        bullet = Bullet(self.x + TILE_SIZE // 4, self.y + TILE_SIZE // 4, target_x, target_y)
        self.bullets.append(bullet)
    
    def take_dmg(self, dmg):
        self.hp -= dmg
        # Create damage text and add it to the list
        damage_text = DamageText(30 + HEALTHBAR_WIDTH, HEIGHT - 10 - HEALTHBAR_HEIGHT // 2, dmg)
        self.damage_texts.append(damage_text)

    def draw(self, screen):
        # Draw Player
        screen.blit(player_img, (self.x, self.y))
        # Draw player bullets
        for bullet in self.bullets:
            bullet.draw(screen)
        # Draw player dmg taken
        for text in self.damage_texts[:]:
            text.update()  # Update the floating text
            text.draw(screen)
            if text.alpha == 0:  # Remove the text when its faded
                self.damage_texts.remove(text)
    
    
    