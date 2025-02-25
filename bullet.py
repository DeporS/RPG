import pygame
import math
from assets import fireball_img
from settings import TILE_SIZE

class Bullet:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.speed = 10
    
        direction_x = target_x - x
        direction_y = target_y - y
        length = math.sqrt(direction_x ** 2 + direction_y ** 2)

        if length != 0:
            self.dx = (direction_x / length) * self.speed
            self.dy = (direction_y / length) * self.speed
        else:
            self.dx = 0
            self.dy = 0
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def collides_with(self, entity):
        # Checks if it collides with anyone
        bullet_rect = pygame.Rect(self.x, self.y, 10, 10)
        entity_rect = pygame.Rect(entity.x, entity.y, TILE_SIZE, TILE_SIZE)
        return bullet_rect.colliderect(entity_rect)

    def draw(self, screen):
        screen.blit(fireball_img, (int(self.x), int(self.y)))