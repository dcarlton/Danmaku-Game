import pygame
import stopit
import thread
import time

from Constants import *
from Enemy import Enemy
from Enumerations import EventType

class Boss(Enemy):
    def __init__(self):
        super(Boss, self).__init__(MAP_WIDTH / 2, 75)
        self.spellcards = None
        self.attackThread = None
        self.timeoutThread = None
        self.timeout = 30
        self.hp = 50
        self.register()

    def attack(self):
        try:
            clock = pygame.time.Clock()
            for spellcard in self.spellcards:
                self.timeout = 3
                self.attackThread = thread.start_new_thread(spellcard, ())
                self.timeoutThread = thread.start_new_thread(self.watchTimeout, ())

                while pygame.event.get(EventType.endSpellcard) == []:
                    clock.tick(60)
            self.endFight()
        except:
            self.die()
            self.endFight()

    def die(self):
        if self.attackThread is not None and self.timeoutThread is not None:
            stopit.async_raise(self.attackThread, Exception)
            self.attackThread = None
            stopit.async_raise(self.timeoutThread, Exception)
            self.timeoutThread = None
            event = pygame.event.Event(EventType.endSpellcard)
            pygame.event.post(event)

    def endFight(self):
        self.unregister()

    def init(self):
        self.register()
        self.attack()

    def watchTimeout(self):
        try:
            while self.timeout > 0 and self.hp > 0:
                time.sleep(1)
                self.timeout -= 1
                print "Time remaining: " + str(self.timeout)
            self.die()
        except:
            pass