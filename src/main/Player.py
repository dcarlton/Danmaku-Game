import pygame

from Character import Character
from Dakka import Dakka
from Enumerations import EventType

class Player(Character):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("images/KyokoStanding.png").convert()
        self.firing = False
        self.hitbox = pygame.Rect(0, 0, 16, 16)
        self.xPosition = 320
        self.yPosition = 240
        self.dakkaDelay = 0

    def hit(self, dakka):
        if dakka.target == "Player":
            print "Hit!"
            return True
        return False

    def update(self):
        for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP]):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_UP:
                    self.ySpeed -= 6
                elif event.key == pygame.K_DOWN:
                    self.ySpeed += 6
                elif event.key == pygame.K_LEFT:
                    self.xSpeed -= 6
                elif event.key == pygame.K_RIGHT:
                    self.xSpeed += 6
                elif event.key == pygame.K_SEMICOLON:
                    self.firing = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ySpeed += 6
                elif event.key == pygame.K_DOWN:
                    self.ySpeed -= 6
                elif event.key == pygame.K_LEFT:
                    self.xSpeed += 6
                elif event.key == pygame.K_RIGHT:
                    self.xSpeed -= 6
                elif event.key == pygame.K_SEMICOLON:
                    self.firing = False

        super(Player, self).update()
        self.hitbox.left = self.xPosition
        self.hitbox.top = self.yPosition

        if self.firing:
            if self.dakkaDelay != 0:
                self.dakkaDelay -= 1
            else:
                dakka = Dakka()
                dakka.xPosition = self.xPosition
                dakka.yPosition = self.yPosition - 16
                dakka.ySpeed = -6
                dakka.target = "Enemy"
                dakka.register()

                self.dakkaDelay = 4