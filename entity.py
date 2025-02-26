import random
import pygame
from settings import TILE_SIZE
from assets import entity_img
from damage_text import DamageText
from name_text import NameText
import math
import time

# damage texts
all_damage_texts = []

class Entity:
    def __init__(self, x, y, hp=20, dmg=5, name="Goblin", lvl=1):
        self.x = x
        self.y = y
        self.speed = 2
        self.hp = hp
        self.max_hp = hp
        self.dmg = dmg
        self.name = name
        self.lvl = lvl

        self.last_attack_time = 0
        self.attack_cooldown = 1

        # Name
        self.name_text = NameText(self.x + TILE_SIZE // 2, self.y - 15, self.name, self.lvl)

    
    def move(self, player):
        # position difference to player
        dx = player.x - self.x
        dy = player.y - self.y

        # direction vector length
        length = math.sqrt(dx ** 2 + dy ** 2)

        if length > self.speed: # move only if distance is greater than speed
            # change length to unit vector (1)
            dx = (dx / length) * self.speed
            dy = (dy / length) * self.speed

            # update position
            self.x += dx
            self.y += dy
        else:
            # if very close set to player x and y
            self.x = player.x
            self.y = player.y

            # make player take dmg every 1 sec
            current_time = time.time()
            if current_time - self.last_attack_time >= self.attack_cooldown:
                player.take_dmg(self.dmg)  # deal damage to the player
                self.last_attack_time = current_time
        
        # Update name position when mob moves
        self.name_text.update_position(self.x + TILE_SIZE // 2, self.y - 15)

    def take_damage(self, damage, crit_chance):
        # Take damage when attacked by player
        if crit_chance * 100 >= random.randint(0, 100):
            damage_text = DamageText(self.x, self.y, damage * 2, "Mob", True)
            self.hp -= damage * 2
        else:
            self.hp -= damage
            damage_text = DamageText(self.x, self.y, damage, "Mob")
        all_damage_texts.append(damage_text)
        
    def draw(self, screen):
        # Draw mob
        screen.blit(entity_img, (self.x, self.y))

        # Draw NameText above the mob
        self.name_text.draw(screen)

        # Draw healthbar
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, TILE_SIZE, 5))  # Background Bar
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 10, max(0, TILE_SIZE * (self.hp / self.max_hp)), 5)) # HP Bar
        
