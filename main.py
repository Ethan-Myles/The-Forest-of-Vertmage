import pygame
import random
import time

from bones import Bones
from character import Character
from gameover import Game_Over
from health import Health
from menu import Menu

# === Initalising Pygame ===
carryOn = True
clock = pygame.time.Clock()
pygame.init()

Width = 1280
Height = 720
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0,)

all_sprites_list = pygame.sprite.Group()


# === initalise font object to render text later ===


menuFont = pygame.font.Font('Exo-SemiBold.ttf', 35)

font = pygame.font.Font('Exo-SemiBold.ttf', 20)


# === setting the screen ===
size = (Width,Height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Forest")

# === Create archer object ===
surface1 = pygame.Surface([0,0],pygame.SRCALPHA)
archer_mask = pygame.mask.from_surface(surface1)
archer = Character(archer_mask)
archer.rect.x = 300
archer.rect.y = 412
characterGroup = pygame.sprite.Group(archer)
all_sprites_list.add(archer)

# === Create skeleton object ===


enemyGroup = pygame.sprite.Group()

for _ in range(1,3):
    surface2 = pygame.Surface([10,20],pygame.SRCALPHA)
    skeleton = Bones(surface2,False,False,random.randint(10,20))
    skeleton.rect.x = random.randint(500,1000)
    skeleton.rect.y = 407
    enemyGroup.add(skeleton)
    all_sprites_list.add(skeleton)


# === Create heart object ===
surface3 = pygame.Surface([1100,650],pygame.SRCALPHA)
heart = Health(surface3)
heart.rect.x = 1100
heart.rect.y = 650
itemsGroup = pygame.sprite.Group(heart)
all_sprites_list.add(heart)



itemsGroup.update()
characterGroup.update()

Menu(screen,menuFont,Width)

# creating 2d array
grid = [[n]*25 for n in range(15)]


# moon
grid[0][3] = -4


# === Randomisation for grey tiles ===
for c in range(0,25):
    for d in range(10,14):
        greyTiles = random.choice([-1,-2,-3])
        grid[d][c] = greyTiles
        greyTiles = random.choice([-1,-2,-3])
        grid[d][c] = greyTiles
        greyTiles = random.choice([-1,-2,-3])
        grid[d][c] = greyTiles
        greyTiles = random.choice([-1,-2,-3])
        grid[d][c] = greyTiles


gridColumn = 0
gridRow = 0
squareSize = 51.5
thickness = 100

strength = 3
slash = False


# === main loop ===
while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False


    all_sprites_list.update()


    # === skeleton movement ===
    for skeleton in enemyGroup:
        skeleton.run()
        if skeleton.rect.x <= -80:
                skeleton.rect.x = 1280


    # === archer respawn on left and right ===
    if archer.rect.x <= -80:
        archer.rect.x = 1280
    elif archer.rect.x >= 1280:
        archer.rect.x = -80
    else:
        archer.rect.x = archer.rect.x


    for row in grid:
        for col in row:
            if col == -1:
                colour = (144,144,144)
            elif col == -2:
                colour = (156,156,156)
            elif col == -3:
                colour = (168,168,168)
            elif col == -4:
                colour = (255,255,255)
            else:
                colour = (97, 147, 182)

            pygame.draw.rect(screen, (colour), (squareSize * gridColumn, squareSize * gridRow, squareSize, squareSize))
            pygame.draw.rect(screen, (colour), (squareSize * gridColumn, squareSize * gridRow, squareSize, thickness))
            pygame.draw.rect(screen, (colour), (squareSize * gridColumn, squareSize * gridRow, thickness, squareSize))
            gridColumn = gridColumn + 1
        gridRow = gridRow + 1
        gridColumn = 0
    gridRow = 0



    # === collision detection ===
    for skeleton in enemyGroup:
        if slash == True:
            col = (archer.rect.colliderect(skeleton.rect))
            if col == True:
                skeleton.die()
        if slash == False:
            col = (archer.rect.colliderect(skeleton.rect))
            if col == True:
                strengthChange = '0.2'
                minusString = '-'
                fstrengthChange = float(strengthChange)
                strength -= (fstrengthChange)
                # The decrease in health shown to the user
                hit = font.render(minusString + strengthChange, True, (Red))
                screen.blit(hit, (archer.rect.x, archer.rect.y))

    # === health change if hit by enemy ===
    if 1 <= strength <= 2:
        heart.two()
    elif 0 <= strength <= 1:
        heart.one()
    elif strength <= 0:
        print('Game Over')
        carryOn = False
        Game_Over(screen, menuFont, Width, clock)
    else:
        heart.three()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        archer.moveRight(20)
    elif keys[pygame.K_a]:
        archer.moveLeft(30)
    elif keys[pygame.K_q]:
        archer.shoot()
    elif keys[pygame.K_e]:
        archer.slash2()
        slash = True
    elif keys[pygame.K_s]:
        archer.crouch()
    elif keys[pygame.K_k]:
        skeleton.test()
    else:
        archer.stand()

    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(300)

pygame.quit()
