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
colour = (100,100,100)
x = 100
y = 100

import pygame

delta = 1

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 'right'
        self.tail_length = 10
        self.tail = []

    def move(self):
        self.tail.append((self.x, self.y))
        self.tail = self.tail[-int(self.tail_length):]

        if self.direction == 'up':
            self.y -= delta
        elif self.direction == 'down':
            self.y += delta
        elif self.direction == 'left':
            self.x -= delta
        elif self.direction == 'right':
            self.x += delta


    def draw(self, surface):
        self.tail_length += 0.25
        for (x, y) in self.tail:
            t = pygame.Rect(x, y, 10, 10)
            pygame.draw.rect(surface, (255, 0, 0), t)
        
        r = pygame.Rect(self.x, self.y, 10, 10)
        pygame.draw.rect(surface, (0, 255, 0), r)

    def change_direction(self, direction):
        if direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        elif direction == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif direction == 'left' and self.direction != 'right':
            self.direction = 'left'
        elif direction == 'right' and self.direction != 'left':
            self.direction = 'right'

snake = Snake(100, 100)
while exit:
    clock.tick(200)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                snake.change_direction('up')

            elif event.key == pygame.K_LEFT:
                snake.change_direction('left')
                
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('right')

            elif event.key == pygame.K_DOWN:
                snake.change_direction('down')

    screen.fill((0,0,0))
    snake.move()
    snake.draw(screen)

    pygame.display.flip()
