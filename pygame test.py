import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
move_up = False
move_right = False
move_left = False
move_down = False
exit = True
colour = (100,100,100)
x = 100
y = 100
gravity = 25
while exit:

    clock.tick(200)
    player = pygame.Surface((40, 40))
    hitrect = pygame.Surface((70, 70))

    player.fill((100,100,100))
    hitrect.fill((100,100,100))
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (100,100,100), pygame.Rect(50, 50, 40, 1000))
    screen.blit(player,(x,y))

    playerrect = pygame.Rect(x,y,40,40)
    hitrect = pygame.Rect(50,50,40,1000)
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


               
    if playerrect.colliderect(hitrect) and move_left == True:
            move_left = False
    if move_left:
        x -= 1  
    elif playerrect.colliderect(hitrect) and move_right == True:
            move_right = False
    elif playerrect.colliderect(hitrect) and move_down == True:
            move_down = False    
    elif playerrect.colliderect(hitrect) and move_up == True:
            move_up = False  
     

    if move_left:
        x -= 1
    if move_right:
        x += 1
    if move_up:
        y -= 1
    if move_down:
        y += 1

    pygame.display.flip()
