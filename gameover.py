import pygame


def Game_Over(screen,menuFont,Width,clock):
    gam = True

    while gam:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()

    screen.fill((151, 188, 98))


    overText = menuFont.render('Game Over', True, (44, 95, 45))
    overTextW = overText.get_width()
    screen.blit(overText, ((Width - overTextW) / 2, 50))

    pygame.display.update()
    clock.tick(15)