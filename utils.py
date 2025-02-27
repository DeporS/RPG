# File for other functions

import random
import pygame
from settings import TILE_SIZE
import math

def check_collision(one, player, others, new_x=None, new_y=None):
    """Checks if mobs collide with other mobs"""
    # For testing new moves
    if new_x is None:
        new_x = one.x
    if new_y is None:
        new_y = one.y


    for other in others:
        if one != other:
            if pygame.Rect(new_x, new_y, TILE_SIZE, TILE_SIZE).colliderect(pygame.Rect(other.x, other.y, TILE_SIZE, TILE_SIZE)):
                return other
    return None


def distance(entity1, entity2):
    """Checks distance between two mobs"""
    return math.sqrt((entity1.x - entity2.x) ** 2 + (entity1.y - entity2.y) ** 2)