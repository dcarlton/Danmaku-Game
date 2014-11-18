import pygame
import math
import sys
import thread
import time

from Character import Character
from Dakka import Dakka
from Enumerations import EventType

class Enemy(Character):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        self.alive = True
        self.image = pygame.image.load("images/KyokoStanding.png").convert()
        self.hitbox = pygame.Rect(x, y, 16, 16)
        self.hp = 1
        self.xPosition = x
        self.yPosition = y

        thread.start_new_thread(self.pattern, ())
        self.register()

    def hit(self, dakka):
        if dakka.target == "Enemy":
            self.hp -= 1
            if self.hp <= 0:
                self.alive = False
                self.unregister()
            return True
        return False

    def makeDakka(self, x, y):
        if self.alive:
            return Dakka(x, y)
        else:
            # Kill the thread!
            sys.exit()

    def pattern(self):
        pass