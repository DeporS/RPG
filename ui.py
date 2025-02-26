import pygame
from settings import HEALTHBAR_HEIGHT, HEALTHBAR_WIDTH, WHITE, HEALTHBARPOS_X
from assets import healthbar_bg, healthbar_fill, font

def draw_health_bar(screen, health, max_health):
    """Draws healthbar"""
    x =  HEALTHBARPOS_X # X position
    y = screen.get_height() - HEALTHBAR_HEIGHT - 10  # down position

    health_ratio = health / max_health
    filled_width = int(HEALTHBAR_WIDTH * health_ratio)

    # draw bg
    screen.blit(healthbar_bg, (x, y))

    # draw fill
    screen.blit(healthbar_fill, (x, y), (0, 0, filled_width, HEALTHBAR_HEIGHT))

    # Render health values ex: "70/100"
    hp_text = f"{health} / {max_health}"
    text_surface = font.render(hp_text, True, WHITE) 
    text_x = x + HEALTHBAR_WIDTH // 2 - text_surface.get_width() // 2  # Center
    text_y = y + HEALTHBAR_HEIGHT // 2 - text_surface.get_height() // 2

    # Draw HP values
    screen.blit(text_surface, (text_x, text_y))