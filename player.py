import pygame
from bullet import Bullet
from damage_text import DamageText
from settings import TILE_SIZE, HEALTHBAR_HEIGHT, HEALTHBAR_WIDTH, HEIGHT, HEALTHBARPOS_X
from assets import player_img
from name_text import NameText
import math


class Player:
    def __init__(self, x, y, hp=100, id=0, nickname="Newbie", lvl=1, xp=0, gold=0):
        self.id = id
        self.x = x
        self.y = y
        self.speed = 4
        self.bullets = []
        self.damage = 5
        self.crit_chance = 0.05
        self.hp = hp
        self.max_hp = hp
        self.damage_texts = []
        self.lvl = lvl
        self.xp = xp
        self.max_xp = 10
        self.gold = gold
        self.nickname = nickname

        # Nickname
        self.name_text = NameText(
            self.x + TILE_SIZE // 2, self.y - 10, self.nickname, self.lvl)

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

        # Update name position when player moves
        self.name_text.update_position(self.x + TILE_SIZE // 2, self.y - 10)

    def shoot(self, target_x, target_y):
        bullet = Bullet(self.x + TILE_SIZE // 4, self.y +
                        TILE_SIZE // 4, target_x, target_y)
        self.bullets.append(bullet)

    def take_dmg(self, dmg):
        self.hp -= dmg
        # Create damage text and add it to the list
        damage_text = DamageText(
            HEALTHBARPOS_X + HEALTHBAR_WIDTH + 20, HEIGHT - 10 - HEALTHBAR_HEIGHT // 2, dmg)
        self.damage_texts.append(damage_text)

    def collect_coin(self, amount):
        self.gold += amount

    def draw(self, screen):
        # Draw Player
        screen.blit(player_img, (self.x, self.y))

        # Draw NameText above the player
        self.name_text.draw(screen)

        # Draw player bullets
        for bullet in self.bullets:
            bullet.draw(screen)
        # Draw player dmg taken
        for text in self.damage_texts[:]:
            text.update()  # Update the floating text
            text.draw(screen)
            if text.alpha == 0:  # Remove the text when its faded
                self.damage_texts.remove(text)
