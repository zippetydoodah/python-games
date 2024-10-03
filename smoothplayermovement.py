import pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 650))
screen.fill((0, 0, 0))
exit = True
gravity = 0.02
colour = (100, 100, 100)
walls = []
enemys = []
access = 0
shoot = False
bullets = []

MAP = {
    "ground1":{
        "exits":[("up","sky1"),("right","ground2"),("left","ground-1")],
    },

    "sky1":{
        "exits":[("down","ground1"),("right","sky2"),("left","sky-1")],
    },
}
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
ENEMYSTATS = {

    "zombie": {
        "healthbar":{
            "health":10,
            "max":10,
            "min":0,
            "location":[20,20,10,5],
            "damage": 2,
            "col": (230, 25, 0),
            "speed":0.25,
        },
    },

    "goblin": {
        "healthbar":{
            "health":15,    
            "max":15,
            "min":0,
            "location":[20,20,15, 5],
            "damage": 5,
            "col": (25, 230, 0),
            "speed":0.5,
        },
    },
}

def getAvailableMoves (player):
    global MAP

    movementOptions = MAP[player.location]["exits"]
    availableMoves = []
    moves = ""
    for element in movementOptions:
        availableMoves.append(element[0])
    for element in availableMoves:
        moves += (element)
        moves += ", "
    return moves

def collisions(player):

    for wall in walls:
        hitrect = wall.hitrect
        for bullet in bullets:
            if bullet.bulletrect.colliderect(hitrect):
                if not bullet.bulletrect.colliderect(player.hitrect):
                    bullets.remove(bullet)

        if player.hitrect.colliderect(hitrect):
            player.jump = True
            if not player.hitrect.colliderect(hitrect.move(4, 0)):
                player.x -= 1
        # Move the player away from the collision while considering the intended direction
            if player.move_left and not player.hitrect.colliderect(hitrect.move(-4, 0)):
                player.x += 1

            elif player.move_right and not player.hitrect.colliderect(hitrect.move(4, 0)):
                player.x -= 2

            elif player.move_up and not player.hitrect.colliderect(hitrect.move(0, -4)):
                    player.velocity = 0
                    player.y += 0.5
            elif player.move_down and not player.hitrect.colliderect(hitrect.move(0, 4)):
                player.velocity = 0
                player.y -= 0.5

            elif player.move_right and player.move_down and not player.hitrect.colliderect(hitrect.move(4, 4)):
                player.x -= 2

            elif player.move_right and player.move_up and not player.hitrect.colliderect(hitrect.move(4, -4)):
                player.x -= 2

            elif player.move_left and player.move_down and not player.hitrect.colliderect(hitrect.move(-4, 4)):
                player.x += 2

            elif player.move_left and player.move_up and not player.hitrect.colliderect(hitrect.move(-4, -4)):
                player.x += 2

class Healthbar:
    def __init__(self,place,person):
        self.health = place[person]["healthbar"]["health"]
        self.max = place[person]["healthbar"]["max"]
        self.min = place[person]["healthbar"]["min"]
        location = place[person]["healthbar"]["location"]
        self.y = location[1]
        self.x = location[0]
        self.distance = self.health
        self.length = location[2]
        self.width = location[3]

    def update(self, amount):
        self.health += amount
        if self.health > self.max:
            self.health = self.max
        if self.health < self.min:
            self.health = self.min
        self.distance = self.health
        print(self.health)

    def move(self,x,y):
        self.x = x
        self.y = y - 10
    def display(self):
        self.hitrect1 = pygame.Rect(self.x, self.y, self.length, self.width)
        self.hitrect = pygame.Rect(self.x, self.y, self.distance, self.width)
        pygame.draw.rect(screen, (255, 0, 0), self.hitrect1)
        pygame.draw.rect(screen, (0, 255, 0), self.hitrect)

class Bullet:
    def __init__(self,x,y,destination):
        self.destination = destination
        self.x = x
        self.y = y
        self.speed = 4
        self.bulletrect = pygame.Rect(self.x,self.y,10,10)

        self.dx = self.destination[0]- self.x
        self.dy = self.destination[1] - self.y
        self.hyp = math.sqrt((self.dx * self.dx) + (self.dy * self.dy))

    def render(self,screen):
        self.bulletrect = pygame.Rect(self.x,self.y,10,10)
        pygame.draw.rect(screen,(0,255,0),self.bulletrect)

    def move(self):
        self.x += (self.dx / self.hyp * self.speed)
        self.y += (self.dy / self.hyp * self.speed)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player = pygame.Surface((25, 25))
        self.hitrect = pygame.Rect(self.x, self.y, 25, 25)
        self.damage = PLAYERSTATS["player"]["healthbar"]["damage"]
        self.healthbar = (Healthbar(PLAYERSTATS,"player"))
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.velocity = 0
        self.location = ""
        self.jump = True

    def move(self):
        global shoot
        global pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot = True
            pos = event.pos
            #bullets.append(Bullet((player_x + 20),540,event.pos))
        elif event.type == pygame.MOUSEBUTTONUP:
            shoot = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.jump:
                # self.jump = False
                self.velocity = -1.5
                self.move_up = True
                self.move_down = False

            elif event.key == pygame.K_LEFT:
                self.move_left = True
                self.move_right = False

            elif event.key == pygame.K_RIGHT:
                self.move_right = True
                self.move_left = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = False

            elif event.key == pygame.K_RIGHT:
                self.move_right = False

        


    def render(self):
        screen.blit(self.player, (self.x, self.y))
        self.player.fill((200, 200, 200))
        self.hitrect = pygame.Rect(self.x, self.y, 25, 25)

class Enemy:
    def __init__(self, enemy, x, y):
        self.health = ENEMYSTATS[enemy]["healthbar"]["health"]
        self.damage = ENEMYSTATS[enemy]["healthbar"]["damage"]
        self.col = ENEMYSTATS[enemy]["healthbar"]["col"]
        self.x = x
        self.y = y
        self.speed = ENEMYSTATS[enemy]["healthbar"]["speed"]
        self.hitrect = pygame.Rect(self.x, self.y, 20, 20)
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.jump = True
        self.healthbar = (Healthbar(ENEMYSTATS,enemy))
        self.velocity = 0


    def move(self):

        if player.x > self.x:
            self.x += self.speed
            self.move_right = True
            self.move_left = False 
        else:
            self.x -= self.speed
            self.move_right = False
            self.move_left = True

        if self.velocity == 0 :
            if self.jump == True:
                if player.y < self.y:
                    self.velocity = -1.5
                    self.jump = False
                    
        if self.velocity > 0:
            self.move_up = False
        else:
            self.move_up = True

        if self.velocity < 0:
            self.move_down = False
        else:
            self.move_down = True

            
        self.hitrect = pygame.Rect(self.x, self.y, 20, 20)

    def render(self):
        pygame.draw.rect(screen, (self.col), self.hitrect)

class Wall:
    def __init__(self, y, w, t, h, r, direction):
        self.y = y
        self.w = w
        self.t = t
        self.h = h
        self.direction = direction
        self.x = random.randint(r, 800 - self.t)
        self.hitrect = pygame.Rect(self.x, self.y, self.w, self.h)

    def move(self):
        if self.x > 800:
            self.x = 0
        elif self.x < -75:
            self.x = 800
        self.x += self.direction
        self.hitrect = pygame.Rect(self.x, self.y, self.w, self.h)

    def render(self, screen):
        pygame.draw.rect(screen, (colour), self.hitrect)

for i in range(6):
    for i in range(3):
        y = access
        w = 75
        walls.append(Wall(y, w, 75, 20, 0, -1))
    access += 100

walls.append(Wall(630, 800, 800, 20, 0, 0))
walls.append(Wall(0, 10, 800, 650, 0, 0))
walls.append(Wall(0, 10, 10, 800, 790, 0))
# floor,left wall,right wall
player = (Player(100, 600))
enemys.append(Enemy("zombie", 50, 600))
enemys.append(Enemy("goblin", 50, 600))
enemys.append(Enemy("goblin", 50, 500))

while exit:
    clock.tick(120)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        player.move()
        

    if player.move_left:
            player.x -= 1
    if player.move_right:
        player.x += 1

    if player.velocity > 0:
        player.move_up = False
    else:
        player.move_up = True

    if player.velocity < 0:
        player.move_down = False
    else:
        player.move_down = True

    collisions(player)
    for enemy in enemys:
        collisions(enemy)

    for enemy in enemys:

        enemy.move()
        enemy.render()
        enemy.healthbar.move(enemy.x,enemy.y)
        enemy.healthbar.display()
        hitrect = enemy.hitrect

        if enemy.healthbar.health == 0:
            enemys.remove(enemy)

        if hitrect.colliderect(player.hitrect):
            if enemy.move_left == True:
                player.x -= 10 
            else:
                player.x += 10 
            player.healthbar.update(-enemy.damage)
        

        for bullet in bullets:
            if hitrect.colliderect(bullet.bulletrect):
                enemy.healthbar.update(-player.damage)
                bullets.remove(bullet)
                
    
    for bullet in bullets:
        bullet.move()
        bullet.render(screen)
        if bullet.x >= 920 or bullet.x <= 0 or bullet.y >= 610 or bullet.y <= 0:
            bullets.remove(bullet)
        
    if shoot:
        bullets.append(Bullet((player.x + 10),(player.y +10),pos))
    
    if len(bullets) >= 1:
        shoot = False
    
    for enemy in enemys:
        enemy.y += enemy.velocity
        enemy.velocity += gravity

    player.y += player.velocity
    player.velocity += gravity

    if player.healthbar.health != 0:
        player.healthbar.display()
        player.render()

    for wall in walls:
        wall.render(screen)
        wall.move()
    
    pygame.display.flip()
