import pygame

# Oyun penceresi boyutları
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Labirent haritası
LABIRENT = [
    "************",
    "*P*        *",
    "*  ******* *",
    "*  *     * *",
    "*  * *** * *",
    "*  * *   * *",
    "*    *   * *",
    "***********E",
]

# Kare boyutları
CELL_WIDTH = SCREEN_WIDTH // len(LABIRENT[0])
CELL_HEIGHT = SCREEN_HEIGHT // len(LABIRENT)

# Oyuncu karakterinin sınıfı
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CELL_WIDTH, CELL_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = CELL_HEIGHT
        self.speed = CELL_WIDTH

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y - self.speed >= 0:
            if LABIRENT[self.rect.y // CELL_HEIGHT - 1][self.rect.x // CELL_WIDTH] != "*":
                self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y + self.speed < SCREEN_HEIGHT:
            if LABIRENT[self.rect.y // CELL_HEIGHT + 1][self.rect.x // CELL_WIDTH] != "*":
                self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            if LABIRENT[self.rect.y // CELL_HEIGHT][self.rect.x // CELL_WIDTH - 1] != "*":
                self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x + self.speed < SCREEN_WIDTH:
            if LABIRENT[self.rect.y // CELL_HEIGHT][self.rect.x // CELL_WIDTH + 1] != "*":
                self.rect.x += self.speed

# Oyun başlatma
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Labirent Kaçış Oyunu")

# Oyuncu ve bitiş çizgisi
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

exit_x, exit_y = None, None

for row in range(len(LABIRENT)):
    for col in range(len(LABIRENT[0])):
        if LABIRENT[row][col] == "P":
            player.rect.x = col * CELL_WIDTH
            player.rect.y = row * CELL_HEIGHT
        if LABIRENT[row][col] == "E":
            exit_x, exit_y = col * CELL_WIDTH, row * CELL_HEIGHT

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player.rect.x == exit_x and player.rect.y == exit_y:
        print("Oyunu kazandınız!")
        running = False

    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
