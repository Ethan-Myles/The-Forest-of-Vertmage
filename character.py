import pygame
import time

class Character(pygame.sprite.Sprite):

    def __init__(self,surface1):
        super().__init__()

        self.rect = pygame.Rect(683, 384, 60, 10)

        self.image = surface1

        pygame.display.set_mode()

        # all the images contained within the array
        self.images = []

        self.images.append(pygame.image.load('Images/run0.png').convert_alpha())
        self.images.append(pygame.image.load('Images/run1.png').convert_alpha())
        self.images.append(pygame.image.load('Images/run2.png').convert_alpha())
        self.images.append(pygame.image.load('Images/run3.png').convert_alpha())
        self.images.append(pygame.image.load('Images/run4.png').convert_alpha())
        self.images.append(pygame.image.load('Images/run5.png').convert_alpha())

        self.counter = 0

        # all the images contained within the array
        self.bowImages = []

        self.bowImages.append(pygame.image.load('Images/bow0.png').convert_alpha())
        self.bowImages.append(pygame.image.load('Images/bow1.png').convert_alpha())
        self.bowImages.append(pygame.image.load('Images/bow2.png').convert_alpha())
        self.bowImages.append(pygame.image.load('Images/bow3.png').convert_alpha())
        self.bowImages.append(pygame.image.load('Images/bow4.png').convert_alpha())
        self.bowImages.append(pygame.image.load('Images/bow5.png').convert_alpha())
        self.bowImages.append(pygame.image.load('Images/bow6.png').convert_alpha())
        self.bowImages.append(pygame.image.load('Images/bow7.png').convert_alpha())
        self.bowImages.append(pygame.image.load('Images/bow8.png').convert_alpha())

        self.bCounter = 0

        # all the images contained within the array
        self.invertedImages = []

        self.invertedImages.append(pygame.image.load('Images/irun0.png').convert_alpha())
        self.invertedImages.append(pygame.image.load('Images/irun1.png').convert_alpha())
        self.invertedImages.append(pygame.image.load('Images/irun2.png').convert_alpha())
        self.invertedImages.append(pygame.image.load('Images/irun3.png').convert_alpha())
        self.invertedImages.append(pygame.image.load('Images/irun4.png').convert_alpha())
        self.invertedImages.append(pygame.image.load('Images/irun5.png').convert_alpha())

        self.iCounter = 0

        # all the images contained within the array
        self.crouchImages = []

        self.crouchImages.append(pygame.image.load('Images/crouch0.png').convert_alpha())
        self.crouchImages.append(pygame.image.load('Images/crouch1.png').convert_alpha())
        self.crouchImages.append(pygame.image.load('Images/crouch2.png').convert_alpha())
        self.crouchImages.append(pygame.image.load('Images/crouch3.png').convert_alpha())

        self.cCounter = 0

        # all the images contained within the array
        self.standImages = []

        self.standImages.append(pygame.image.load('Images/stand0.png').convert_alpha())
        self.standImages.append(pygame.image.load('Images/stand1.png').convert_alpha())
        self.standImages.append(pygame.image.load('Images/stand2.png').convert_alpha())
        self.standImages.append(pygame.image.load('Images/stand3.png').convert_alpha())

        self.sCounter = 0

        # all the images contained within the array
        self.attack2Images = []

        self.attack2Images.append(pygame.image.load('Images/a2_0.png').convert_alpha())
        self.attack2Images.append(pygame.image.load('Images/a2_1.png').convert_alpha())
        self.attack2Images.append(pygame.image.load('Images/a2_2.png').convert_alpha())
        self.attack2Images.append(pygame.image.load('Images/a2_3.png').convert_alpha())
        self.attack2Images.append(pygame.image.load('Images/a2_4.png').convert_alpha())
        self.attack2Images.append(pygame.image.load('Images/a2_5.png').convert_alpha())

        self.a2Counter = 0

    def stand(self):
        # selecting a specific image from the array
        self.image = self.standImages[self.sCounter]

        time.sleep(0.05)
        self.sCounter += 1

        # restart the loop
        if self.sCounter >= len(self.standImages):
            self.sCounter = 0

        self.image = self.standImages[self.sCounter]

    def moveLeft(self,pixels):
        self.rect.x -= pixels

        # selecting a specific image from the array
        self.image = self.invertedImages[self.iCounter]

        time.sleep(0.05)
        self.iCounter += 1

        # restart the loop
        if self.iCounter >= len(self.invertedImages):
            self.iCounter = 0

    def moveRight(self, pixels):
        self.rect.x += pixels

        # selecting a specific image from the array
        self.image = self.images[self.counter]

        time.sleep(0.02)
        self.counter += 1

        # restart the loop
        if self.counter >= len(self.images):
            self.counter = 0

        self.image = self.images[self.counter]

    def shoot(self):
        # selecting a specific image from the array
        self.image = self.bowImages[self.bCounter]

        time.sleep(0.04)
        self.bCounter += 1

        #restart the loop
        if self.bCounter >= len(self.bowImages):
            self.bCounter = 0

        self.image = self.bowImages[self.bCounter]



    def slash2(self):
        # selecting a specific image from the array
        self.image = self.attack2Images[self.a2Counter]

        time.sleep(0.04)
        self.a2Counter += 1

        #restart the loop
        if self.a2Counter >= len(self.attack2Images):
            self.a2Counter = 0

        self.image = self.attack2Images[self.a2Counter]

    def crouch(self):
        # selecting a specific image from the array
        self.image = self.crouchImages[self.cCounter]

        time.sleep(0.05)
        self.cCounter += 1

        #restart the loop
        if self.cCounter >= len(self.crouchImages):
            self.cCounter = 0

        self.image = self.crouchImages[self.cCounter]
















