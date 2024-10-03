import pygame
import os
import math
import time

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

image_folder = "C:\\Users\\zacha_er3uo9\\coding\\pygame-example\\src\\python_pixilart"
ground_file = os.path.join(image_folder, "ground.png")
background_file = os.path.join(image_folder, "background.png")

inventory = {
    "dirt":{
        "amount":0,
    },
    "grass":{
        "amount":0,
    },
}

blocktypes = {
    "grass":"dirt_grass_2X_size.png",
    "dirt":"dirt_block_X2_size.png",
}

class Hotbar:
    def __init__(self,x,y,type):
        self.type = type
        self.x = x
        self.y = y
        self.name = "inventory_frame_size50x50.png"
        self.hotbar_file = os.path.join(image_folder, self.name)
        self.hotbar_image = pygame.image.load(self.hotbar_file,self.name).convert_alpha()
        self.hotbar_rect = self.hotbar_image.get_rect()
        self.hotbar_mask = pygame.mask.from_surface(self.hotbar_image)

    def render(self,screen):
        self.hotbar_rect.topleft = (self.x,self.y)
        screen.blit(self.hotbar_image, self.hotbar_rect)
        if inventory[self.type]["amount"] != 0:
            name = blocktypes[self.type]
            self.shown_item_file = os.path.join(image_folder,name)
            self.shown_item_image = pygame.image.load(self.shown_item_file,name)
            self.shown_item_rect = self.shown_item_image.get_rect()
            self.shown_item_rect.topleft = (self.hotbar_rect.centerx,self.hotbar_rect.centery)
            screen.blit(self.shown_item_image,self.shown_item_rect)
    

class Block:
    def __init__(self,x,y,type,name):
        self.x = x
        self.y = y
        self.type = type        
        self.name = name
        self.dirt_block_file = os.path.join(image_folder, self.name)
        self.dirt_image = pygame.image.load(self.dirt_block_file,self.name).convert_alpha()
        self.dirt_rect = self.dirt_image.get_rect()
        self.dirt_mask = pygame.mask.from_surface(self.dirt_image)

    def render(self,screen):
        self.dirt_rect.topleft = (self.x,self.y)
        screen.blit(self.dirt_image,self.dirt_rect)


class Player:
    def __init__(self):
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.jump = False
        self.grounded = False
        self.velocity = 0
        self.player_file = os.path.join(image_folder, "player_test_bigger.png")
        self.player_image = pygame.image.load(self.player_file,'player_test_bigger.png').convert_alpha()
        self.player_rect = self.player_image.get_rect()
        self.player_mask = pygame.mask.from_surface(self.player_image)
        self.player_rect.topleft = (100, 100)

    def move(self):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.jump = True
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


    def blockplace(self):
        global blocks
        position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            li = []
            for c in position:
                
                c = c / 20
                k = math.trunc(c)
                k *= 20
                li.append(k)

            if event.button == 1:
                for block in blocks:
                    if li[0] == block.x and li[1] == block.y:
                        blocks.remove(block)
                        inventory[block.type]["amount"] += 1
            

            else: 
                f = True
                for block in blocks:
                    if block.x != li[0] and block.y != li[1]:
                        for hotbar in hotbars:
                            amount = inventory[hotbar.type]["amount"]
                            if f:
                                if amount != 0:
                                    f = False
                                    inventory[hotbar.type]["amount"] -= 1
                                    name = blocktypes[hotbar.type]
                                    blocks.append(Block(li[0],li[1],hotbar.type,name))
                        
          
    def render(self,screen):
        screen.blit(self.player_image,self.player_rect)

global blocks
blocks = []
def startup(blocks):
    name = "dirt_grass_2X_size.png"
    type = 'grass'
    x = -800
    y = 500
    for i in range(1600):
        blocks.append(Block(x,y,type,name))
        x += 20
        if x == 1600:
            name = "dirt_block_X2_size.png"
            type = 'dirt'
            y +=20
            x = -800
    return blocks

y = 500
x = 200
hotbars = []
type = "dirt"
for i in range(2):
    hotbars.append(Hotbar(x,y,type))
    x += 100
    type = "grass"

player = (Player())
running = True
startup(blocks)
gravity = 0.09
left_scroll = False
right_scroll = False
r = False
amount = 0
while running:
    start = time.time()
    screen.fill((255, 255, 255))  
    clock.tick(120)
    r = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.move()
        player.blockplace()

    if player.jump:
        player.velocity = -2.5
        player.grounded = False
        player.jump = False
    

    

    if player.velocity < 0:
        player.move_down = False
        player.move_up = True
    else:
        player.move_down = True
        

    for block in blocks:
    
        offset = (block.dirt_rect.x - player.player_rect.x, block.dirt_rect.y - player.player_rect.y)
        if player.player_mask.overlap(block.dirt_mask, offset):

            if player.move_down:
                player.player_rect.y -= 1
                player.velocity = 0
                player.move_down = False
                player.grounded = True
                r = True 

            if player.move_up:
                player.player_rect.y += 1
                player.velocity = 0
                player.move_up = False

            if player.move_left:
                player.player_rect.x += 2

            if player.move_right:
                player.player_rect.x -= 2

        else:

            gravity = 0.09
        block.render(screen)

    if not player.grounded:
        player.player_rect.y += player.velocity
        player.velocity += gravity

    if not r:
        player.grounded = False

    if player.move_left:
        if player.player_rect.x >= 250:
            player.player_rect.x -= 1
        else:
            left_scroll = True
            for block in blocks:
                block.x += 1

    if not player.move_left and left_scroll:
        left_scroll = False
        #print(1)
        for block in blocks:
            #print("blockx",block.x)
            x = block.x/20
            x = math.trunc(x)
            x *= 20
            amount = block.x - x
            

            if amount != 0:
                if amount > 0:
                    block.x -= amount
                    print("pos",block.x)
                else:
                    block.x -= amount
                    print(1)
                    print(block.x)

                    
    if player.move_right:
        if player.player_rect.x <= 450:
            player.player_rect.x += 1
        else:
            right_scroll = True
            for block in blocks:
                block.x -= 1

    if not player.move_right and right_scroll:
        right_scroll = False
        for block in blocks:
            x = block.x/20
            x = math.trunc(x)
            x *= 20
            amount = block.x - x
            if amount != 0:
                if amount > 0:
                    block.x -= amount
                else:
                    block.x -= amount

    for hotbar in hotbars:
        hotbar.render(screen)

    player.render(screen)
    pygame.display.flip() 

    end = time.time()

    #print('main loop time', end - start)


