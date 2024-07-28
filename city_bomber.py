import pygame
import time
import random
import sys

pygame.init()
clock = pygame.time.Clock()
exit = True 
screen = pygame.display.set_mode((800, 600))
bombs = []
towers = []
x = 10

class Bomb:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.bombrect = pygame.Rect(self.x,self.y,35,35)
    def move(self):
        self.y += 1
        self.bombrect = pygame.Rect(self.x,self.y,5,10)
    def render(self, screen):
        pygame.draw.rect(screen,(0,0,0),self.bombrect)

class Plane:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,direction):
        self.x += direction
        self.planerect = pygame.Rect(self.x,self.y,40,20)

    def render(self,screen):
        pygame.draw.rect(screen,(0,0,0),self.planerect)

class Towers:
    def __init__(self,x,y):
        height = random.randint(100,500)
        self.x = x
        self.y = y - height
        self.height = height

        print(self.x, self.y, 40, self.height)
        self.towerrect = pygame.Rect(self.x,self.y, 40, self.height)

    def hit(self):
        self.y += random.randint(20,30)
        self.towerrect = pygame.Rect(self.x,self.y,40, self.height)

    def render(self):
        pygame.draw.rect(screen,(255,0,0),self.towerrect)

for i in range(10):
        x += 60
        towers.append(Towers(x,600))


player = (Plane(0,0))
towersdestroyed = 0
while exit:

    clock.tick(100)
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bombs.append(Bomb(player.x + 20,player.y +20))
                #time.sleep(2)

    if player.x <= 0:
        player.move(1)
        moveright = True
        moveleft = False
        player.y += 35

    elif player.x >= 760:
        player.move(-1)
        moveleft = True
        moveright = False
        player.y += 35

    else:
        if moveright:
            player.move(1)
        if moveleft:
            player.move(-1)
    for tower in towers:
        if player.planerect.colliderect(tower.towerrect):
            pygame.quit()
            sys.exit()

    player.render(screen)
    for tower in towers:
        tower.render()

    for bomb in bombs:
        bomb.move()
        bomb.render(screen)

    for bomb in bombs:
        bombrect = bomb.bombrect
        for tower in towers:
            if bombrect.colliderect(tower.towerrect):
                tower.hit()
                bombs.remove(bomb)

    for tower in towers:
        if tower.y >= 600:
            towers.remove(tower)
            towersdestroyed += 1
            print(towersdestroyed)
    if towersdestroyed == 10:
        font = pygame.font.SysFont('Arial', 32)
        text = font.render(("Game Complete!"), True, (0,0,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (400 // 2, 400 // 2)
        screen.blit(text, textRect)        
            
    pygame.display.flip()