import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([900, 600])
exit = True
player_x = 20
player_y = 500
velocity = 0
vvelocity = 0
gravity = 0.025

class Platform:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,80,20)

    def render(self):
        self.rect = pygame.Rect(self.x,self.y,80,20)
        pygame.draw.rect(screen,(200,100,100),self.rect)

platforms = []
y = 50
x = 900

for i in range(5):
    platforms.append(Platform(x,y))
    y += 100
    x -= 150

while exit:

    clock.tick(100)
    screen.fill((255,255,255))

    player = pygame.Surface((35, 35))
    playerrect = pygame.Rect(player_x, player_y, 35, 35)
    player.fill((0, 255, 0))
    screen.blit(player, (player_x,player_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                velocity = -5  
            elif event.key == pygame.K_d:
                velocity = 5  
            elif event.key == pygame.K_SPACE:
                vvelocity = -1.75

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                velocity = 0 
            elif event.key == pygame.K_d:
                    velocity = 0

    for plat in platforms:
        plat.render()

    player_x += velocity
    player_y += vvelocity
    vvelocity += gravity 

    if player_x < 0:
        player_x = 0
        velocity = 0

    if player_x > 865:  
        player_x = 865
        velocity = 0

    if player_y >= 565:
        player_y = 565
        vvelocity = 0

    
    for plat in platforms:
        if playerrect.colliderect(plat.rect):
            if velocity < 0:
                player_x = plat.rect.right
            if velocity > 0:
                player_x = plat.rect.left - playerrect.width

            elif vvelocity > 0:  # Falling down; hit the top of the platform
                player_y = plat.rect.top - playerrect.height
                vvelocity = 0
                
            elif vvelocity < 0:  # Moving up; hit the bottom of the platform
                player_y = plat.rect.bottom
                vvelocity = 0
            

    pygame.display.flip()