import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Endless Mini-Game')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Game settings
player_size = 50
player_speed = 5
enemy_size = 50
enemy_speed = 2
enemy_spawn_rate = 30  # Every 30 frames, a new enemy spawns

# Initialize player
player = pygame.Rect(screen_width // 2 - player_size // 2, screen_height - player_size - 10, player_size, player_size)

# List of enemies
enemies = []

# Game loop
running = True
score = 0
frame_count = 0

while running:
    screen.fill(BLACK)
    frame_count += 1

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < screen_width:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < screen_height:
        player.y += player_speed

    # Spawn enemies
    if frame_count % enemy_spawn_rate == 0:
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemies.append(pygame.Rect(enemy_x, -enemy_size, enemy_size, enemy_size))

    # Move enemies and check collisions
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.colliderect(player):
            running = False  # Game over on collision
        if enemy.top > screen_height:
            enemies.remove(enemy)
            score += 1  # Increase score when enemy goes off screen

    # Draw player
    pygame.draw.rect(screen, WHITE, player)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, enemy)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
