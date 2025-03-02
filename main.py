import pygame
from settings import FPS, WHITE, screen
from player import Player
from entity import Entity, all_damage_texts
from goblin import Goblin
from ui import draw_health_bar, draw_player_gold
from coins import Coins
import database
import random
import time

pygame.init()

player = Player(400, 300)

# Creates tables if dont exist
database.create_tables()

# Loads player if exist
player_data = database.load_player()
if player_data:
    player = Player(
        400, 300, 100, player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])
else:
    database.save_player("DeporS", 1, 0, 0)
    player_data = database.load_player()
    player = Player(
        400, 300, 100, player_data[0], player_data[1], player_data[2], player_data[3], player_data[4])

# Database saving
last_time = 0
time_interval = 2 * 1000  # Time between database updates


def update_database():
    database.update_player(player.id, player.nickname,
                           player.lvl, player.xp, player.gold)


# Spawn mobs
mobs = [
    Goblin(100, 100),
    Goblin(500, 100),
    Goblin(500, 500),
    Goblin(100, 500)
]

dead_mobs = []  # List of dead mobs needed for respawning
dropped_coins = []  # List of dropped coins from dead mobs


def update_mobs(respawn_time):
    '''Function for updating mobs'''
    global mobs, dead_mobs
    current_time = pygame.time.get_ticks()

    # Actions with dead mobs
    for mob in mobs[:]:
        if mob.hp <= 0:
            # Save respawn position and dead time
            dead_mobs.append((type(mob), mob.starting_x,
                             mob.starting_y, current_time))
            mobs.remove(mob)  # Remove from alive mobs

            # Drop coins
            drop_pic = random.choice(mob.gold_pic_options)
            dropped_coins.append(
                Coins(mob.x, mob.y, mob.gold_drop[drop_pic], drop_pic))

    # Respawning dead mobs after {respawn_time} seconds
    for mob_type, x, y, t in dead_mobs[:]:
        if current_time - t >= respawn_time * 1000:
            mobs.append(mob_type(x, y))
            dead_mobs.remove((mob_type, x, y, t))


running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()

    if current_time - last_time >= time_interval:
        update_database()
        last_time = current_time

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
    for coin in dropped_coins[:]:  # Iterate over copy to remove elements
        if coin.collected:  # Remove already collected
            dropped_coins.remove(coin)
        else:
            coin.check_collection(player)
            coin.draw(screen)

    # Player healthbar
    draw_health_bar(screen, player.hp, player.max_hp)

    # Player gold
    draw_player_gold(screen, player.gold)

    # Mobs take damage texts
    for text in all_damage_texts[:]:
        text.update()  # Update the floating text
        text.draw(screen)
        if text.alpha == 0:  # Remove the text when its faded
            all_damage_texts.remove(text)

    pygame.display.flip()

pygame.quit()
