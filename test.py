import pygame
import sys

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([900, 600])

# Player rectangle
player_rect = pygame.Rect(50, 50, 35, 35)
velocity = 5

running = True
while running:
    clock.tick(10)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Move player rect to the right by 5 pixels
    
    new_player_rect = player_rect.move(velocity, 2)

    # Draw original and moved rect
    pygame.draw.rect(screen, (0, 255, 0), player_rect)
    pygame.draw.rect(screen, (255, 0, 0), new_player_rect)

    pygame.display.flip()
