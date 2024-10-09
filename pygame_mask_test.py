import pygame
import os
import math
import time

pygame.init()
clock = pygame.time.Clock()

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
    #"pickaxe":{
        #"amount":1,
        #"type":"copper",
    #},
}

blocktypes = {
    "grass":"dirt_grass_2X_size.png",
    "dirt":"dirt_block_X2_size.png",
    "stone":"stone_block_v1.png",
    #"pickaxe":"copper_pickaxe.png",
}

class View:
    def __init__(self):
        self.x = 0
        self.screen = pygame.display.set_mode((800, 600))

    def move(self, dx):
        self.x += dx

    def render(self, objects):
        for obj in objects:
            obj.render(self)

view = View()

class Inventory:
    def __init__(self):
        self.items = ["",""] # item that are in the inventory so that it can tell whether to add to stack item or to add to new hotbar point
    def block_move(self):
        position = pygame.mouse.get_pos()
        
    

                

class Hotbar:
    def __init__(self,x,y):
        self.type = ""
        self.x = x
        self.y = y
        self.amount = 0
        self.name = "inventory_space_smaller.png"
        self.hotbar_file = os.path.join(image_folder, self.name)
        self.hotbar_image = pygame.image.load(self.hotbar_file,self.name).convert_alpha()
        self.hotbar_rect = self.hotbar_image.get_rect()
        self.hotbar_mask = pygame.mask.from_surface(self.hotbar_image)

    def render(self,view):

        self.hotbar_rect.topleft = (self.x,self.y)
        view.screen.blit(self.hotbar_image, self.hotbar_rect)

        if self.amount != 0 and self.type != 0:
            name = blocktypes[self.type]
            self.shown_item_file = os.path.join(image_folder,name)
            self.shown_item_image = pygame.image.load(self.shown_item_file,name)
            self.shown_item_rect = self.shown_item_image.get_rect()
            self.shown_item_rect.topleft = ((self.hotbar_rect.topleft[0] + 11),(self.hotbar_rect.topleft[1] + 11))
            view.screen.blit(self.shown_item_image,self.shown_item_rect)
    

class Block:
    def __init__(self,x,y,type,name):
        self.x = x
        self.y = y
        self.type = type        
        self.name = name
        self.dirt_block_file = os.path.join(image_folder, self.name)
        self.block_image = pygame.image.load(self.dirt_block_file,self.name).convert_alpha()
        self.block_rect = self.block_image.get_rect()
        self.dirt_mask = pygame.mask.from_surface(self.block_image)

    def render(self, view):

        self.block_rect.topleft = (self.x - view.x ,self.y)
        view.screen.blit(self.block_image,self.block_rect)



        
class Player:
    def __init__(self):
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.jump = False
        self.grounded = False
        self.velocity = 0
        self.block_highlight_file = os.path.join(image_folder, "block-select-highlight.png")
        self.block_highlight_image = pygame.image.load(self.block_highlight_file,'block-select-highlight.png').convert_alpha()
        self.block_highlight_rect = self.block_highlight_image.get_rect()
        self.player_file = os.path.join(image_folder, "player_test_bigger.png")
        self.player_image = pygame.image.load(self.player_file,'player_test_bigger.png').convert_alpha()
        self.player_rect = self.player_image.get_rect()
        self.player_mask = pygame.mask.from_surface(self.player_image)
        self.player_rect.topleft = (100, 100)
        self.blockhighlightt = False 

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
        [positionX, positionY] = pygame.mouse.get_pos()

        x = math.trunc((positionX + view.x) / 20) * 20
        y = math.trunc(positionY/ 20) * 20
        li = (x,  y)
    
        self.blockhighlightt = False
        for block in blocks:
            if li[0] == block.x and li[1] == block.y:
                print(block.x, li[0], view.x, positionX, positionY)
                
                self.block_highlight_rect.topleft = ((li[0] - view.x), li[1])
                self.blockhighlightt = True
                


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                r = True
                z = True
                for block in blocks:
                    if li[0] == block.x and li[1] == block.y: #checks x,y against mouse coords
                        for item in inv.items: #inv.items is a list with the items in the inventory
                            if block.type == item: # if the blocktype is in the list containing the items in inv
                                z = False 
                                for hotbar in hotbars: #iterate through the hotbars until:
                                    if hotbar.type == block.type: #checks if hotbar type == block.type
                                        if r:
                                            r = False
                                            blocks.remove(block)
                                            hotbar.amount += 1
                                            inv.items.append(block.type)
                                            print(1)
                                            
                        if z:
                            s = True
                            for hotbar in hotbars:
                                if hotbar.type == "":
                                    if s:
                                        s = False
                                        hotbar.type = block.type
                                        inv.items.append(block.type)
                                        hotbar.amount += 1
                                        blocks.remove(block)
                                        print(2)  

            else:
                f = True
                s = True
                for block in blocks:
                    if block.x == li[0] and block.y == li[1]:
                        f = False

                if f:
                    for hotbar in hotbars:
                        amount = hotbar.amount
                        
                        if s:
                            if amount != 0 and hotbar.type != "":
                                s = False
                                hotbar.amount -= 1
                                name = blocktypes[hotbar.type]
                                blocks.append(Block(li[0],li[1],hotbar.type,name))
                                if hotbar.amount == 0:
                                    inv.items.remove(hotbar.type)
                                    hotbar.type = ""
                                    

                        
    def render(self,view):
        if self.blockhighlightt:
            view.screen.blit(self.block_highlight_image,self.block_highlight_rect)
        view.screen.blit(self.player_image,self.player_rect)


global blocks
blocks = []

def startup(blocks):
    name = "dirt_grass_2X_size.png"
    type = 'grass'
    x = 0
    y = 500
    for i in range(1600):
        blocks.append(Block(x,y,type,name))
        x += 20
        if x == 1600:
            name = "dirt_block_X2_size.png"
            type = "dirt"
            y += 20
            x = 0

        if y >= 540:
            name = "stone_block_v1.png"
            type = "stone"
    return blocks

y = 100
x = 200
hotbars = []

for i in range(3):
    hotbars.append(Hotbar(x,y))
    x += 55
    
inv = (Inventory())
player = (Player())
running = True
startup(blocks)
gravity = 0.09

while running:

    start = time.time()
    view.screen.fill((255, 255, 255))  
    clock.tick(120)
    r = False
    to_render = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.move()

    if player.jump:
        player.velocity = -2.5
        player.grounded = False
        player.jump = False

    if player.velocity < 0:
        player.move_down = False
        player.move_up = True
    else:
        player.move_down = True

    if not player.grounded:
        player.player_rect.y += player.velocity
        player.velocity += gravity

    if player.move_right:
        if not player.player_rect.x >= 450:
            player.player_rect.x += 1

        else:
            view.move(1)

    if player.move_left:
        if not player.player_rect.x <= 250:
            player.player_rect.x -= 1

        else:
            view.move(-1)

    for block in blocks:
        to_render.append(block)

    for block in blocks:
    
        offset = (block.block_rect.x - player.player_rect.x, block.block_rect.y - player.player_rect.y)
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
        
    if not r:
        player.grounded = False

    for hotbar in hotbars:
        to_render.append(hotbar)

    player.blockplace()
    to_render.append(player)
    view.render(to_render)

    
    pygame.display.flip() 

    end = time.time()

    #print('main loop time', end - start)


