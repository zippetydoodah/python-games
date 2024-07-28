import pygame
import os

canvas = pygame.display.set_mode((1000, 800)) 
pygame.display.set_caption("sdfg") 
canvas.fill((255,255,255))
exit = True
image_directory = "C:\\Users\\zacha_er3uo9\\coding\\pygame-example\\src\\python_pixilart"

# Load the image using the full path
image_path = os.path.join(image_directory, "pixil-frame-0 (6).png")
pixilart_image = pygame.image.load(image_path).convert_alpha()
canvas.blit(pixilart_image, (500,500))

while exit: 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = False 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
        # Blit the loaded image onto the canvas at position (0, 0)
                canvas.blit(pixilart_image, (0, 0))
            

    pygame.display.update()

pygame.quit()