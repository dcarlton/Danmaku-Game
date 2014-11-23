import pygame

class EventType:
    registerDakka = pygame.USEREVENT # Attribute dakka contains the Dakka to be registered
    unregisterDakka = pygame.USEREVENT + 1
    registerCharacter = pygame.USEREVENT + 2 # Attribute character contains the Character to be registered
    unregisterCharacter = pygame.USEREVENT + 3
    outOfLives = pygame.USEREVENT + 4
    win = pygame.USEREVENT + 5
    endSpellcard = pygame.USEREVENT + 6