import pygame
import sys
import time
import math

sys.path.append("src/main")
from Constants import *
from Dakka import Dakka
from Enemy import Enemy
from Enumerations import EventType
from Player import Player
from Updater import Updater

screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
updater = Updater()

pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.KEYDOWN,
                          pygame.KEYUP,
                          EventType.registerDakka,
                          EventType.unregisterDakka,
                          EventType.registerCharacter,
                          EventType.unregisterCharacter,
                          EventType.outOfLives,
                          EventType.win
                          ])


player = Player()
player.register()

class Stage1RotateEnemy(Enemy):
    def pattern(self):
        angle = 1.5 * math.pi
        while True:
            dakka = self.makeDakka(self.xPosition, self.yPosition)
            dakka.xSpeed = 6 * math.sin(angle)
            dakka.ySpeed = 6 * math.cos(angle)
            dakka.target = "Player"
            dakka.register()

            angle += (0.25 * math.pi)
            time.sleep(0.25)

Stage1RotateEnemy(100, 100)
Stage1RotateEnemy(540, 100)
Stage1RotateEnemy(100, 250)
Stage1RotateEnemy(540, 250)
Stage1RotateEnemy(100, 400)
Stage1RotateEnemy(540, 400)

clock = pygame.time.Clock()
while True:
    updater.update()
    # THIS CODE SHOULD BE IN A STAGE
    if len(updater.characters) == 1:
        event = pygame.event.Event(EventType.win)
        pygame.event.post(event)
    for event in pygame.event.get(EventType.outOfLives):
        print "Game over! You lose!"
        exit()
    for event in pygame.event.get(EventType.win):
        print "You win!"
        exit()
    clock.tick(60)
