import pygame
from assets import coins_one_img, coins_two_img, coins_four_img

class Coins:
    def __init__(self, x, y, amount, pic):
        self.x = x
        self.y = y
        self.amount = amount
        

        if pic == 0:
            self.pic = coins_one_img
        elif pic == 1:
            self.pic = coins_two_img
        else:
            self.pic = coins_four_img
    
    def draw(self, screen):
        # Draw dropped coins
        screen.blit(self.pic, (self.x, self.y))