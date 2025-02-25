import pygame
from settings import RED, WHITE

class DamageText:
    def __init__(self, x, y, damage, who="Player"):
        self.x = x
        self.y = y
        self.damage = damage
        self.alpha = 255  # Opacity (starts fully visible)
        self.font = pygame.font.SysFont("None", 50)
        self.text = self.font.render('-' + str(damage), True, RED)
        self.text_rect = self.text.get_rect(center=(x, y))
        self.life_time = 60  # Time in frames for how long the damage text will float (about 1 second)

    def update(self):
        self.y -= 0.2  # Move upwards
        self.alpha -= 255/60  # Decrease opacity
        if self.alpha <= 0:
            self.alpha = 0
        self.text.set_alpha(self.alpha)  # Update the transparency
        
        # Update the text_rect position after modifying y
        self.text_rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)