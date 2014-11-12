import math
import pygame
import sys

objects = []
screen = pygame.display.set_mode((640, 480))

class Shot:
    xPosition = 0
    yPosition = 0
    xSpeed = 0
    ySpeed = 0
    image = pygame.image.load("images/RedBall.png").convert()

    def update(self):
        self.xPosition += self.xSpeed
        self.yPosition += self.ySpeed

class Enemy(Shot):
    angle = 1.5 * math.pi
    image = pygame.image.load("images/KyokoStanding.png").convert()
    def fire(self):
        shot = Shot()
        shot.xPosition = self.xPosition
        shot.yPosition = self.yPosition
        shot.xSpeed = 6 * math.sin(self.angle)
        shot.ySpeed = 6 * math.cos(self.angle)
        objects.append(shot)

    def update(self):
        self.fire()
        self.angle += (0.25 * math.pi)

class Player(Shot):
    image = pygame.image.load("images/KyokoStanding.png").convert()
    move = "No"
    xPosition = 320
    yPosition = 240

    def update(self):
        for event in pygame.event.get():
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
enemy1.xPosition = 50
enemy1.yPosition = 50
objects.append(enemy1)

enemy2 = Enemy()
enemy2.xPosition = 590
enemy2.yPosition = 50
objects.append(enemy2)

while True:
    screen.fill((255, 255, 255))
    for thingy in objects:
        thingy.update()
        screen.blit(thingy.image, (thingy.xPosition, thingy.yPosition))
    pygame.display.flip()