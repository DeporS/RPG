import pygame
from settings import TILE_SIZE
from assets import entity_img
import math

class Entity:
    def __init__(self, x, y, hp=20):
        self.x = x
        self.y = y
        self.speed = 2
        self.hp = hp
        self.max_hp = hp
    
    def move(self, player):
        # position difference to player
        dx = player.x - self.x
        dy = player.y - self.y

        # direction vector length
        length = math.sqrt(dx ** 2 + dy ** 2)

        if length != 0:
            # change length to unit vector (1)
            dx = (dx / length) * self.speed
            dy = (dy / length) * self.speed

            # update position
            self.x += dx
            self.y += dy

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("Im dead!!!")
        
    def draw(self, screen):
        screen.blit(entity_img, (self.x, self.y))
        # Healthbar
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, TILE_SIZE, 5))  # Background Bar
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 10, max(0, TILE_SIZE * (self.hp / self.max_hp)), 5)) # HP Bar