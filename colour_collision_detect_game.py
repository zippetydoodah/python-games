
import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 650))
screen.fill((0, 0, 0))
exit = True
collision_col = ((200,200,200))
collision = False
PLAYERSTATS = {
    "player":{
        "healthbar":{
            "health":100,
            "max":100,
            "min":0,
            "location":[20,20,100,20],
            "damage":1,
        },
    },
}
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player = pygame.Surface((25, 25))
        self.hitrect = pygame.Rect(self.x, self.y, 25, 25)
        self.damage = PLAYERSTATS["player"]["healthbar"]["damage"]
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.move_down = False

    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_up = True
                self.move_down = False

            elif event.key == pygame.K_LEFT:
                self.move_left = True
                self.move_right = False

            elif event.key == pygame.K_RIGHT:
                self.move_right = True
                self.move_left = False
            elif event.key == pygame.K_DOWN:
                self.move_down = True
                self.move_up = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = False

            elif event.key == pygame.K_RIGHT:
                self.move_right = False

            elif event.key == pygame.K_DOWN:
                self.move_down = False

            if event.key == pygame.K_UP:
                self.move_up = False

    def render(self):
        screen.blit(self.player, (self.x, self.y))
        self.player.fill((200, 200, 200))
        self.hitrect = pygame.Rect(self.x, self.y, 25, 25)

player = Player(200,200)

while exit:
    clock.tick(120)
    screen.fill((0, 0, 0))

    #places = [(player.hitrect.left,player.hitrect.top),(player.hitrect.left,player.hitrect.bottom),(player.hitrect.right,player.hitrect.bottom),(player.hitrect.right,player.hitrect.top)]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

        player.move()
        
    if player.move_left:
        player.x -= 1
    if player.move_right:
        player.x += 1
    if player.move_up:
        player.y -= 1
    if player.move_down:
        player.y += 1
    
    obrect = pygame.Rect(400,400,35,100)
    pygame.draw.rect(screen,(255,255,0),obrect)
    player.render()
    collision = False
    tolerance = 1 
    for x in range(obrect.x, obrect.x + obrect.width, tolerance):
        for y in range(obrect.y, obrect.y + obrect.height, tolerance):
            
            colour = screen.get_at((x,y))
            if colour == collision_col:
                print(2)
                collision = True
                print(1)
                
    if collision:
        if player.move_down:
            player.y -= 1
        if player.move_up:
            player.y += 1
        if player.move_left:
            player.x += 1
        if player.move_right:
            player.x -= 1
        if player.move_down and player.move_left:
            player.y -= 1
            player.x += 1
        if player.move_up and player.move_left:
            player.y += 1
            player.x += 1
        if player.move_up and player.move_right:
            player.x -= 1
            player.y += 1
        if player.move_down and player.move_right:
            player.x -= 1
            player.y -= 1
        


    


    
    pygame.display.flip()
    