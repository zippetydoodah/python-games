import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Example: Filling the screen with white
    screen.fill((255, 255, 255))
    
    # Drawing a red rectangle
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(300, 300, 50, 50))
    
    # Checking the color of the pixel at (105, 105)
    pixel_color = screen.get_at((105, 105))
    print("Color of pixel at (105, 105):", pixel_color)

    pygame.display.flip()

pygame.quit()
sys.exit()
