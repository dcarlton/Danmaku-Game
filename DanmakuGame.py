import pygame
import thread
import sys

sys.path.append("src/main")
from Enemy import Enemy
from Enumerations import EventType
from Player import Player
from Updater import Updater

screen = pygame.display.set_mode((640, 480))
updater = Updater()

pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.KEYDOWN,
                          pygame.KEYUP,
                          EventType.registerDakka,
                          EventType.unregisterDakka,
                          EventType.registerCharacter,
                          EventType.unregisterCharacter
                          ])


player = Player()
player.hitbox.move_ip(player.xPosition, player.yPosition)
player.register()

enemy1 = Enemy()
enemy1.xPosition = 100
enemy1.yPosition = 100
enemy1.hitbox.left = enemy1.xPosition
enemy1.hitbox.top = enemy1.yPosition
thread.start_new_thread(enemy1.fire, ())
enemy1.register()

enemy2 = Enemy()
enemy2.xPosition = 540
enemy2.yPosition = 100
enemy2.hitbox.left = enemy2.xPosition
enemy2.hitbox.top = enemy2.yPosition
thread.start_new_thread(enemy2.fire, ())
enemy2.register()

enemy3 = Enemy()
enemy3.xPosition = 100
enemy3.yPosition = 250
enemy3.hitbox.left = enemy3.xPosition
enemy3.hitbox.top = enemy3.yPosition
thread.start_new_thread(enemy3.fire, ())
enemy3.register()

enemy4 = Enemy()
enemy4.xPosition = 540
enemy4.yPosition = 250
enemy4.hitbox.left = enemy4.xPosition
enemy4.hitbox.top = enemy4.yPosition
thread.start_new_thread(enemy4.fire, ())
enemy4.register()

enemy5 = Enemy()
enemy5.xPosition = 100
enemy5.yPosition = 400
enemy5.hitbox.left = enemy5.xPosition
enemy5.hitbox.top = enemy5.yPosition
thread.start_new_thread(enemy5.fire, ())
enemy5.register()

enemy6 = Enemy()
enemy6.xPosition = 540
enemy6.yPosition = 400
enemy6.hitbox.left = enemy6.xPosition
enemy6.hitbox.top = enemy6.yPosition
thread.start_new_thread(enemy6.fire, ())
enemy6.register()

clock = pygame.time.Clock()
while True:
    updater.update()
    clock.tick(60)
