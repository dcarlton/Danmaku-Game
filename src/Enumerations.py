import pygame

class EventType:
    registerDakka = pygame.USEREVENT # Attribute dakka contains the Dakka to be registered
    unregisterDakka = pygame.USEREVENT + 1
    registerCharacter = pygame.USEREVENT + 2
    unregisterCharacter = pygame.USEREVENT + 3