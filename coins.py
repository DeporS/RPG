import pygame
from assets import coins_one_img, coins_two_img, coins_four_img
from settings import TILE_SIZE


class Coins:
    def __init__(self, x, y, amount, pic):
        self.x = x
        self.y = y
        self.amount = amount
        self.collected = False

        if pic == 0:
            self.pic = coins_one_img
        elif pic == 1:
            self.pic = coins_two_img
        else:
            self.pic = coins_four_img

    def check_collection(self, player):
        x = TILE_SIZE
        if abs(self.x - player.x) < x and abs(self.y - player.y) < x and self.collected == False:
            player.collect_coin(self.amount)
            self.collected = True

    def draw(self, screen):
        # Draw dropped coins
        screen.blit(self.pic, (self.x, self.y))
