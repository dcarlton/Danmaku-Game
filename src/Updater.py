import pygame

from Enumerations import EventType

class Updater:
    def __init__(self):
        self.characters = []
        self.dakkaList = []
        self.screen = pygame.display.get_surface()

    def checkEvents(self):
        for event in pygame.event.get(EventType.registerDakka):
            self.dakkaList.append(event.dakka)
        for event in pygame.event.get(EventType.unregisterDakka):
            self.dakkaList.remove(event.dakka)
        for event in pygame.event.get(EventType.registerCharacter):
            self.characters.append(event.character)
        for event in pygame.event.get(EventType.unregisterCharacter):
            self.characters.remove(event.character)

    def update(self):
        self.screen.fill((255, 255, 255))
        self.checkEvents()
        for dakka in self.dakkaList:
            for character in self.characters:
                if dakka.hitbox.colliderect(character.hitbox) and character.hit(dakka):
                    dakka.unregister()
            dakka.update()
            self.screen.blit(dakka.image, (dakka.xPosition, dakka.yPosition))
        for character in self.characters:
            character.update()
            self.screen.blit(character.image, (character.xPosition, character.yPosition))
        pygame.display.flip()