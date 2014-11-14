import math
import pygame
import sys
import thread
import time

sys.path.append("./src")

from Object import Object

characters = []
objects = []
screen = pygame.display.set_mode((640, 480))

pygame.event.set_allowed(None)
pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP, pygame.USEREVENT])

class Shot(Object):
    def __init__(self):
        super(Shot, self).__init__()
        self.hitbox = pygame.Rect(0, 0, 16, 16)
        self.image = pygame.image.load("images/RedBall.png").convert()
        self.target = None
        self.xPosition = 0
        self.yPosition = 0

    def update(self):
        super(Shot, self).update()
        self.hitbox.left = self.xPosition
        self.hitbox.top = self.yPosition
        if self.xPosition < 0 or self.xPosition > 640 or self.yPosition < 0 or self.yPosition > 480:
            objects.remove(self)
            return
        for thingy in characters:
            if self.hitbox.colliderect(thingy.hitbox) and thingy.hit(self):
                objects.remove(self)
                return

class Enemy(Object):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("images/KyokoStanding.png").convert()
        self.hitbox = pygame.Rect(0, 0, 16, 16)
        self.hp = 50
        self.xPosition = 0
        self.yPosition = 0

    def fire(self):
        angle = 1.5 * math.pi
        while True:
            if self.hp <= 0:
                characters.remove(self)
                thread.exit()

            shot = Shot()
            shot.xPosition = self.xPosition
            shot.yPosition = self.yPosition
            shot.xSpeed = 6 * math.sin(angle)
            shot.ySpeed = 6 * math.cos(angle)
            shot.target = "Player"
            event = pygame.event.Event(pygame.USEREVENT, {"shot": shot})
            pygame.event.post(event)

            angle += (0.25 * math.pi)
            time.sleep(0.25)

    def hit(self, shot):
        if shot.target == "Enemy":
            self.hp -= 1
            return True
        return False

class Player(Object):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("images/KyokoStanding.png").convert()
        self.firing = False
        self.hitbox = pygame.Rect(0, 0, 16, 16)
        self.xPosition = 320
        self.yPosition = 240
        self.shotDelay = 0

    def hit(self, shot):
        if shot.target == "Player":
            print "Hit!"
            return True
        return False

    def update(self):
        for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP]):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_UP:
                    self.ySpeed -= 6
                elif event.key == pygame.K_DOWN:
                    self.ySpeed += 6
                elif event.key == pygame.K_LEFT:
                    self.xSpeed -= 6
                elif event.key == pygame.K_RIGHT:
                    self.xSpeed += 6
                elif event.key == pygame.K_SEMICOLON:
                    self.firing = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ySpeed += 6
                elif event.key == pygame.K_DOWN:
                    self.ySpeed -= 6
                elif event.key == pygame.K_LEFT:
                    self.xSpeed += 6
                elif event.key == pygame.K_RIGHT:
                    self.xSpeed -= 6
                elif event.key == pygame.K_SEMICOLON:
                    self.firing = False

        super(Player, self).update()
        self.hitbox.left = self.xPosition
        self.hitbox.top = self.yPosition

        if self.firing:
            if self.shotDelay != 0:
                self.shotDelay -= 1
            else:
                shot = Shot()
                shot.xPosition = player.xPosition
                shot.yPosition = player.yPosition - 16
                shot.ySpeed = -6
                shot.target = "Enemy"
                event = pygame.event.Event(pygame.USEREVENT, {"shot": shot})
                pygame.event.post(event)

                self.shotDelay = 4


player = Player()
player.hitbox.move_ip(player.xPosition, player.yPosition)
characters.append(player)

enemy1 = Enemy()
enemy1.xPosition = 100
enemy1.yPosition = 100
enemy1.hitbox.left = enemy1.xPosition
enemy1.hitbox.top = enemy1.yPosition
thread.start_new_thread(enemy1.fire, ())
characters.append(enemy1)

enemy2 = Enemy()
enemy2.xPosition = 540
enemy2.yPosition = 100
enemy2.hitbox.left = enemy2.xPosition
enemy2.hitbox.top = enemy2.yPosition
thread.start_new_thread(enemy2.fire, ())
characters.append(enemy2)

enemy3 = Enemy()
enemy3.xPosition = 100
enemy3.yPosition = 250
enemy3.hitbox.left = enemy3.xPosition
enemy3.hitbox.top = enemy3.yPosition
thread.start_new_thread(enemy3.fire, ())
characters.append(enemy3)

enemy4 = Enemy()
enemy4.xPosition = 540
enemy4.yPosition = 250
enemy4.hitbox.left = enemy4.xPosition
enemy4.hitbox.top = enemy4.yPosition
thread.start_new_thread(enemy4.fire, ())
characters.append(enemy4)

enemy5 = Enemy()
enemy5.xPosition = 100
enemy5.yPosition = 400
enemy5.hitbox.left = enemy5.xPosition
enemy5.hitbox.top = enemy5.yPosition
thread.start_new_thread(enemy5.fire, ())
characters.append(enemy5)

enemy6 = Enemy()
enemy6.xPosition = 540
enemy6.yPosition = 400
enemy6.hitbox.left = enemy6.xPosition
enemy6.hitbox.top = enemy6.yPosition
thread.start_new_thread(enemy6.fire, ())
characters.append(enemy6)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get(pygame.USEREVENT):
        objects.append(event.shot)
    screen.fill((255, 255, 255))
    for thingy in characters:
        thingy.update()
        screen.blit(thingy.image, (thingy.xPosition, thingy.yPosition))
    for thingy in objects:
        thingy.update()
        screen.blit(thingy.image, (thingy.xPosition, thingy.yPosition))
    pygame.display.flip()

    clock.tick(60)
