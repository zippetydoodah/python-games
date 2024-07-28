import pygame
import sys
import random
pygame.init()
clock = pygame.time.Clock()



screen = pygame.display.set_mode([900, 600])
exit = True
vertical_velocity = 0
gravity = 0.045
player_y = 100
jump = True

class Obstruction:
    def __init__(self,x,y):

        self.x = x
        self.y = y
        self.rects()

    def rects(self):
        self.squarerect = pygame.Rect(self.x,self.y,40,40)
    def draw(self):
        pygame.draw.rect(screen,(200,100,100),self.squarerect)

    def move(self):
        self.x -= 2
        self.rects()

obstructions = []
xobstruct = 800

for i in range(100):
    num = random.randint(350,800)
    xobstruct += num
    obstructions.append(Obstruction(xobstruct,540))

score = 0

while exit:
    clock.tick(200)
    screen.fill((255, 255, 255))

    for obstruct in obstructions:
       
        obstruct.move()
        obstruct.draw()
        
        if obstruct.x <= -20:
            obstructions.remove(obstruct)
            print(12)
            score +=1
     

    font = pygame.font.SysFont('Arial', 45)
    text = font.render("%s"%(score), True, (0,0,255), (0,0,0))
    textRect = text.get_rect()
    textRect.center = (400 // 2, 400 // 2)
    screen.blit(text, textRect)

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jump == False:
                    vertical_velocity = -2.8
                    jump = True
  
    player_y += vertical_velocity
    vertical_velocity += gravity

    player = pygame.Surface((40,40))
    playerrect = pygame.Rect(560 ,player_y,40,40)
    player.fill((0,255,0))
    screen.blit(player,(560,player_y))

    if player_y < 0:
        jump = False
        player_y = 0
        vertical_velocity = 0

    elif player_y > 560:
        jump = False
        player_y = 560
        vertical_velocity = 0

    for obstruct in obstructions:
        if playerrect.colliderect(obstruct.squarerect):
            exit = False
            
    pygame.display.flip()