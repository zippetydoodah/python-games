import pygame
import sys
import math
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([900, 600])
exit_game = True
velocity = 0
friction = 0.07
player_x = 500
shoot = False
enemybullets = []
playerbullets = []
obstacles = []
upgrades = []
upgrade = False
timeup = 0

class Obstacle:
    def __init__(self):
        self.x = random.randint(5,895)
        self.y = 0
    def move(self):
        self.y += 2
    def render(self,screen):
        self.obrect = pygame.Rect(self.x,self.y,20,20)
        pygame.draw.rect(screen,(255,0,0),self.obrect)

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.bulletrect = pygame.Rect(self.x,self.y,10,15)

    def render(self,screen):
        self.bulletrect = pygame.Rect(self.x,self.y,10,15)
        pygame.draw.rect(screen,(0,255,255),self.bulletrect)

    def playermove(self):
        self.y -= 3
    def enemymove(self):
        self.y +=5

class Increasenumbullets:
    def __init__(self):
        self.x = random.randint(5, 895)
        self.y = 0

    def move(self):
        self.y += 1

    def render(self):
        self.uprect = pygame.Rect(self.x,self.y,30,30)
        pygame.draw.rect(screen,(0,0,255),self.uprect)

while exit_game:

    if upgrade:
        timeup += 0.1

        if timeup >= 100:
            upgrade = False
            timeup = 0

    upchance = random.randint(0,1000)
    clock.tick(100)
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            shoot = True
            
        elif event.type == pygame.MOUSEBUTTONUP:
            shoot = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                velocity = -5  
            elif event.key == pygame.K_d:
                velocity = 5  

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                velocity = 0 
            elif event.key == pygame.K_d:
                    velocity = 0

    if upchance == 10 and upgrade == False:
        upgrades.append(Increasenumbullets())

    if upgrade:
        pygame.draw.rect(screen,(0,0,255),pygame.Rect(880,580,40,40))
    for u in upgrades:
        u.move()
        u.render()

    if len(obstacles) <= 15:
        obstacles.append(Obstacle())

    if shoot:
        if upgrade:
            playerbullets.append(Bullet((player_x + 25),540))
            playerbullets.append(Bullet((player_x ),540))
        else:
            playerbullets.append(Bullet((player_x +10),540))

    for obstacle in obstacles:
        if obstacle.y >= 610:
            obstacles.remove(obstacle)
        obstacle.move()
    
    for bullet in playerbullets:
        if bullet.y <= 0:
            playerbullets.remove(bullet)
        bullet.playermove()

    for bullet in enemybullets:
        if bullet.y <= 0:
            enemybullets.remove(bullet)
        bullet.enemymove()
    if len(playerbullets) >= 1:
        shoot = False

    for enemy in obstacles:
        if enemy.x == player_x:
            enemybullets.append(Bullet(enemy.x, enemy.y))

    player_x += velocity
            
    if player_x < 0:
        player_x = 0
        velocity = 0
    elif player_x > 860:  
        player_x = 860
        velocity = 0

    player = pygame.Surface((35, 35))
    playerrect = pygame.Rect(player_x, 540, 35, 35)
    player.fill((0, 255, 0))
    screen.blit(player, (player_x, 540))

    for obstacle in obstacles:
        obstacle.render(screen)
    for bullet in enemybullets:
        bullet.render(screen)

    for bullet in playerbullets:
        bullet.render(screen)

    for obstacle in obstacles:
        if playerrect.colliderect(obstacle.obrect):
            pygame.quit()
            sys.exit()

    for u in upgrades:
        if playerrect.colliderect(u.uprect):
            upgrades.remove(u)
            upgrade = True

    for ebullet in enemybullets:
        if playerrect.colliderect(ebullet.bulletrect):
            pygame.quit()
            sys.exit()

    for bullet in playerbullets:
        bulletrect = bullet.bulletrect
        for obstacle in obstacles:
            if bulletrect.colliderect(obstacle.obrect) and bullet in playerbullets:
                obstacles.remove(obstacle)
                playerbullets.remove(bullet)
    
    pygame.display.flip()
