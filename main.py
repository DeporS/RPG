import pygame
from settings import FPS, WHITE, screen
from player import Player
from entity import Entity, all_damage_texts
from utils import SpawnEntity
from ui import draw_health_bar

pygame.init()

player = Player(400, 300)
entity = Entity(600, 400)
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)

    # Events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.shoot(*pygame.mouse.get_pos())

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Entity movement
    entity.move(player)

    # Bullets
    for bullet in player.bullets[:]:
        bullet.move()
        if bullet.collides_with(entity):
            entity.take_damage(player.damage, player.crit_chance)
            player.bullets.remove(bullet)

    # Spawn new entity
    if entity.hp <= 0:
        entity = SpawnEntity()

    # Drawing   
    screen.fill(WHITE)
    player.draw(screen)
    entity.draw(screen)

    # Player healthbar
    draw_health_bar(screen, player.hp, player.max_hp)

    # Mobs take damage texts
    for text in all_damage_texts[:]:
        text.update()  # Update the floating text
        text.draw(screen)
        if text.alpha == 0:  # Remove the text when its faded
            all_damage_texts.remove(text)

    pygame.display.flip()

pygame.quit()
