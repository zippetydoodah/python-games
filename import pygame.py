import pygame
import random
pygame.init()
colour = (17,166,255)
target_colour = (255,220,255)
canvas = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption("sdfg") 

exit = True
while exit: 
    for event in pygame.event.get(): 
        canvas.fill(colour)
        
        
        pressedkeys = pygame.key.get_pressed()
        if not pressedkeys [pygame.K_LEFT]:
                colour5 = random.randint(1,255)
                colour4= random.randint(1,255)
                colour6= random.randint(1,255)
                circle = pygame.draw.circle(canvas,(colour4,colour5,colour6),(50,50),30)
        if pressedkeys[pygame.K_RIGHT]:
            circle = pygame.draw.circle(canvas,(123,123,123),(50,50),30)
        if target_colour == canvas.get_at((50,50)):
             print ("ww")
        if event.type == pygame.QUIT: 
            exit = False
    
    pygame.display.update()