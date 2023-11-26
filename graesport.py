import pygame
import random
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 800, 600
FPS = 60

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ustawienia gracza
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Ustawienia przeszkód
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5

# Inicjalizacja okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prosta Gra Esportowa")

# Funkcja rysująca gracza
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_width, player_height])

# Funkcja rysująca przeszkodę
def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, [x, y, obstacle_width, obstacle_height])

# Funkcja główna gry
def game():
    clock = pygame.time.Clock()

    obstacles = []
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Dodawanie przeszkód
        if random.randint(0, 100) < 5:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = 0
            obstacles.append([obstacle_x, obstacle_y])

        # Ruch przeszkód
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if obstacle[1] > HEIGHT:
                obstacles.remove(obstacle)
                score += 1

        # Sprawdzenie kolizji z graczem
        for obstacle in obstacles:
            if (
                player_x < obstacle[0] + obstacle_width
                and player_x + player_width > obstacle[0]
                and player_y < obstacle[1] + obstacle_height
                and player_y + player_height > obstacle[1]
            ):
                print("Game Over! Your score:", score)
                pygame.quit()
                sys.exit()

        # Wyczyszczenie ekranu
        screen.fill((0, 0, 0))

        # Rysowanie gracza i przeszkód
        draw_player(player_x, player_y)
        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])

        pygame.display.flip()

        # Ustawienie liczby klatek na sekundę
        clock.tick(FPS)

# Rozpoczęcie gry
game()
