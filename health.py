import pygame
import time

class Health(pygame.sprite.Sprite):

    def __init__(self,surface3):
        super().__init__()

        self.rect = pygame.Rect(683, 384, 300, 800)

        self.image = surface3

    def one(self):
        self.image = pygame.image.load('Images/heart0.png')

    def two(self):
        self.image = pygame.image.load('Images/heart1.png')

    def three(self):
        self.image = pygame.image.load('Images/heart2.png')

