import pygame
import sys

sys.path.append("src/main")
from Constants import *
from Enumerations import EventType
from Starter import Starter

screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))

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

Starter().startCampaign()