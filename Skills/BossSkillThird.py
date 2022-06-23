import time, pygame, win32gui, random, main, Event, Move, threading, Bullt, math, OEmoji, Frame, main, wx


class BossSkillThird:
    stopok = False

    @classmethod
    def teleport(cls):
        while Event.Game.haveBoss:
            while Event.Game.istimestoptime:
                time.sleep(1)
            Event.Game.boss.x = random.randint(400, 560)
            Event.Game.boss.y = random.randint(0, 400)
            time.sleep(1)

    @classmethod
    def superShoot(cls):
        index = 10
        dir = 1
        for i in range(16):
            if Event.Game.haveBoss:
                while Event.Game.istimestoptime:
                    time.sleep(1)
                newbumb = Bullt.BossBumb(Event.Game.boss.x, index)
                newbumb.speed = 5
                newbumb.sample = 0
                newbumb.rect = newbumb.image.get_rect()
                newbumb.rect.left = newbumb.x
                newbumb.rect.top = newbumb.y
                if dir == 1:
                    index += 60
                else:
                    index -= 60
                if index >= 450:
                    dir = -1
                newbumb.image = Event.Game.bulluten[4]
                Event.Game.allenbumbs.append(newbumb)
                time.sleep(0.3)

    @classmethod
    def moveFrameThird(cls):
        try:
            while Event.Game.haveBoss:
                Move.moveWin(Event.Game.rx, Event.Game.ry - 10)
                time.sleep(0.2597)
                Move.moveWin(Event.Game.rx - 10, Event.Game.ry - 10)
                time.sleep(0.2597)
                Move.moveWin(Event.Game.rx - 10, Event.Game.ry)
                time.sleep(0.2597)
                Move.moveWin(Event.Game.rx, Event.Game.ry)
                time.sleep(0.2597)
        except RuntimeError:
            pass

    @classmethod
    def setgold(cls):
        Event.Game.gold = True
        Event.Game.golden.play()
        time.sleep(5)
        Event.Game.gold = False

    @classmethod
    def cutBody(cls):
        newfen = OEmoji.BossEmemy()
        newfen.x = random.randint(400, 560)
        newfen.y = random.randint(0, 400)
        newfen.bossrint = 3
        newfen.image = pygame.image.load('image/bossenemy-3.png')
        newfen.maxlive = 65 * Event.Game.bossdeathtimes
        newfen.live = 65 * Event.Game.bossdeathtimes
        newfen.isboss = False
        newfen.rint = 1
        newfen.sleepbumbtime = 3
        Event.Game.g_enemies.append(newfen)
        newfen = OEmoji.BossEmemy()
        newfen.x = random.randint(400, 560)
        newfen.y = random.randint(0, 400)
        newfen.bossrint = 3
        newfen.image = pygame.image.load('image/bossenemy-3.png')
        newfen.maxlive = 65 * Event.Game.bossdeathtimes
        newfen.live = 65 * Event.Game.bossdeathtimes
        newfen.isboss = False
        newfen.rint = 1
        newfen.sleepbumbtime = 3
        Event.Game.g_enemies.append(newfen)

    @classmethod
    def updatewhenstop(cls):
        boss3 = pygame.image.load('image/boss3.png')
        while cls.stopok:
            Event.Game.screen.blit(Event.Game.boss3r, (0, 0))
            Event.Game.screen.blit(Event.Game.wateremoji.image, (Event.Game.wateremoji.x, Event.Game.wateremoji.y))
            for i in Event.Game.g_enemies:
                i.shoot()
                try:
                    Event.Game.screen.blit(i.image, (i.x, i.y))
                except pygame.error:
                    pass
            for i in Event.Game.allenbumbs:
                Event.Game.screen.blit(i.image, (i.x, i.y))
            for i in Event.Game.wateremoji.allbumb:
                Event.Game.screen.blit(i.image, (i.x, i.y))
            try:
                for i in Event.Game.allsupply:
                    Event.Game.screen.blit(i.image, (i.x, i.y))
            except pygame.error:
                pass
            Event.Game.setDirection()
            Event.Game.boss.move()
            Event.Game.showPower()
            font2 = pygame.font.SysFont(None, 20)
            Event.Game.showLife(font2, Event.Game.screen)
            pygame.display.update()
            pygame.time.Clock().tick(Event.Game.FPS)

    @classmethod
    def timestop(cls):
        t1 = threading.Thread(target=cls.updatewhenstop)
        t1.daemon = True
        t1.start()
        Event.Game.theworld.play()
        cls.stopok = True
        timek = time.time()
        Event.Game.isBossTimestop = True
        while time.time() - timek <= 5:
            a = 1
            pass
        Event.Game.isBossTimestop = False
        cls.stopok = False
