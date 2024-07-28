import pygame

pygame.init()
exit = False
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

xcoords = 100
y2coords = 40
x2coords = 500
ycoords = 5
pcoordx = 10
pcoordy = 10

# Flags to track movement
move_left = False
move_right = False
move_up = False
move_down = False

def wall(xcoords,x2coords):
    wall = pygame.Surface((40,50))
    wall.fill((200, 100, 100))
    wall2 = pygame.Surface((80,100))
    wall.fill((200,100,100))
    if xcoords == 0:
        xcoords = 800
    else:
        xcoords -= 1
    if x2coords == 0:
        x2coords = 800
    else:
        x2coords -= 1

    return wall, xcoords, wall2,x2coords

while not exit:
    clock.tick(100)  # Limit frame rate to 60 FPS
    if pcoordx == xcoords and pcoordy == ycoords:
        exit = True
    else:
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                # Set movement flags when keys are pressed
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_UP:
                    move_up = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
            elif event.type == pygame.KEYUP:
                # Unset movement flags when keys are released
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_DOWN:
                    move_down = False

        # Update player's position based on movement flags
        if move_left:
            pcoordx -= 5
        if move_right:
            pcoordx += 5
        if move_up:
            pcoordy -= 5
        if move_down:
            pcoordy += 5

        # Update game state
        newsurface, xcoords, newsurface2,x2coords = wall(xcoords,x2coords)

        # Draw everything
        screen.fill((0, 0, 0))
        screen.blit(newsurface, (xcoords, ycoords))
        screen.blit(newsurface2,(x2coords,y2coords))
        pygame.draw.rect(screen, (0, 0, 100), pygame.Rect(pcoordx, pcoordy, 20, 20))
        # Update the display
        pygame.display.flip()
        player_rect = pygame.Rect(pcoordx, pcoordy, 20, 20)
        wall_rect = pygame.Rect(xcoords, ycoords, 20, 200)
        # Handle collision (e.g., stop the player from moving)
        pcoordx = max(0, min(pcoordx, 800 - 20))
        pcoordy = max(0, min(pcoordy, 600 - 20))
        if player_rect.colliderect(wall_rect):
            exit = True


pygame.quit()