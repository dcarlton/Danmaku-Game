import pygame

class EventType:
    registerDakka = pygame.USEREVENT # Attribute dakka contains the Dakka to be registered
    unregisterDakka = pygame.USEREVENT + 1
    registerCharacter = pygame.USEREVENT + 2 # Attribute character contains the Character to be registered
    unregisterCharacter = pygame.USEREVENT + 3