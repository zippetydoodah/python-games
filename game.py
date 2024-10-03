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


image_folder = "C:\\Users\\zacha_er3uo9\\coding\\pygame-example\\src\\python_pixilart"
slime_file = os.path.join(image_folder, "player_test_bigger.png")
background_file = os.path.join(image_folder, "background.png")
ground_file = os.path.join(image_folder, "ground.png")

slime_image = pygame.image.load(slime_file).convert_alpha()
background_image = pygame.image.load(background_file).convert_alpha()
ground_image = pygame.image.load(ground_file).convert_alpha()




while exit:
# Load the image using the full path
    screen.blit(slime_image, (500,500))
    screen.blit(background_image, (0,0))
    screen.blit(ground_image, (0,0))
    
    color_at_pixel = screen.get_at((x, y))
    print(color_at_pixel)
    hitrect = pygame.Surface((70, 70))
    hitrect.fill((100,100,100))
    #screen.fill((0,0,0))
    screen.blit(ground_image, (0,0))

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(1, 800, 800, 40))
    screen.blit(slime_image,(x,y))

    playerrect = pygame.Rect(x,y, slime_image.get_width(), slime_image.get_height())
    hitrect_pixilart3 = pygame.Rect(0, 0, ground_image.get_width(), ground_image.get_height())
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
        if move_left and not playerrect.colliderect(hitrect_pixilart3.move(-5, 0)):
            x += 2
        elif move_right and not playerrect.colliderect(hitrect_pixilart3.move(5, 0)):
            x -= 2
        elif move_up and not playerrect.colliderect(hitrect_pixilart3.move(0, -5)):
            y += 2
        elif move_down and not playerrect.colliderect(hitrect_pixilart3.move(0, 5)):
            move_down = False
            y -= 2
        
        
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