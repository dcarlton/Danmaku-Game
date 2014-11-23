import pygame
import random
import time

from Boss import Boss
from Constants import *
from Dakka import Dakka

class Stage1MiniBoss(Boss):
    def __init__(self):
        super(Stage1MiniBoss, self).__init__()
        #self.image = pygame.image.load("images/KyokoStanding.png").convert()
        self.spellcards = [self.blitz]
        self.attack()

    def blitz(self):
        try:
            self.hp = 100
            self.timeout = 30
            clock = pygame.time.Clock()
            while True:
                dakka = Dakka(random.randint(0, MAP_WIDTH), 0)
                dakka.xSpeed = random.uniform(-3, 3)
                dakka.ySpeed = 4
                dakka.target = "Player"
                dakka.register()
                clock.tick(15)
        except:
            pass