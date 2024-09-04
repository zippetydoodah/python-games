import pygame
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 650))
screen.fill((0, 0, 0))
move_up = False
move_right = False
move_left = False
move_down = False
exit = True
velocity = 0
gravity = 0.02
colour = (100, 100, 100)
px = 100
py = 600
walls = []
access = 0
jump = 1
ENEMYSTATS = {
    "zombie": {
        "damage": 2,
        "enemyhealth": 10,
        "col": (230, 25, 0),
    },

    "goblin": {
        "damage": 5,
        "enemyhealth": 15,
        "col": (25, 230, 0),
    },
}


class Health:
    def __init__(self):
        self.health = 100
        self.max = 100
        self.min = 0
        self.x = 20
        self.y = 20
        self.distance = self.health

    def update(self, amount):
        self.health += amount
        if self.health > self.max:
            self.health = self.max
        if self.health < self.min:
            self.health = self.min
        self.distance = self.health
        print(self.distance)

    def display(self):
        self.hitrect1 = pygame.Rect(self.x, self.y, 100, 20)
        self.hitrect = pygame.Rect(self.x, self.y, self.distance, 20)
        pygame.draw.rect(screen, (255, 0, 0), self.hitrect1)
        pygame.draw.rect(screen, (0, 255, 0), self.hitrect)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player = pygame.Surface((25, 25))
        self.playerrect = pygame.Rect(self.x, self.y, 25, 25)

    def render(self):
        screen.blit(self.player, (self.x, self.y))
        self.player.fill((200, 200, 200))
        self.playerrect = pygame.Rect(self.x, self.y, 25, 25)


class Enemy:
    def __init__(self, enemy, x, y):
        self.health = ENEMYSTATS[enemy]["enemyhealth"]
        self.damage = ENEMYSTATS[enemy]["damage"]
        self.col = ENEMYSTATS[enemy]["col"]
        self.x = x
        self.y = y
        self.speed = 0.5
        self.enemyhitrect = pygame.Rect(self.x, self.y, 20, 20)

    def move(self):
        if player.x > self.x:
            self.x += self.speed
        else:
            self.x -= self.speed

        # if player.y > self.y:
        #     self.y += self.speed
        # else:
        #     self.y -= self.speed

        self.enemyhitrect = pygame.Rect(self.x, self.y, 20, 20)

    def render(self):
        pygame.draw.rect(screen, (self.col), self.enemyhitrect)


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
player = (Player(px, py))
health = (Health())
enemy = (Enemy("zombie", 50, 600))
while exit:
    clock.tick(120)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and jump:
                # jump = False
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
        player.x -= 1
    if move_right:
        player.x += 1

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

        if player.playerrect.colliderect(hitrect):

            jump = True
            if not player.playerrect.colliderect(hitrect.move(4, 0)):
                player.x -= 1
        # Move the player away from the collision while considering the intended direction
            if move_left and not player.playerrect.colliderect(hitrect.move(-4, 0)):
                player.x += 1

            elif move_right and not player.playerrect.colliderect(hitrect.move(4, 0)):
                player.x -= 30

            elif move_up and not player.playerrect.colliderect(hitrect.move(0, -4)):
                velocity = 0

            elif move_down and not player.playerrect.colliderect(hitrect.move(0, 4)):
                velocity = 0

            elif move_right and move_down and not player.playerrect.colliderect(hitrect.move(4, 4)):
                player.x -= 2

            elif move_right and move_up and not player.playerrect.colliderect(hitrect.move(4, -4)):
                player.x -= 2

            elif move_left and move_down and not player.playerrect.colliderect(hitrect.move(-4, 4)):
                player.x += 2

            elif move_left and move_up and not player.playerrect.colliderect(hitrect.move(-4, -4)):
                player.x += 2

    enemy.move()
    enemy.render()
    if player.playerrect.colliderect(enemy.enemyhitrect):
        health.update(-10)
        player.x += 20
    player.y += velocity
    velocity += gravity

    health.display()
    player.render()

    for wall in walls:
        wall.render(screen)
        wall.move()
    pygame.display.flip()
