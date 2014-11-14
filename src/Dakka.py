import pygame

from Enumerations import EventType
from Object import Object

class Dakka(Object):
    def __init__(self):
        super(Dakka, self).__init__()
        self.hitbox = pygame.Rect(0, 0, 16, 16)
        self.image = pygame.image.load("images/RedBall.png").convert()
        self.target = None
        self.xPosition = 0
        self.yPosition = 0

    def register(self):
        event = pygame.event.Event(EventType.registerDakka, {"dakka": self})
        pygame.event.post(event)

    def unregister(self):
        event = pygame.event.Event(EventType.unregisterDakka, {"dakka": self})
        pygame.event.post(event)

    def update(self):
        super(Dakka, self).update()
        self.hitbox.left = self.xPosition
        self.hitbox.top = self.yPosition
        if self.xPosition < 0 or self.xPosition > 640 or self.yPosition < 0 or self.yPosition > 480:
            self.unregister()
            return