# File for other functions

import random
from entity import Entity

def SpawnEntity(mob):
    return Entity(random.randint(0, 800), random.randint(0, 600))
