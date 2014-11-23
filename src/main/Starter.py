import pygame
import stopit
import sys
import thread

sys.path.append("src/main/stage1")

from Enumerations import EventType
from Player import Player
from Stage1PreMiniBoss import Stage1PreMiniBoss
from Stage1MiniBoss import Stage1MiniBoss
from Updater import Updater

class Starter:
    # startWhatever should be class functions, should be impossible to create a Starter
    gameThread = None

    def gameloop(self):
        updater = Updater()
        player = Player()
        player.register()

        clock = pygame.time.Clock()
        while True:
            updater.update()
            for event in pygame.event.get(EventType.outOfLives):
                if Starter.gameThread is not None:
                    stopit.async_raise(Starter.gameThread, Exception)
                pygame.font.init()
                text = pygame.font.SysFont(None, 120).render("You lost!", False, (0, 0, 0))
                pygame.display.get_surface().blit(text, (100, 200))
                pygame.display.flip()
                import time
                time.sleep(3)
                return
            for event in pygame.event.get(EventType.win):
                if Starter.gameThread is not None:
                    stopit.async_raise(Starter.gameThread, Exception)
                pygame.font.init()
                text = pygame.font.SysFont(None, 120).render("You win!", False, (0, 0, 0))
                pygame.display.get_surface().blit(text, (100, 200))
                pygame.display.flip()
                import time
                time.sleep(3)
                return
            clock.tick(60)

    def startCampaign(self):
        Starter.gameThread = thread.start_new_thread(self.campaign, ())
        self.gameloop()

    def startStage1(self):
        Starter.gameThread = thread.start_new_thread(self.stage1(), ())
        self.gameloop()

    def startStage2(self):
        Starter.gameThread = thread.start_new_thread(self.stage2(), ())
        self.gameloop()

    def startStage3(self):
        Starter.gameThread = thread.start_new_thread(self.stage3(), ())
        self.gameloop()

    def startStage4(self):
        Starter.gameThread = thread.start_new_thread(self.stage4(), ())
        self.gameloop()

    def startStage5(self):
        Starter.gameThread = thread.start_new_thread(self.stage5(), ())
        self.gameloop()

    def startStage6(self):
        Starter.gameThread = thread.start_new_thread(self.stage6(), ())
        self.gameloop()

    def campaign(self):
        self.stage1()
        self.stage2()
        self.stage3()
        self.stage4()
        self.stage5()
        self.stage6()
        Starter.gameThread = None
        event = pygame.event.Event(EventType.win)
        pygame.event.post(event)

    def stage1(self):
        #Stage1PreMiniBoss()
        Stage1MiniBoss()

    def stage2(self):
        pass

    def stage3(self):
        pass

    def stage4(self):
        pass

    def stage5(self):
        pass

    def stage6(self):
        pass