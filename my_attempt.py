import pygame 
import random
pygame.init() 
colour = (17,166,255)
colour2 = (1,2,3)
colour3 = (255,220,255)
# CREATING CANVAS 
canvas = pygame.display.set_mode((500, 500)) 
  
# TITLE OF CANVAS 
pygame.display.set_caption("sdfg") 
exit = True
canvas.fill(colour)

while exit: 
    
    #sets the colour of the canvas
    pygame.draw.rect(canvas, colour2,pygame.Rect(50,50,120,60))
    for event in pygame.event.get(): 

        if event.type == pygame.QUIT: 
            exit = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                co = random.randint(50,500)
                co2 = random.randint(50,500)
                pygame.draw.circle(canvas,colour3,(co2,co),30)
                pygame.display.set_caption("hi james")
            if event.key == pygame.K_z:
                pygame.display.set_caption("hi zach")
        
    pygame.display.update()