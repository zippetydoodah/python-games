import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
move_up = False
move_right = False
move_left = False
move_down = False
exit = True
velocity = 0
gravity = 0.009
colour = (100,100,100)
px = 100
py = 100
walls = []
access = 0
COORDS = {
    0:[50,500,400,40],
    1:[100,600,400,20],
    2:[75,200,100,100],
    3:[],
    4:[],
    5:[],
}
class Wall:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hitrect = pygame.Rect(self.x,self.y,self.w,self.h)
    def move(self):
        if self.x > 800:
            self.x = 0
        self.x += 1 
        self.hitrect = pygame.Rect(self.x,self.y,self.w,self.h)

    def render(self,screen):
        pygame.draw.rect(screen,(colour),self.hitrect)

for i in range(3):
    x = COORDS[access][0]
    y = COORDS[access][1]
    w = COORDS[access][2]
    h = COORDS[access][3]
    walls.append(Wall(x,y,w,h))
    access += 1

while exit:
    clock.tick(200)
    player = pygame.Surface((40, 40))
    player.fill((200,200,200))
    screen.fill((0,0,0))

    
    screen.blit(player,(px,py))
    playerrect = pygame.Rect(px,py,40,40)

    #pygame.draw.rect(screen, (100,100,100), pygame.Rect(50, 50, 40, 40))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
            
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                velocity = -1.5
                move_up = True
                move_right = False
                move_left = False
                move_down = False

            elif event.key == pygame.K_LEFT:
                move_left = True
                move_up = False
                move_right = False
                move_down = False

            elif event.key == pygame.K_RIGHT:
                move_right = True
                move_up = False
                move_left = False
                move_down = False

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
        # Move the player away from the collision while considering the intended direction
            if move_left and not playerrect.colliderect(hitrect.move(-2, 0)):
                px += 1
            elif move_right and not playerrect.colliderect(hitrect.move(2, 0)):
                px -= 1
            elif move_up and not playerrect.colliderect(hitrect.move(0, -4)):
                velocity = 0
                
            elif move_down and not playerrect.colliderect(hitrect.move(0,4)):
                velocity = 0
            
    py += velocity
    velocity += gravity
    #for wall in walls:
        #wall.move()
    for wall in walls:
        wall.render(screen)
    pygame.display.flip()
