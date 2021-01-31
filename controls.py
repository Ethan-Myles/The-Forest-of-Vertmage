import pygame

def Controls(screen):
    con = True


    while con:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        print('Im in')