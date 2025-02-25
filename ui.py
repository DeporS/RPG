import pygame
from settings import HEALTHBAR_HEIGHT, HEALTHBAR_WIDTH
from assets import healthbar_bg, healthbar_fill

def draw_health_bar(screen, health, max_health):
    """Draws healthbar left down corner"""
    x = 10  # left position
    y = screen.get_height() - HEALTHBAR_HEIGHT - 10  # down position

    health_ratio = health / max_health
    filled_width = int(HEALTHBAR_WIDTH * health_ratio)

    # draw bg
    screen.blit(healthbar_bg, (x, y))

    # draw fill
    screen.blit(healthbar_fill, (x, y), (0, 0, filled_width, HEALTHBAR_HEIGHT))