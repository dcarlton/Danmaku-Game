import pygame
import sys

sys.path.append("src/main")

from Enemy import Enemy
from Enumerations import EventType

pygame.display.set_mode((640, 480))

def test_enemyRegister():
    enemy = Enemy(0, 0)
    enemy.register()
    event = pygame.event.get(EventType.registerCharacter)[0]
    assert event.character == enemy

def test_enemyUnregister():
    enemy = Enemy(0, 0)
    enemy.unregister()
    event = pygame.event.get(EventType.unregisterCharacter)[0]
    assert event.character == enemy

def test_enemyMovesWhenUpdated():
    enemy = Enemy(0, 0)
    enemy.xAcceleration = 1
    enemy.yAcceleration = 1
    enemy.update()
    assert enemy.xPosition == 1
    assert enemy.yPosition == 1

def test_enemyHitboxMovesWhenUpdated():
    enemy = Enemy(0, 0)
    enemy.xAcceleration = 1
    enemy.yAcceleration = 1
    enemy.update()
    assert enemy.hitbox.left == 1
    assert enemy.hitbox.top == 1