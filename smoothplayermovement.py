import pygame
import random 
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,650))
screen.fill((0,0,0))
move_up = False
move_right = False
move_left = False
move_down = False
exit = True
velocity = 0
gravity = 0.02
colour = (100,100,100)
px = 100
py = 600
walls = []
access = 0
jump = 1

class Wall:
    def __init__(self,y,w,t,h,r,direction):
        self.y = y
        self.w = w
        self.t = t
        self.h = h
        self.direction = direction
        self.x = random.randint(r,800 - self.t)
        self.hitrect = pygame.Rect(self.x,self.y,self.w,self.h)

    def move(self):
        if self.x > 800:
            self.x = 0
        elif self.x < -75:
            self.x = 800
        self.x += self.direction
        self.hitrect = pygame.Rect(self.x,self.y,self.w,self.h)

    def render(self,screen):
        pygame.draw.rect(screen,(colour),self.hitrect)

for i in range(6):
    for i in range(3):
        y = access
        w = 75
        walls.append(Wall(y,w,75,20,0,-1))
    access += 100

walls.append(Wall(630,800,800,20,0,0))
walls.append(Wall(0,10,800,650,0,0))
walls.append(Wall(0,10,10,800,790,0))
#floor,left wall,right wall

while exit:
    clock.tick(120)
    player = pygame.Surface((25, 25))
    player.fill((200,200,200))
    screen.fill((0,0,0))
    screen.blit(player,(px,py))
    playerrect = pygame.Rect(px,py,25,25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and jump:
                jump = False
                velocity = -1.5
                move_up = True
                move_down = False

            elif event.key == pygame.K_LEFT:
                move_left = True
                move_right = False

            elif event.key == pygame.K_RIGHT:
                move_right = True
                move_left = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
                
            elif event.key == pygame.K_RIGHT:
                move_right = False
                
    if move_left:
        px -= 1
    if move_right:
        px += 1

    if velocity > 0:
        move_up = False
    else:
        move_up = True

    if velocity < 0:
        move_down = False
    else: 
        move_down = True

    for wall in walls:
        hitrect = wall.hitrect

        if playerrect.colliderect(hitrect):
            
            jump = True
            if not playerrect.colliderect(hitrect.move(4, 0)):
                px -= 1
        # Move the player away from the collision while considering the intended direction
            if move_left and not playerrect.colliderect(hitrect.move(-4, 0)):
                px += 1

            elif move_right and not playerrect.colliderect(hitrect.move(4, 0)):
                px -= 2

            elif move_up and not playerrect.colliderect(hitrect.move(0, -4)):
                velocity = 0

            elif move_down and not playerrect.colliderect(hitrect.move(0, 4)):
                velocity = 0

            
            elif move_right and move_down and not playerrect.colliderect(hitrect.move(4, 4)):
                px -= 2
                
            elif move_right and move_up and not playerrect.colliderect(hitrect.move(4, -4)):
                px -= 2
                
            elif move_left and move_down and not playerrect.colliderect(hitrect.move(-4, 4)):
                px += 2
                
            elif move_left and move_up and not playerrect.colliderect(hitrect.move(-4, -4)):
                px += 2
                    
            
    py += velocity
    velocity += gravity

    for wall in walls:
        wall.render(screen)
        wall.move()
    pygame.display.flip()
