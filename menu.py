import pygame
from controls import Controls

def Menu(screen,menuFont,Width):
    men = True

    selection = ''

    while men:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    selection = 'B'
                if event.key == pygame.K_s and selection == 'B':
                    selection = 'C'
                elif event.key == pygame.K_s:
                    selection = 'E'
                if event.key==pygame.K_RETURN:
                    if selection =='C':
                        Controls(screen)
                    if selection=='B':
                        men = False
                    if selection=='E':
                        pygame.quit()
                        quit()

        screen.fill((151,188,98))

        title = menuFont.render('Voyage: The Forest of Vertmage', True, (44,95,45))
        titleW = title.get_width()
        screen.blit(title, ((Width - titleW) / 2, 50))

        if selection == 'B':
            colour = (35, 85, 135)
        else:
            colour = (44,95,45)

        begin = menuFont.render('Begin Game', True, (colour))
        beginW = begin.get_width()
        screen.blit(begin, ((Width - beginW) / 2, 200))


        if selection == 'C':
            colour = (35, 85, 135)
        else:
            colour = (44,95,45)

        begin = menuFont.render('Controls', True, (colour))
        beginW = begin.get_width()
        screen.blit(begin, ((Width - beginW) / 2, 300))

        if selection == 'E':
            colour = (35, 85, 135)
        else:
            colour = (44,95,45)

        test = menuFont.render('Exit', True, (colour))
        testW = test.get_width()
        screen.blit(test, ((Width - testW) / 2, 400))



        pygame.display.flip()

