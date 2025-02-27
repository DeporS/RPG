import pygame
from settings import FPS, WHITE, screen
from player import Player
from entity import Entity, all_damage_texts
from goblin import Goblin
from ui import draw_health_bar
from coins import Coins
import random

pygame.init()

player = Player(400, 300)

mobs = [
    Goblin(100, 100),
    Goblin(500, 100),
    Goblin(500, 500),
    Goblin(100, 500)
]

dead_mobs = [] # List of dead mobs needed for respawning
dropped_coins = [] # List of dropped coins from dead mobs

def update_mobs(respawn_time):
    '''Function for updating mobs'''
    global mobs, dead_mobs
    current_time = pygame.time.get_ticks()

    # Actions with dead mobs
    for mob in mobs[:]:
        if mob.hp <= 0:
            dead_mobs.append((type(mob), mob.starting_x, mob.starting_y, current_time)) # Save respawn position and dead time
            mobs.remove(mob) # Remove from alive mobs

            # Drop coins
            drop_pic = random.choice(mob.gold_pic_options)
            dropped_coins.append(Coins(mob.x, mob.y, mob.gold_drop[drop_pic], drop_pic))
    
    # Respawning dead mobs after {respawn_time} seconds
    for mob_type, x, y, t in dead_mobs[:]:
        if current_time - t >= respawn_time * 1000:
            mobs.append(mob_type(x, y))
            dead_mobs.remove((mob_type, x, y, t))


running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)

    # Events a
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.shoot(*pygame.mouse.get_pos())

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # All mobs
    for mob in mobs:
        # Follow player
        mob.move(player, mobs)

    # Deleting and respawning dead mobs
    update_mobs(5)
        

    # Bullets
    for bullet in player.bullets[:]:
        bullet.move()
        for mob in mobs:
            if bullet.collides_with(mob):
                mob.take_damage(player.damage, player.crit_chance)
                if bullet in player.bullets:
                    player.bullets.remove(bullet)

    

    """  Drawing  """ 
    screen.fill(WHITE)
    player.draw(screen)
    for mob in mobs:
        mob.draw(screen)
    for coin in dropped_coins:
        coin.draw(screen)

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
