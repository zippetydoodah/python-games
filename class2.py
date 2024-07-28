import random
import pygame
pygame.init()
clock = pygame.time.Clock()
canvas = pygame.display.set_mode((700,700)) 
pygame.display.set_caption("sdfg") 

class Makesquare:
    def __init__(self):
        self.x = random.randint(0,700)
        self.y = random.randint(0,700)
        pygame.draw.rect(canvas, (0, 0, 100), pygame.Rect(self.x, self.y, 1, 1))
        pygame.draw.rect(canvas, (100,0,0), pygame.Rect(self.y, self.x, 1, 1))
        self.x = random.randint(0,700)
        self.y = random.randint(0,700)
        pygame.draw.rect(canvas, (0,100,0), pygame.Rect(self.x, self.y, 1, 1))
        pygame.draw.rect(canvas, (100,100,100), pygame.Rect(self.y, self.x, 1, 1))
        return

e = True
while e:
    Makesquare()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            e = False
    pygame.display.update()
