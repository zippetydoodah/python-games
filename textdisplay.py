import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
exit = True
font = pygame.font.SysFont('Arial', 32)
text = font.render('hello paul ', True, (0,0,255), (255,0,0))
textRect = text.get_rect()
textRect.center = (400 // 2, 400 // 2)

while exit:
    screen.fill((0,0,0))
    screen.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit = False
            
    pygame.display.update()