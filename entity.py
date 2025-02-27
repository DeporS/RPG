import random
import pygame
from settings import TILE_SIZE
from assets import entity_img
from damage_text import DamageText
from name_text import NameText
from utils import check_collision
import math
import time

# damage texts
all_damage_texts = []

class Entity:
    def __init__(self, x, y, hp=20, dmg=5, name="Goblin", lvl=1):
        self.x = x
        self.y = y
        self.starting_x = x
        self.starting_y = y
        self.speed = 2
        self.hp = hp
        self.max_hp = hp
        self.dmg = dmg
        self.name = name
        self.lvl = lvl

        self.last_attack_time = 0
        self.attack_cooldown = 2

        # Name
        self.name_text = NameText(self.x + TILE_SIZE // 2, self.y - 15, self.name, self.lvl)

    
    def move(self, player, mobs):
        # position difference to player
        dx = player.x - self.x
        dy = player.y - self.y

        # direction vector length
        length = math.sqrt(dx ** 2 + dy ** 2)

        if length > self.speed: # move only if distance is greater than speed
            # change length to unit vector (1)
            dx = (dx / length) * self.speed
            dy = (dy / length) * self.speed

            # Potential new moves
            new_x = self.x + dx
            new_y = self.y + dy

            # returns mob coliding with this one
            colliding_mob = check_collision(self, player, mobs, new_x, new_y)

            if not colliding_mob:
                self.x = new_x
                self.y = new_y
            else:
                # moving sideways or upside down to avoid collision
                if check_collision(self, player, mobs, self.x + dx, self.y) is None:
                    self.x += dx
                elif check_collision(self, player, mobs, self.x, self.y + dy) is None:
                    self.y += dy


        # Deal damage to player when within x radius
        x = TILE_SIZE + 5 # One tile plus 5, meaning max 9 mobs can hit player while surrounding him
        if abs(self.x - player.x) < x and abs(self.y - player.y) < x:
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
        
