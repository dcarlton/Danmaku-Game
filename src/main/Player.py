import pygame

from Character import Character
from Constants import *
from Dakka import Dakka
from Enumerations import EventType

class Player(Character):
    def __init__(self, x = MAP_WIDTH / 2, y = MAP_HEIGHT - 100):
        super(Player, self).__init__()
        self.image = pygame.image.load("images/KyokoStanding.png").convert()
        self.firing = False
        self.lives = 2
        self.xPosition = x
        self.yPosition = y
        self.hitbox = pygame.Rect(self.xPosition + 6, self.yPosition + 6, 4, 4)
        self.dakkaDelay = 0

    def fire(self):
        if self.dakkaDelay != 0:
            self.dakkaDelay -= 1
        else:
            dakka = Dakka(self.xPosition, self.yPosition - 16)
            dakka.ySpeed = -6
            dakka.target = "Enemy"
            dakka.register()

            self.dakkaDelay = 4

    def hit(self, dakka):
        if dakka.target == "Player":
            self.lives -= 1
            if self.lives < 0:
                event = pygame.event.Event(EventType.outOfLives)
                pygame.event.post(event)
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

        if self.firing:
            self.fire()