import pygame
import time
pygame.init()
exit = True

screen = pygame.display.set_mode((800, 600))

surface = pygame.Surface((500, 300))
surface.fill((255,1,1))
screen.blit(surface, (0,0))
xcoord = 50
ycoord = 50

def wall(ycoord,xcoord,keypressed):

    newsurface = pygame.Surface((10,10))
    newsurface.fill((200,100,100))

    if keypressed == "Kleft":
        xcoord = xcoord - 10
    if keypressed == "Kup":
        ycoord = ycoord + 10
    if keypressed == "Kdown":
        ycoord = ycoord - 10
    if keypressed == "Kright":
        xcoord = xcoord + 10
        
    return newsurface, xcoord, ycoord, 

while exit:
    

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                keypressed = "Kleft"
                newsurface, xcoord, ycoord = wall(ycoord, xcoord, keypressed)
                screen.fill((0,0,0))
                screen.blit(newsurface,(xcoord,ycoord))
                pygame.display.flip()

            if event.key == pygame.K_RIGHT:
                keypressed = "Kright"
                newsurface, xcoord, ycoord = wall(ycoord, xcoord, keypressed)
                screen.fill((0,0,0))
                screen.blit(newsurface,(xcoord,ycoord))
                pygame.display.flip()

            if event.key == pygame.K_DOWN:
                keypressed = "Kup"
                newsurface, xcoord, ycoord = wall(ycoord, xcoord, keypressed)
                screen.fill((0,0,0))
                screen.blit(newsurface,(xcoord,ycoord))
                pygame.display.flip()

            if event.key == pygame.K_UP:
                keypressed = "Kdown"
                newsurface, xcoord, ycoord = wall(ycoord, xcoord, keypressed)
                screen.fill((0,0,0))
                screen.blit(newsurface,(xcoord,ycoord))
                pygame.display.flip()
       
        if event.type == pygame.QUIT: 
            exit = False
