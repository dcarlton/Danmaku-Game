from datetime import datetime
import math
import pygame
import sys
import thread
import time

objects = []
screen = pygame.display.set_mode((640, 480))

pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP, pygame.USEREVENT])

class Shot:
    xPosition = 0
    yPosition = 0
    xSpeed = 0
    ySpeed = 0
    image = pygame.image.load("images/RedBall.png").convert()

    def update(self):
        self.xPosition += self.xSpeed
        self.yPosition += self.ySpeed
        if self.xPosition < 0 or self.xPosition > 640 or self.yPosition < 0 or self.yPosition > 480:
            objects.remove(self)

class Enemy(Shot):
    image = pygame.image.load("images/KyokoStanding.png").convert()
    def fire(self):
        angle = 1.5 * math.pi
        while True:
            shot = Shot()
            shot.xPosition = self.xPosition
            shot.yPosition = self.yPosition
            shot.xSpeed = 6 * math.sin(angle)
            shot.ySpeed = 6 * math.cos(angle)
            event = pygame.event.Event(pygame.USEREVENT, {"shot": shot})
            pygame.event.post(event)
            #objects.append(shot)

            angle += (0.25 * math.pi)
            time.sleep(0.25)

    def update(self):
        pass

class Player(Shot):
    image = pygame.image.load("images/KyokoStanding.png").convert()
    move = "No"
    xPosition = 320
    yPosition = 240

    def update(self):
        for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP]):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_UP:
                    self.move = "Up"
                if event.key == pygame.K_DOWN:
                    self.move = "Down"
            elif event.type == pygame.KEYUP:
                self.move = "No"
        if self.move == "Up":
            self.yPosition -= 1
        elif self.move == "Down":
            self.yPosition += 1


player = Player()
objects.append(player)

enemy1 = Enemy()
enemy1.xPosition = 100
enemy1.yPosition = 100
thread.start_new_thread(enemy1.fire, ())
objects.append(enemy1)

enemy2 = Enemy()
enemy2.xPosition = 540
enemy2.yPosition = 100
thread.start_new_thread(enemy2.fire, ())
objects.append(enemy2)

enemy3 = Enemy()
enemy3.xPosition = 100
enemy3.yPosition = 250
thread.start_new_thread(enemy3.fire, ())
objects.append(enemy3)

enemy4 = Enemy()
enemy4.xPosition = 540
enemy4.yPosition = 250
thread.start_new_thread(enemy4.fire, ())
objects.append(enemy4)

enemy5 = Enemy()
enemy5.xPosition = 100
enemy5.yPosition = 400
thread.start_new_thread(enemy5.fire, ())
objects.append(enemy5)

enemy6 = Enemy()
enemy6.xPosition = 540
enemy6.yPosition = 400
thread.start_new_thread(enemy6.fire, ())
objects.append(enemy6)

while True:
    startTime = datetime.now()
    for event in pygame.event.get(pygame.USEREVENT):
        objects.append(event.shot)
    screen.fill((255, 255, 255))
    for thingy in objects:
        thingy.update()
        screen.blit(thingy.image, (thingy.xPosition, thingy.yPosition))
    pygame.display.flip()

    endTime = datetime.now()
    delta = (endTime - startTime).microseconds
    if delta < 326667:
        waitTime = (326667 - delta) / 1000000
        time.sleep(waitTime)
