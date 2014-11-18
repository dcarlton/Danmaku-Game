import pygame
import thread
import sys

sys.path.append("src/main")
from Constants import *
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
                          EventType.outOfLives
                          ])


player = Player()
player.register()

enemy1 = Enemy(100, 100)
thread.start_new_thread(enemy1.fire, ())
enemy1.register()

enemy2 = Enemy(540, 100)
thread.start_new_thread(enemy2.fire, ())
enemy2.register()

enemy3 = Enemy(100, 250)
thread.start_new_thread(enemy3.fire, ())
enemy3.register()

enemy4 = Enemy(540, 250)
thread.start_new_thread(enemy4.fire, ())
enemy4.register()

enemy5 = Enemy(100, 400)
thread.start_new_thread(enemy5.fire, ())
enemy5.register()

enemy6 = Enemy(540, 400)
thread.start_new_thread(enemy6.fire, ())
enemy6.register()

clock = pygame.time.Clock()
while True:
    updater.update()
    for event in pygame.event.get(EventType.outOfLives):
        print "Game over! You lose!"
        exit()
    clock.tick(60)
