from entity import Entity

class Goblin(Entity):
    def __init__(self, x, y, hp=20, dmg=5, name="Goblin", lvl=3):
        super().__init__(x, y, hp, dmg, name, lvl)