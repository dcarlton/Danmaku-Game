import pygame
import sys

sys.path.append("src/main")

from Dakka import Dakka
from Enumerations import EventType
from Player import Player

pygame.display.set_mode((640, 480))

def test_playerRegister():
    player = Player()
    player.register()
    event = pygame.event.get(EventType.registerCharacter)[0]
    assert event.character == player

def test_playerUnregister():
    player = Player()
    player.unregister()
    event = pygame.event.get(EventType.unregisterCharacter)[0]
    assert event.character == player

def test_playerMovesWhenUpdated():
    player = Player()
    player.xPosition = 0
    player.yPosition = 0
    player.xAcceleration = 1
    player.yAcceleration = 1
    player.update()
    assert player.xPosition == 1
    assert player.yPosition == 1

def test_playerHitboxMovesWhenUpdated():
    player = Player()
    player.xPosition = 0
    player.yPosition = 0
    hitboxLeft = player.hitbox.left
    hitboxTop = player.hitbox.top
    player.xAcceleration = 1
    player.yAcceleration = 1
    player.update()
    assert player.hitbox.left == hitboxLeft + 1
    assert player.hitbox.top == hitboxTop + 1

def test_playerHitboxSize():
    # Give Player a constructor that takes a starting position
    player = Player()
    player.hitbox.left = 0
    player.hitbox.top = 0
    assert not player.hitbox.colliderect(pygame.Rect(4, 4, 1000, 1000))

def test_playerCanBeHit():
    player = Player()
    dakka = Dakka(player.xPosition, player.yPosition)
    dakka.target = "Player"
    assert player.hitbox.colliderect(dakka.hitbox) and player.hit(dakka)

def test_playerFiresDakka():
    player = Player()
    fireEvent = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_SEMICOLON} )
    pygame.event.post(fireEvent)
    player.update()
    event = pygame.event.get(EventType.registerDakka)[0]
    assert event.dakka
    assert event.dakka.target == "Enemy"

def test_playerStopsFiringDakka():
    player = Player()
    player.firing = True
    stopFiring = pygame.event.Event(pygame.KEYUP, {"key": pygame.K_SEMICOLON} )
    pygame.event.post(stopFiring)
    player.update()
    event = pygame.event.get(EventType.registerDakka)
    assert event == []

def test_playerRespondsToDownArrow():
    player = Player()
    player.yPosition = 100
    event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_DOWN} )
    pygame.event.post(event)
    player.update()
    assert player.yPosition > 100

    event = pygame.event.Event(pygame.KEYUP, {"key": pygame.K_DOWN} )
    pygame.event.post(event)
    player.update()
    assert player.ySpeed == 0

def test_playerRespondsToLeftArrow():
    player = Player()
    player.xPosition = 100
    event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_LEFT} )
    pygame.event.post(event)
    player.update()
    assert player.xPosition < 100

    event = pygame.event.Event(pygame.KEYUP, {"key": pygame.K_LEFT} )
    pygame.event.post(event)
    player.update()
    assert player.xSpeed == 0

def test_playerRespondsToRightArrow():
    player = Player()
    player.xPosition = 100
    event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RIGHT} )
    pygame.event.post(event)
    player.update()
    assert player.xPosition > 100

    event = pygame.event.Event(pygame.KEYUP, {"key": pygame.K_RIGHT} )
    pygame.event.post(event)
    player.update()
    assert player.xSpeed == 0

def test_playerRespondsToUpArrow():
    player = Player()
    player.yPosition = 100
    event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_UP} )
    pygame.event.post(event)
    player.update()
    assert player.yPosition < 100

    event = pygame.event.Event(pygame.KEYUP, {"key": pygame.K_UP} )
    pygame.event.post(event)
    player.update()
    assert player.ySpeed == 0