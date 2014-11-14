import pygame
import sys

sys.path.append("src/main")

from Dakka import Dakka
from Enumerations import EventType

pygame.display.set_mode((640, 480))

def test_dakkaRegister():
    dakka = Dakka()
    dakka.register()
    event = pygame.event.get(EventType.registerDakka)[0]
    assert event.dakka == dakka

def test_dakkaUnregister():
    dakka = Dakka()
    dakka.unregister()
    event = pygame.event.get(EventType.unregisterDakka)[0]
    assert event.dakka == dakka

def test_dakkaMovesWhenUpdated():
    dakka = Dakka()
    dakka.xPosition = 0
    dakka.yPosition = 0
    dakka.xAcceleration = 1
    dakka.yAcceleration = 1
    dakka.update()
    assert dakka.xPosition == 1
    assert dakka.yPosition == 1

def test_dakkaHitboxMovesWhenUpdated():
    dakka = Dakka()
    dakka.xPosition = 0
    dakka.yPosition = 0
    dakka.xAcceleration = 1
    dakka.yAcceleration = 1
    dakka.update()
    assert dakka.hitbox.left == 1
    assert dakka.hitbox.top == 1

def test_dakkaUnregistersWhenOffScreen():
    dakka = Dakka()
    dakka.xPosition = -1
    dakka.yPosition = -1
    dakka.update()
    event = pygame.event.get(EventType.unregisterDakka)[0]
    assert event.dakka == dakka