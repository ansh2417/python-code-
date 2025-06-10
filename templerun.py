import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Temple Run - Basic Runner")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

player = pygame.Rect(100, 300, 50, 50)
player_velocity = 0
jumping = False

obstacles = []
SPAWN_OBSTACLE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_OBSTACLE, 1500)

ground_y = 350

score = 0

def display_text(text, x, y, color):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def reset_game():
    global player, player_velocity, jumping, obstacles, score
    player.y = 300
    player_velocity = 0
    jumping = False
    obstacles.clear()
    score = 0

running = True
game_over = False

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SPAWN_OBSTACLE and not game_over:
            obstacle = pygame.Rect(WIDTH, ground_y - 50, 50, 50)
            obstacles.append(obstacle)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping and not game_over:
                player_velocity = -15
                jumping = True
            if event.key == pygame.K_r and game_over:
                reset_game()
                game_over = False

    if not game_over:
        player_velocity += 1
        player.y += player_velocity

        if player.y >= 300:
            player.y = 300
            jumping = False

        for obs in obstacles:
            obs.x -= 6

        obstacles = [obs for obs in obstacles if obs.x > -50]

        for obs in obstacles:
            if player.colliderect(obs):
                game_over = True

        score += 1

    pygame.draw.rect(screen, GREEN, (0, ground_y, WIDTH, HEIGHT - ground_y))

    pygame.draw.rect(screen, BLUE, player)
    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)

    display_text(f"Score: {score // 10}", 10, 10, (0, 0, 0))

    if game_over:
        display_text("GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 30, RED)
        display_text("Press R to Restart", WIDTH // 2 - 130, HEIGHT // 2 + 10, RED)

    pygame.display.update()
    clock.tick(60)
