import pygame
import random

# Oyun penceresi boyutları
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Oyuncu karakterinin sınıfı
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

# Meyve nesnenin sınıfı
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(0, SCREEN_HEIGHT // 2)

# Oyun başlatma
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Yakala Meyve")

# Oyuncu ve meyve grupları
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

fruits = pygame.sprite.Group()
for _ in range(10):
    fruit = Fruit()
    fruits.add(fruit)
    all_sprites.add(fruit)

# Oyun döngüsü
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hits = pygame.sprite.spritecollide(player, fruits, True)
    for fruit in hits:
        player.score += 1
        new_fruit = Fruit()
        fruits.add(new_fruit)
        all_sprites.add(new_fruit)

    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    if player.score >= 20:
        running = False

    clock.tick(60)

pygame.quit()
