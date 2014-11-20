import pygame
import sys

sys.path.append("src/main")

from Character import Character
from Dakka import Dakka
from Enumerations import EventType
from Player import Player
from Updater import Updater

pygame.display.set_mode((640, 480))

def test_updaterRegistersCharacters():
    character = Character()
    updater = Updater()
    event = pygame.event.Event(EventType.registerCharacter, {"character": character} )
    pygame.event.post(event)
    updater.checkEvents()
    assert character in updater.characters

def test_updaterUnregistersCharacters():
    character = Character()
    updater = Updater()
    updater.characters.append(character)
    event = pygame.event.Event(EventType.unregisterCharacter, {"character": character} )
    pygame.event.post(event)
    updater.checkEvents()
    assert character not in updater.characters

def test_updaterRegistersDakka():
    dakka = Dakka(0, 0)
    updater = Updater()
    event = pygame.event.Event(EventType.registerDakka, {"dakka": dakka} )
    pygame.event.post(event)
    updater.checkEvents()
    assert dakka in updater.dakkaList

def test_updaterUnregistersDakka():
    dakka = Dakka(0, 0)
    updater = Updater()
    updater.dakkaList.append(dakka)
    event = pygame.event.Event(EventType.unregisterDakka, {"dakka": dakka} )
    pygame.event.post(event)
    updater.checkEvents()
    assert dakka not in updater.dakkaList

def test_updaterUpdatesDakkaPosition():
    dakka = Dakka(0, 0)
    dakka.xSpeed = 5
    updater = Updater()
    updater.dakkaList.append(dakka)
    updater.update()
    assert dakka.xPosition == 5

def test_updaterUpdatesCharacterPosition():
    character = Character()
    character.xPosition = 0
    character.yPosition = 0
    character.xSpeed = 5
    character.hitbox = pygame.Rect(0, 0, 0, 0)
    character.image = pygame.Surface((0, 0))
    character.register()

    updater = Updater()
    updater.update()
    assert character.xPosition == 5

def test_updaterDetectsCollisions():
    updater = Updater()

    player = Player(0, 0)
    updater.characters.append(player)

    dakka = Dakka(0, 0)
    dakka.target = "Player"
    updater.dakkaList.append(dakka)

    updater.update()
    event = pygame.event.get(EventType.unregisterDakka)[0]
    assert event.dakka == dakka