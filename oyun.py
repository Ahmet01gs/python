import pygame
import random

# Oyun alanı boyutları
WIDTH, HEIGHT = 640, 480

# Renkler
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Yılanın hızı ve başlangıç boyutu
SNAKE_SPEED = 15
SNAKE_SIZE = 20

# Oyun ekranını başlatma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")

# Yılanın başlangıç konumu ve hareket yönü
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_dx, snake_dy = 0, 0

# Yılanın vücudu
snake_body = [(snake_x, snake_y)]

# Yem başlangıç konumu
food_x, food_y = random.randint(0, WIDTH - SNAKE_SIZE), random.randint(0, HEIGHT - SNAKE_SIZE)

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy == 0:
                snake_dx, snake_dy = 0, -SNAKE_SIZE
            if event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dx, snake_dy = 0, SNAKE_SIZE
            if event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx, snake_dy = -SNAKE_SIZE, 0
            if event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx, snake_dy = SNAKE_SIZE, 0

    # Yılanın hareketi
    snake_x += snake_dx
    snake_y += snake_dy
    snake_body.insert(0, (snake_x, snake_y))

    # Yem yendiyse yeni yem oluşturma
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = random.randint(0, WIDTH - SNAKE_SIZE), random.randint(0, HEIGHT - SNAKE_SIZE)
    else:
        snake_body.pop()

    # Oyun alanını temizleme
    screen.fill(BLACK)

    # Yılanı çizme
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Yemi çizme
    pygame.draw.rect(screen, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    # Oyun ekranını güncelleme
    pygame.display.update()

    # Yılanın çarpışma kontrolü
    if (snake_x >= WIDTH or snake_x < 0) or (snake_y >= HEIGHT or snake_y < 0) or (snake_body[0] in snake_body[1:]):
        running = False

    # Oyun hızını ayarlama
    pygame.time.Clock().tick(SNAKE_SPEED)

# Oyun döngüsünden çıkınca pygame'i kapatma
pygame.quit()
