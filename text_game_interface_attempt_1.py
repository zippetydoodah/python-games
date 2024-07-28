import pygame
import sys
pygame.init()
clock = pygame.time.Clock()

MAP = {
    "forest1": {
        "name":"forest",
        "exits": [("east", "forest2")],
        "description": "There are apple trees!",
    },

    "forest2": {
        "name":"forest",
        "exits": [("west", "forest1"), ("north", "village")],
        "description": "you are in a big forest",
    },
    "village": {
        "name":"village",
        "exits": [("south", "forest2")],
        "description": "There are apple trees!",
    },
}

INVENTORY = {
    "rusty sword": 0,
    "sword": 1,
    "fists": 1,
    "spear": 10,
    "shield": 0,
    "axe": 0,
    "apple": 0,
    "banana": 0,
    "berry": 3,
    "skin": 0,
    "bones": 0,
    "wood": 80,
    "stone": 80,
    "pinecone": 0,
}

ITEM_TYPE = {
    "rusty sword": "weapon",
    "sword": "weapon",
    "fists": "weapon",
    "spear": "weapon",
    "shield": "weapon",
    "axe": "weapon",

    "apple": "food",
    "banana": "food",
    "berry": "food",

    "skin": "misc",
    "bones": "misc",
    "wood": "misc",
    "stone": "misc",
    "pinecone": "misc",

}

global LIST
global PLAYERLOCATION
PLAYERLOCATION = "forest1"
LIST = []

def getAvailableMoves(playerLocation):

    global MAP
    movementOptions = MAP[playerLocation]["exits"]
    availableMoves = []
    moves = ""

    for element in movementOptions:
        availableMoves.append(element[0])
        LIST.append(element[0])

    for element in availableMoves:
        moves += (element)
        moves += ", "

    return moves

def moveplayer(direction, playerlocation):
    global MAP
    
    movementoptions = MAP[playerlocation]["exits"]

    for element in movementoptions:
        command = element[0]
        destination = element[1]

        if (command == direction):
            return destination
    return PLAYERLOCATION

class TextDisplay:

    def __init__(self, xpos, ypos, text):
        self.font = pygame.font.SysFont("Times New Roman", 23)
        self.text = self.font.render(text, True, (0, 0, 255), (255, 255, 255))
        self.xpos = xpos
        self.ypos = ypos

    def render(self, screen):
        textRect = self.text.get_rect()
        textRect.center = (self.xpos // 2, self.ypos // 2)
        screen.blit(self.text, textRect)

    def setText(self, text):
        self.text = self.font.render(text, True, (0, 0, 255), (255, 255, 255))

    def setcoords(self,xpos,ypos,screen):
        textRect = self.text.get_rect()
        textRect.center = (xpos // 2, ypos // 2)
        screen.blit(self.text,textRect)


class Buttondisplay:
    def __init__(self, xpos, ypos,colour):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.equiprect = pygame.Rect(self.xpos,self.ypos,40,40)
    def render(self, screen):
        pygame.draw.rect(screen,self.colour,self.equiprect)
        
    
    def clicked(self,pos,s):
        if self.equiprect.collidepoint(pos):
            self.colour = s


screen = pygame.display.set_mode([900, 600])
base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False
 
playerLocationDisplay = TextDisplay(400, 200, '')
movesDisplay = TextDisplay(400, 350, '')
equipdisplay = TextDisplay(400, 350, 'Equip')

def equiploop(e):
    x = 100       
    buttons = [] 
    items = getitems("weapon")
    number_of_times = len(items)
    update_equipdisplay(items,900,100)
    for i in range(number_of_times):
        buttons.append(Buttondisplay(x,400,(100,100,100)))
        x += 80

    while e:
        
        screen.fill((255, 255, 255))
        
        
        for display in equipitemdisplay:
            display.render(screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    e = False   
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                col = (200,200,200)
                for button in buttons:
                    button.clicked(event.pos,col)
            elif event.type == pygame.MOUSEBUTTONUP:
                col = (100,100,100)
                for button in buttons:
                    button.clicked(event.pos,col)
                        
        equipdisplay.render(screen) 
        for button in buttons:
            button.render(screen)
        pygame.display.flip()

def getitems(items):
    names = []
    newnames = []
    for name, itemtype in ITEM_TYPE.items():
        if itemtype == items:
            
            names.append(name)
    for element in names:
        num = INVENTORY[element]
        if num != 0:
            newnames.append(element)
    return newnames

def update_equipdisplay(place, xpos, ypos):
    global equipitemdisplay
    equipitemdisplay = []
    for element  in place:
        equipitemdisplay.append(TextDisplay(xpos, ypos, element,))
        ypos += 50


def updateinventory(place, xpos, ypos):
    global inventorydisplay
    inventorydisplay = []
    for element, amount  in place.items():
        inventorydisplay.append(TextDisplay(xpos, ypos, f"{element}: {amount}",))
        ypos += 50


while True:
    screen.fill((255, 255, 255))

    updateinventory(INVENTORY,700,100)
    output = "Place: "
    moves = "Options: "

    output += MAP[PLAYERLOCATION]["name"]
    playerLocationDisplay.setText(output)
    
    moves += getAvailableMoves(PLAYERLOCATION)
    movesDisplay.setText(moves)

    for display in inventorydisplay:
        display.render(screen)

    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            else:
                user_text += event.unicode

            if event.key == pygame.K_RETURN:
                length = len(user_text)
                if user_text.lower()[0] == "e"and length == 2:
                    user_text = ""
                    e = True
                    equiploop(e)
                        
                       


                for element in LIST:
                    if element in user_text.lower():
                        PLAYERLOCATION = moveplayer(element,PLAYERLOCATION)
                        user_text = ""


                

    if active:
        color = color_active

    else:
        color = color_passive

    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)

    playerLocationDisplay.render(screen)
    movesDisplay.render(screen)


    pygame.display.flip()
    clock.tick(60)
