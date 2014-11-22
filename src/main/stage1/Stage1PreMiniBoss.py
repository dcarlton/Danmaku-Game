import math
import pygame
import time

from Dakka import Dakka
from Enemy import Enemy
from Player import Player

class Stage1PreMiniBoss:
    def __init__(self):
        class Stage1RotateEnemy(Enemy):
            def pattern(self):
                try:
                  while True:
                    angle = math.atan2(Player.y - self.yPosition, Player.x - self.xPosition)
                    dakka = Dakka(self.xPosition, self.yPosition)
                    dakka.xSpeed = 6 * math.cos(angle)
                    dakka.ySpeed = 6 * math.sin(angle)
                    dakka.target = "Player"
                    dakka.register()
                    time.sleep(0.25)
                except:
                  pass

        enemies = []
        enemies.append(Stage1RotateEnemy(200, 100))
        enemies.append(Stage1RotateEnemy(250, 100))
        enemies.append(Stage1RotateEnemy(300, 100))
        enemies.append(Stage1RotateEnemy(350, 100))
        enemies.append(Stage1RotateEnemy(400, 100))
        enemies.append(Stage1RotateEnemy(450, 100))
        for enemy in enemies:
            enemy.init()

        time.sleep(5)
        for enemy in enemies:
            enemy.hp = 0