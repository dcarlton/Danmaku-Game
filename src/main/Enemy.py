import pygame
import stopit
import thread

from Character import Character
from Dakka import Dakka
from Enumerations import EventType

class Enemy(Character):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("images/KyokoStanding.png").convert()
        self.hitbox = pygame.Rect(x, y, 16, 16)
        self.hp = 1
        self.xPosition = x
        self.yPosition = y
        self.thread = None

    def die(self):
        self.unregister()
        if self.thread is not None:
            stopit.async_raise(self.thread, Exception)
            self.thread = None

    def hit(self, dakka):
        if dakka.target == "Enemy":
            self.hp -= 1
            return True
        return False

    def init(self):
        self.register()
        self.thread = thread.start_new_thread(self.pattern, ())

    def pattern(self):
        pass

    def update(self):
        super(Enemy, self).update()
        if self.hp <= 0:
            self.die()