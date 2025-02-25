import pygame
from settings import FPS, WHITE, screen
from player import Player
from entity import Entity
from utils import SpawnEntity

pygame.init()

player = Player(400, 300)
entity = Entity(600, 400)
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)

    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.shoot(*pygame.mouse.get_pos())

    # Ruch gracza
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Ruch wroga
    entity.move(player)

    # Ruch pocisków i kolizje
    for bullet in player.bullets[:]:
        bullet.move()
        if bullet.collides_with(entity):
            entity.take_damage(5)
            player.bullets.remove(bullet)

    # Spawn nowego przeciwnika, jeśli poprzedni zginął
    if entity.hp <= 0:
        entity = SpawnEntity()

    # Rysowanie elementów
    screen.fill(WHITE)
    player.draw(screen)
    entity.draw(screen)

    pygame.display.flip()

pygame.quit()
