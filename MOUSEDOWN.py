import pygame
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Paint program")
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))

x=500
y=500
erasery = 100
eraserx = 100
erasercol = (0,0,0)
colour = (0,0,255)
sizedownx = 55
sizedowny = 145
sizeupx = 100
sizeupy = 145
brushsizex = 20
brushsizey = 20
eraserchoice = False
exit = True
eraserbutton = True

while exit:
    
    clock.tick(1000000000000)
    surface = pygame.Surface((x,y))
    
    if eraserchoice == True:
        pygame.draw.rect(screen, (erasercol), pygame.Rect(x, y, brushsizex, brushsizey))
        
    if eraserchoice == False:
        pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(x, y, brushsizex, brushsizey))
   
    pygame.draw.rect(screen, eraserbutton, pygame.Rect(eraserx, erasery, 40, 40))
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(sizedownx,sizedowny, 40, 40))
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(sizeupx,sizeupy, 40, 40))

    surfacerect = pygame.Rect(x, y,brushsizex,brushsizey)
    eraserrect = pygame.Rect(eraserx, erasery, 40, 40)
    sizedownrect = pygame.Rect(sizedownx, sizedowny, 40, 40)
    sizeuprect = pygame.Rect(sizeupx, sizeupy, 40, 40)

    for event in pygame.event.get():
        position = pygame.mouse.get_pos()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sizedownrect.collidepoint(position):
                eraserbutton = (40,40,40)
                brushsizex = brushsizex - 1
                brushsizey = brushsizey - 1

            if sizeuprect.collidepoint(position):
                brushsizex = brushsizex + 1
                brushsizey = brushsizey + 1

            if eraserrect.collidepoint(position):
                eraserbutton = (30,30,30)
                if eraserchoice == True:
                    eraserchoice = False
                elif eraserchoice == False:
                    eraserchoice = True

        if event.type == pygame.MOUSEBUTTONUP:
            if eraserrect.collidepoint(position):
                eraserbutton = (50,50,50)
                
        if event.type == pygame.QUIT: 
            exit = False

    x = position[0]
    y = position[1]
    
    pygame.display.update()
    
        