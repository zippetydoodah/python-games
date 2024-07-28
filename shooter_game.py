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
bullets = []
obstacles = []

class Obstacle:
    def __init__(self):
        self.x = random.randint(10,890)
        self.y = 0
    def move(self):
        self.y += 2
    def render(self,screen):
        self.obrect = pygame.Rect(self.x,self.y,20,20)
        pygame.draw.rect(screen,(255,0,0),self.obrect)

class Bullet:
    def __init__(self,x,y,destination):
        self.destination = destination
        self.x = x
        self.y = y
        self.speed = 4
        self.bulletrect = pygame.Rect(self.x,self.y,15,15)

        self.dx = self.destination[0]- self.x
        self.dy = self.destination[1] - self.y
        self.hyp = math.sqrt((self.dx * self.dx) + (self.dy * self.dy))

    def render(self,screen):
        self.bulletrect = pygame.Rect(self.x,self.y,10,15)
        pygame.draw.rect(screen,(0,255,0),self.bulletrect)

    def move(self):
    
        self.x += (self.dx / self.hyp * self.speed)
        self.y += (self.dy / self.hyp * self.speed)



while exit_game:
    clock.tick(100)  
    screen.fill((255, 255, 255))
    if len(obstacles) <= 10:
        obstacles.append(Obstacle())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            shoot = True
            pos = event.pos
            #bullets.append(Bullet((player_x + 20),540,event.pos))
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
    if shoot:
        bullets.append(Bullet((player_x + 20),540,pos))

    for obstacle in obstacles:
        if obstacle.y >= 610:
            obstacles.remove(obstacle)
        obstacle.move()
    
    for bullet in bullets:
        if bullet.x >= 920 or bullet.x <= 0 or bullet.y >= 610 or bullet.y <= 0:
            bullets.remove(bullet)
        bullet.move()

    if len(bullets) >= 1:
        shoot = False


    player_x += velocity
            
    if player_x < 0:
        player_x = 0
        velocity = 0
    elif player_x > 860:  
        player_x = 860
        velocity = 0

    player = pygame.Surface((40, 40))
    playerrect = pygame.Rect(player_x, 540, 40, 40)
    player.fill((0, 255, 0))
    screen.blit(player, (player_x, 540))

    for obstacle in obstacles:
        obstacle.render(screen)

    for bullet in bullets:
        bullet.render(screen)
    for obstacle in obstacles:
        if playerrect.colliderect(obstacle.obrect):
            pygame.quit()
            sys.exit()

    for bullet in bullets:
        bulletrect = bullet.bulletrect
        for obstacle in obstacles:
            if bulletrect.colliderect(obstacle.obrect) and bullet in bullets:
                obstacles.remove(obstacle)
                bullets.remove(bullet)
        
    pygame.display.flip()
