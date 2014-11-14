import pygame

from Enumerations import EventType
from Object import Object

class Character(Object):
    def register(self):
        event = pygame.event.Event(EventType.registerCharacter, {"character": self})
        pygame.event.post(event)

    def unregister(self):
        event = pygame.event.Event(EventType.unregisterCharacter, {"character": self})
        pygame.event.post(event)