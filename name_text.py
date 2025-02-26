import pygame
from settings import RED, WHITE, BLACK

class NameText:
    def __init__(self, x, y, nickname, lvl):
        self.x = x
        self.y = y
        self.nickname = nickname
        self.lvl = lvl
        self.font = pygame.font.SysFont("None", 15)
        self.text = self.font.render(nickname + " lvl. " + str(lvl), True, BLACK)
        self.text_rect = self.text.get_rect(center=(x, y))
    
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)