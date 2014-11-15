import math
import thread
import time
import pygame

from Character import Character
from Dakka import Dakka
from Enumerations import EventType

class Enemy(Character):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("images/KyokoStanding.png").convert()
        self.hitbox = pygame.Rect(x, y, 16, 16)
        self.hp = 50
        self.xPosition = x
        self.yPosition = y

    def fire(self):
        angle = 1.5 * math.pi
        while True:
            if self.hp <= 0:
                self.unregister()
                thread.exit()

            dakka = Dakka(self.xPosition, self.yPosition)
            dakka.xSpeed = 6 * math.sin(angle)
            dakka.ySpeed = 6 * math.cos(angle)
            dakka.target = "Player"
            dakka.register()

            angle += (0.25 * math.pi)
            time.sleep(0.25)

    def hit(self, dakka):
        if dakka.target == "Enemy":
            self.hp -= 1
            return True
        return False