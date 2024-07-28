import pygame
import time
import math
import random

pygame.init()
clock = pygame.time.Clock()
exit = True 
screen = pygame.display.set_mode((800, 600))


xcoords = 500  
ycoords = 0
holey = 200
holeheight = 250   
playerx = 100
playery = 100
velocity = 0
gravity = 0.0075 
score = 0

def wall(xcoords,holey,holeheight):
    wall = pygame.Surface((40,600))
    wall.fill((200,100,100))
    hole = pygame.Surface((xcoords,holey))
    hole.fill((0,0,0))

    if xcoords == 0:
        xcoords = 800
        holey = random.randint(0,600)
        holeheight = random.randint(200,400)
    else:
        xcoords = xcoords- 1 

    return hole, wall, xcoords, holey, holeheight


while exit:
    if xcoords == playerx:
        score += 1
    font = pygame.font.SysFont('Arial', 32)
    text = font.render("%s"%(score), True, (0,0,255), (255,0,0))
    textRect = text.get_rect()
    textRect.center = (400 // 2, 400 // 2)
 
    moveup = False
    clock.tick(400) 
    
    hole, walls, xcoords, holey, holeheight = wall(xcoords, holey, holeheight)
    player = pygame.Surface((40,40))
    # Separate wall and hole rectangles
    wallrect = pygame.Rect(xcoords, 0, 40, holey)
    holerect = pygame.Rect(xcoords, holey, 40,holeheight)
    
    pygame.draw.rect(screen, (200, 100, 100), (xcoords, holey + holeheight, 40, 600 - holey - holeheight))  # Draw lower wall

     

    playerrect = pygame.Rect(playerx,playery,40,40)
    player.fill((0,255,0))
    screen.fill((0,0,0))
    screen.blit(walls,(xcoords,ycoords))
    screen.blit(hole,(xcoords,holey))
    screen.blit(player,(playerx,playery))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = -1.5
  
    playery += velocity
    velocity += gravity

    if playerrect.colliderect(wallrect):
        if playerrect.colliderect(holerect):
            exit = True

        else:

            exit = False
            screen.blit(text, textRect) 
    pygame.display.flip()


font = pygame.font.SysFont('Arial', 32)
text = font.render("%s"%(score), True, (0,0,255), (255,0,0))
textRect = text.get_rect()
textRect.center = (400 // 2, 400 // 2)
time.sleep(2)