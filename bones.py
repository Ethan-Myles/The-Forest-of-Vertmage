import pygame
import time
import random

class Bones(pygame.sprite.Sprite):

    def __init__(self,surface2,still,crumble,pixels):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(683, 384, 10, 10)

        self.image = surface2

        self.crumble = crumble

        self.pixels = pixels

        # change speed
        self.pixels = 10

        self.still = still

        pygame.display.set_mode()

        self.standImages = []

        self.standImages.append(pygame.image.load('S_Images/stand0.png').convert_alpha())
        self.standImages.append(pygame.image.load('S_Images/stand1.png').convert_alpha())
        self.standImages.append(pygame.image.load('S_Images/stand2.png').convert_alpha())

        self.sCounter = 0

        self.runImages = []

        self.runImages.append(pygame.image.load('S_Images/run0.png').convert_alpha())
        self.runImages.append(pygame.image.load('S_Images/run1.png').convert_alpha())
        self.runImages.append(pygame.image.load('S_Images/run2.png').convert_alpha())
        self.runImages.append(pygame.image.load('S_Images/run3.png').convert_alpha())
        self.runImages.append(pygame.image.load('S_Images/run4.png').convert_alpha())
        self.runImages.append(pygame.image.load('S_Images/run5.png').convert_alpha())

        self.rCounter = 0

        self.deadImages = []

        self.deadImages.append(pygame.image.load('S_Images/dead0.png').convert_alpha())
        self.deadImages.append(pygame.image.load('S_Images/dead1.png').convert_alpha())
        self.deadImages.append(pygame.image.load('S_Images/dead2.png').convert_alpha())
        self.deadImages.append(pygame.image.load('S_Images/dead3.png').convert_alpha())
        self.deadImages.append(pygame.image.load('S_Images/dead4.png').convert_alpha())
        self.deadImages.append(pygame.image.load('S_Images/dead5.png').convert_alpha())

        self.dCounter = 0



    def stand(self):
        self.still = True


    def die(self):
        self.crumble = True

    def test(self):
       self.image = pygame.image.load('S_Images/a2_0.png')


    def run(self):

        if self.crumble == True:
            # selecting a specific image from the array
            self.image = self.deadImages[self.dCounter]

            time.sleep(0.05)
            self.dCounter += 1

            # restart the loop
            if self.dCounter == 6:
                self.dCounter = 5

        else:
            self.rect.x -= self.pixels
            # selecting a specific image from the array
            self.image = self.runImages[self.rCounter]

            time.sleep(0.05)
            self.rCounter += 1

            # restart the loop
            if self.rCounter >= len(self.runImages):
                self.rCounter = 0






