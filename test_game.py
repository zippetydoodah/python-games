import pygame
import os
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
exit = True
x = 20
y = 20
width = 15
height = 15
move_up = False
move_right = False
move_left = False
move_down = False
collision_col = ((156, 90, 60))
collision = False


image_folder = "C:\\Users\\zacha_er3uo9\\coding\\pygame-example\\src\\python_pixilart"
slime_file = os.path.join(image_folder, "player_test_bigger.png")
background_file = os.path.join(image_folder, "background.png")
ground_file = os.path.join(image_folder, "ground.png")

player = pygame.image.load(slime_file).convert_alpha()
background_image = pygame.image.load(background_file).convert_alpha()
ground_image = pygame.image.load(ground_file).convert_alpha()

def move():
        global move_down
        global move_left
        global move_up
        global move_right

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
                move_down = False

            elif event.key == pygame.K_LEFT:
                move_left = True
                move_right = False

            elif event.key == pygame.K_RIGHT:
                move_right = True
                move_left = False
            elif event.key == pygame.K_DOWN:
                move_down = True
                move_up = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False

            elif event.key == pygame.K_RIGHT:
                move_right = False

            elif event.key == pygame.K_DOWN:
                move_down = False

            if event.key == pygame.K_UP:
                move_up = False

while exit:
    clock.tick(100)
    screen.fill((0, 0, 0))
    
    screen.blit(player, (x,y))
    screen.blit(background_image, (0,0))
    screen.blit(ground_image, (0,0))
    
    #places = [(player.hitrect.left,player.hitrect.top),(player.hitrect.left,player.hitrect.bottom),(player.hitrect.right,player.hitrect.bottom),(player.hitrect.right,player.hitrect.top)]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        move()

    if move_left:
        x -= 1
    if move_right:
        x += 1
    if move_up:
        y -= 1
    if move_down:
        y += 1
    
    collision = False
    tolerance = 5
    
    screen.blit(player,(x,y))
    for t in range(x, x + width, tolerance):
        for u in range(y, y + height, tolerance):
            
            colour = screen.get_at((t,u))
            if colour == collision_col:
                print(2)
                collision = True
                print(1)
                
    if collision:
        if move_down:
            y -= 1
        if move_up:
            y += 1
        if move_left:
            x += 1
        if move_right:
            x -= 1
        if move_down and move_left:
            y -= 1
            x += 1
        if move_up and move_left:
            y += 1
            x += 1
        if move_up and move_right:
            x -= 1
            y += 1
        if move_down and move_right:
            x -= 1
            y -= 1
        


    


    
    pygame.display.flip()
    