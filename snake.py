import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)



# Screen dimensions
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Game variables
cell_size = 20
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction_idx = 0
snake = [(5, 5), (5, 6), (5, 7)]
food = (random.randint(0, (WIDTH // cell_size) - 1), random.randint(0, (HEIGHT // cell_size) - 1))

running = True
while running:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction_idx != 2:
                direction_idx = 0
            elif event.key == pygame.K_RIGHT and direction_idx != 3:
                direction_idx = 1
            elif event.key == pygame.K_DOWN and direction_idx != 0:
                direction_idx = 2
            elif event.key == pygame.K_LEFT and direction_idx != 1:
                direction_idx = 3
    
    # Move snake
    head = snake[0]
    new_head = ((head[0] + directions[direction_idx][0]) % (WIDTH // cell_size), 
                (head[1] + directions[direction_idx][1]) % (HEIGHT // cell_size))
    snake = [new_head] + snake[:-1]
    
    # Check for food collision
    if new_head == food:
        snake.append(snake[-1])
        food = (random.randint(0, (WIDTH // cell_size) - 1), random.randint(0, (HEIGHT // cell_size) - 1))
    
    # Check for self collision
    if new_head in snake[1:]:
        running = False
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))
    
    # Draw food
    pygame.draw.rect(screen, RED, (food[0] * cell_size, food[1] * cell_size, cell_size, cell_size))
    
    pygame.display.flip()
    
    pygame.time.Clock().tick(10)

pygame.quit()