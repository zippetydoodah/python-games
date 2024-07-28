import pygame
import os
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
exit = True
x = 20
y = 20
move_up = False
move_right = False
move_left = False
move_down = False

while exit:
    

    slimecharacter = "C:\\Users\\zacha_er3uo9\\coding\\pygame-example\\src\\python_pixilart"
    background = "C:\\Users\\zacha_er3uo9\\coding\\pygame-example\\src\\python_pixilart"
    ground = "C:\\Users\\zacha_er3uo9\\coding\\pygame-example\\src\\python_pixilart"

# Load the image using the full path
    image_path = os.path.join(slimecharacter, "pixil-frame-0 (9).png")
    image_path2 = os.path.join(background, "pixil-frame-0 (11) background.png")
    image_path3 = os.path.join(ground, "pixil-frame-0 (12) ground.png")

    pixilart_image = pygame.image.load(image_path).convert_alpha()
    pixilart_image2 = pygame.image.load(image_path2).convert_alpha()
    pixilart_image3 = pygame.image.load(image_path3).convert_alpha()

    screen.blit(pixilart_image, (500,500))
    screen.blit(pixilart_image2, (0,0))
    screen.blit(pixilart_image3, (0,0))
    

    hitrect = pygame.Surface((70, 70))
    hitrect.fill((100,100,100))
    screen.fill((0,0,0))
    screen.blit(pixilart_image3, (0,0))

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(1, 800, 800, 40))
    screen.blit(pixilart_image,(x,y))

    playerrect = pygame.Rect(x,y, pixilart_image.get_width(), pixilart_image.get_height())
    hitrect_pixilart3 = pygame.Rect(0, 0, pixilart_image3.get_width(), pixilart_image3.get_height())
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                move_up = True
                move_right = False
                move_left = False
                move_down = False

            elif event.key == pygame.K_LEFT:
                move_left = True
                move_up = False
                move_right = False
                move_down = False

            elif event.key == pygame.K_RIGHT:
                move_right = True
                move_up = False
                move_left = False
                move_down = False

            elif event.key == pygame.K_DOWN:
                move_down = True
                move_up = False
                move_right = False
                move_left = False
        # Update player's position based on movement flags
    

    if playerrect.colliderect(hitrect_pixilart3):
        if move_left and not playerrect.colliderect(hitrect_pixilart3.move(-1, 0)):
            x += 1
        elif move_right and not playerrect.colliderect(hitrect_pixilart3.move(1, 0)):
            x -= 1
        elif move_up and not playerrect.colliderect(hitrect_pixilart3.move(0, -1)):
            y += 1
        elif move_down and not playerrect.colliderect(hitrect_pixilart3.move(0, 1)):
            y -= 1
        
    if move_left:
        x -= 1
    if move_right:
        x += 1
    if move_up:
        y -= 1
    if move_down:
        y += 1

    # Move the player away from the collision while considering the intended direction
        
    pygame.display.update()