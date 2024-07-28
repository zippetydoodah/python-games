import pygame
import random
import sys
pygame.init()
clock = pygame.time.Clock()
exit = True
screen = pygame.display.set_mode((800, 600))
player_y = 200
velocity = 0
gravity = 0.0095
play = False
inverse = False

class Buttondisplay:
    def __init__(self, xpos, ypos,colour,name):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.equiprect = pygame.Rect(self.xpos,self.ypos,40,40)
    def render(self, screen):
        pygame.draw.rect(screen,self.colour,self.equiprect)
        
    
    def clicked(self,pos,s):
        if self.equiprect.collidepoint(pos):
            self.colour = s
            return True
class Wall:
    def __init__(self,x,y):
        
        self.x = x
        self.y = y 
        self.hole_y = 0
        self.hole_height = 0
        if self.x <= -30:
            self.x = 800

        self.hole()
        self.rects()

    def hole(self):
        self.hole_y = random.randint(0,500)
        self.hole_height = random.randint(100,600)
        
    def rects(self):
        self.wallrect = pygame.Rect(self.x,self.y,40,self.hole_y)
        self.lowwallrect =  pygame.Rect(self.x, self.hole_y + self.hole_height, 40 , 600 - (self.hole_y + self.hole_height))
        self.holerect = pygame.Rect(self.x, self.hole_y,40,self.hole_height)
        
    def move(self):
        self.x -= 1
        self.rects()

    def draw(self):
        pygame.draw.rect(screen,(200,100,100),self.wallrect)
        pygame.draw.rect(screen,(200,100,100),self.lowwallrect)
        pygame.draw.rect(screen,(0,0,0),self.holerect)


wall1 = Wall(-10,0)
wall2 = Wall(400,0)
score = 0

fade = pygame.Surface((800, 600))
fade.fill((0, 0, 0))
while exit:

    p = False
    walls = []

    walls.append(wall1)
    walls.append(wall2)
    
    if not play:
        clock.tick(100)
    else:
        clock.tick(300)
    screen.fill((0,0,0))

    if play:
        for wall in walls:
            if wall.x == 450:
                score += 1
                
    score_background = pygame.Rect(0, 0,70,50)
    pygame.draw.rect(screen,(100,100,100),score_background)
    font = pygame.font.SysFont('Arial', 30)
    text = font.render("%s"%(score), True, (0,0,255), (100,100,100))
    textRect = text.get_rect()
    textRect.center = (40 // 2, 60 // 2)
    screen.blit(text, textRect)


    if wall1.x <= -30:
        wall1 = Wall(-30,0)
    if wall2.x <= -30:
        wall2 = Wall(-30,0)

    wall2.move()
    wall1.move()
    wall1.draw()
    wall2.draw()
    
    

    player = pygame.Surface((40,40))
    playerrect = pygame.Rect(300,player_y,40,40)
    player.fill((0,255,0))
    screen.blit(player,(300,player_y))

    if play:
        for wall in walls:
            if playerrect.colliderect(wall.wallrect) or playerrect.colliderect(wall.lowwallrect):
                if not playerrect.colliderect(wall.holerect):

                    player_y = 200
                    p = True
                    s = 0
                    x = 100
                    buttons = []
                    name = 1
                    for i in range(2):
                        buttons.append(Buttondisplay(x,400,(100,100,100),name))
                        name += 1
                        x += 80 

                    while p:
                        clock.tick(30)
                        play = False
                       

                        
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    p = False
                                    score = 0
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                col = (200,200,200)
                                for button in buttons:
                                    if button.clicked(event.pos,col):
                                        if button.name == 1:
                                            inverse = True
                                            print(1)
                                        elif button.name == 2:
                                            inverse = False
                                            print(2)
                            elif event.type == pygame.MOUSEBUTTONUP:
                                col = (100,100,100)
                                for button in buttons:
                                    button.clicked(event.pos,col)

                        s +=1
                        fade.set_alpha(s)
                        screen.blit(fade, (0, 0))
                        text = font.render("%s %s"%("Score: ", score), True, (0,0,255), (0,0,0))
                        textRect = text.get_rect()
                        textRect.center = (400 // 2, 400 // 2)
                        screen.blit(text, textRect)
                        for button in buttons:
                            button.render(screen)
                        pygame.display.flip()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    if play:
                        if inverse:
                            velocity = 1.5
                            gravity = -0.0095
                            
                        elif inverse == False:
                            velocity = -1.5
                            gravity = 0.0095
                            
                    play = True

    if play: 
        player_y += velocity
        velocity += gravity

        if player_y < 0:
            player_y = 0
            velocity = 0

        elif player_y > 560:
            player_y = 560
            velocity = 0
    pygame.display.flip()
