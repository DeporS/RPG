import pygame
import math

pygame.init()

NAME = "MY RPG"

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 32
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)

# Loading assets
player_img = pygame.image.load("Assets/player.png") 
player_img = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))
entity_img = pygame.image.load("Assets/enemy.png")
entity_img = pygame.transform.scale(entity_img, (TILE_SIZE, TILE_SIZE))
fireball_img = pygame.image.load("Assets/fireball.png")
fireball_img = pygame.transform.scale(fireball_img, (20, 20))

# Player Class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.bullets = []
        self.hp = 100

    def move(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
    
    def shoot(self, target_x, target_y):
        bullet = Bullet(self.x + TILE_SIZE // 2, self.y + TILE_SIZE // 2, target_x, target_y)
        self.bullets.append(bullet)

    def draw(self, screen):
        screen.blit(player_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)


class Entity:
    def __init__(self, x, y, hp=20):
        self.x = x
        self.y = y
        self.speed = 3
        self.hp = hp
        
    def draw(self, screen):
        screen.blit(entity_img, (self.x, self.y))


class Bullet:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.speed = 10
    
        direction_x = target_x - x
        direction_y = target_y - y
        length = math.sqrt(direction_x ** 2 + direction_y ** 2)

        if length != 0:
            self.dx = (direction_x / length) * self.speed
            self.dy = (direction_y / length) * self.speed
        else:
            self.dx = 0
            self.dy = 0
    
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        screen.blit(fireball_img, (int(self.x), int(self.y)))

# Player init
player = Player(WIDTH // 2, HEIGHT // 2)
entity = Entity(600, 400)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                player.shoot(mouse_x, mouse_y)
    
    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Update bullets
    for bullet in player.bullets:
        bullet.move()
    
    # Drawing
    screen.fill(WHITE)
    player.draw(screen)
    entity.draw(screen)
    pygame.display.flip()

pygame.quit()
