import time, pygame, win32gui, random, main, Event, Move, threading, Bullt, math, OEmoji

import wx

import Frame


class BossSkillForth:
    frame = object

    @classmethod
    def light(cls, newbumb):
        time.sleep(2)
        bumb = Bullt.BossBumb(newbumb.x - 640, newbumb.y)
        bumb.canMove = False
        bumb.banRemove = True
        bumb.canDelete = False
        bumb.image = pygame.image.load('image/light.png')
        bumb.rect = bumb.image.get_rect()
        bumb.rect.left = bumb.x
        bumb.rect.top = bumb.y
        Event.Game.allenbumbs.append(bumb)
        index = 1
        for i in range(13):
            bumb.image.set_alpha(index)
            index += 18
            time.sleep(0.08)
        Event.Game.allenbumbs.remove(newbumb)
        index = 255
        for i in range(13):
            bumb.image.set_alpha(index)
            index -= 18
            time.sleep(0.08)
        Event.Game.allenbumbs.remove(bumb)

    @classmethod
    def lightshoot(cls):
        for i in range(5):
            if Event.Game.haveBoss:
                while Event.Game.istimestoptime:
                    time.sleep(1)
                x, y = random.randint(150, main.WINDOWWIDTH - 30), random.randint(0, main.WINDOWHEIGHT - 30)
                newbumb = Bullt.BossBumb(x, y)
                newbumb.canMove = False
                newbumb.hurt = 0
                newbumb.canDelete = False
                newbumb.image = pygame.image.load('image/error.png')
                Event.Game.allenbumbs.append(newbumb)
                th = threading.Thread(target=cls.light, args=(newbumb,))
                th.daemon = True
                th.start()
                time.sleep(0.2)

    @classmethod
    def dragAttack(cls, newbumb):
        art = math.atan(newbumb.tan)
        artt = math.atan(newbumb.tan)
        sample = newbumb.sample
        while -20 <= newbumb.x < main.WINDOWWIDTH and -20 <= newbumb.y <= main.WINDOWHEIGHT and not newbumb.blow:
            while Event.Game.istimestoptime:
                time.sleep(1)
            art -= math.pi / 5
            newbumb.tan = math.tan(art)
            if math.cos(art) < 0:
                newbumb.sample = 1
            else:
                newbumb.sample = -1
            if sample == 0:
                if newbumb.direction == 'left':
                    newbumb.x -= newbumb.speed
            elif sample == 1:
                newbumb.x += math.sqrt(newbumb.speed * 10 / (1 + math.tan(artt) ** 2))
                newbumb.y += math.sqrt(newbumb.speed * 10 / (1 + math.tan(artt) ** 2)) * math.tan(artt)
            elif sample == -1:
                newbumb.x -= math.sqrt(newbumb.speed * 9 / (1 + math.tan(artt) ** 2))
                newbumb.y -= math.sqrt(newbumb.speed * 9 / (1 + math.tan(artt) ** 2)) * math.tan(artt)
            newbumb.rect.left = newbumb.x
            newbumb.rect.top = newbumb.y
            time.sleep(0.1)
        if not (-20 <= newbumb.x < main.WINDOWWIDTH and -20 <= newbumb.y <= main.WINDOWHEIGHT):
            try:
                Event.Game.allenbumbs.remove(newbumb)
            except ValueError:
                pass

    @classmethod
    def dragShoot(cls):
        for i in range(20):
            if Event.Game.haveBoss:
                while Event.Game.istimestoptime:
                    time.sleep(1)
                newbumb = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
                newbumb.image = Event.Game.bulluten[10]
                newbumb.rect = newbumb.image.get_rect()
                newbumb.rect.left = newbumb.x
                newbumb.rect.top = newbumb.y
                newbumb.banRemove = True
                Event.Game.allenbumbs.append(newbumb)
                th = threading.Thread(target=cls.dragAttack, args=(newbumb,))
                th.daemon = True
                th.start()
                time.sleep(0.2)

    @classmethod
    def sideMove(cls, tv1, tv2, tv3, tv4):
        for i in range(5):
            tv1.y -= 8
            tv2.y += 8
            tv3.y -= 8
            tv4.y += 8
            time.sleep(0.3)

    @classmethod
    def tvShoot(cls, tv1, tv2, tv3, tv4):
        for i in range(25):
            newbumb1 = Bullt.EmemiesBumb(tv1.x, tv1.y)
            newbumb2 = Bullt.EmemiesBumb(tv2.x, tv2.y)
            newbumb1.image = Event.Game.bulluten[10]
            newbumb2.image = Event.Game.bulluten[10]
            newbumb1.speed = 19
            newbumb2.speed = 19
            newbumb3 = Bullt.EmemiesBumb(tv3.x, tv3.y)
            newbumb4 = Bullt.EmemiesBumb(tv4.x, tv4.y)
            newbumb3.image = Event.Game.bulluten[10]
            newbumb4.image = Event.Game.bulluten[10]
            newbumb3.speed = 19
            newbumb4.speed = 19
            newbumb1.rect = newbumb1.image.get_rect()
            newbumb1.rect.left = newbumb1.x
            newbumb1.rect.top = newbumb1.y
            newbumb2.rect = newbumb2.image.get_rect()
            newbumb2.rect.left = newbumb2.x
            newbumb2.rect.top = newbumb2.y
            newbumb3.rect = newbumb3.image.get_rect()
            newbumb3.rect.left = newbumb3.x
            newbumb3.rect.top = newbumb3.y
            newbumb4.rect = newbumb4.image.get_rect()
            newbumb4.rect.left = newbumb4.x
            newbumb4.rect.top = newbumb4.y
            Event.Game.allenbumbs.append(newbumb1)
            Event.Game.allenbumbs.append(newbumb2)
            Event.Game.allenbumbs.append(newbumb3)
            Event.Game.allenbumbs.append(newbumb4)
            time.sleep(0.1)

    @classmethod
    def sideShoot(cls):
        new1 = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
        new2 = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y + 40)
        new3 = Bullt.BossBumb(Event.Game.boss.x, Event.Game.wateremoji.y + 20)
        new4 = Bullt.BossBumb(Event.Game.boss.x, Event.Game.wateremoji.y)
        new1.image = pygame.image.load('image/tv.png')
        new2.image = pygame.image.load('image/tv.png')
        new3.image = pygame.image.load('image/tv.png')
        new4.image = pygame.image.load('image/tv.png')
        new1.canDelete = False
        new2.canDelete = False
        new3.canDelete = False
        new4.canDelete = False
        new1.hurt, new2.hurt, new3.hurt, new4.hurt = 0, 0, 0, 0
        new1.canMove = False
        new2.canMove = False
        new3.canMove = False
        new4.canMove = False
        new1.banRemove = True
        new2.banRemove = True
        new3.banRemove = True
        new4.banRemove = True
        Event.Game.allenbumbs.append(new1)
        Event.Game.allenbumbs.append(new2)
        Event.Game.allenbumbs.append(new3)
        Event.Game.allenbumbs.append(new4)
        Event.Game.boss.canShoot = False
        th = threading.Thread(target=cls.sideMove, args=(new1, new2, new3, new4))
        th.daemon = True
        th.start()
        time.sleep(2)
        th = threading.Thread(target=cls.tvShoot, args=(new1, new2, new3, new4))
        th.daemon = True
        th.start()
        time.sleep(2.5)
        Event.Game.allenbumbs.remove(new1)
        Event.Game.allenbumbs.remove(new2)
        Event.Game.allenbumbs.remove(new3)
        Event.Game.allenbumbs.remove(new4)
        Event.Game.boss.canShoot = True

    @classmethod
    def removeUFO(cls, newe):
        while newe.y <= main.WINDOWHEIGHT:
            if newe not in Event.Game.g_enemies:
                return
            time.sleep(3)
        try:
            Event.Game.g_enemies.remove(newe)
        except ValueError:
            pass

    @classmethod
    def summonUFO(cls):
        for i in range(12):
            newe = OEmoji.Enemy()
            newe.canChangeMove = False
            newe.direction = 'down'
            newe.y = -40
            newe.x = random.randint(300, 400)
            newe.rint = 8
            newe.image = pygame.image.load('image/alien.png')
            newe.live = 40 * Event.Game.bossdeathtimes
            newe.maxlive = 40 * Event.Game.bossdeathtimes
            Event.Game.g_enemies.append(newe)
            th = threading.Thread(target=cls.removeUFO, args=(newe,))
            th.daemon = True
            th.start()
            time.sleep(0.4)

    @classmethod
    def move(cls):
        try:
            while Event.Game.haveBoss and Event.Game.boss.bossrint == 4:
                cls.frame.Move(Event.Game.rx + 640, 0)
                time.sleep(0.331)
                cls.frame.Move(Event.Game.rx - 220, 0)
                time.sleep(0.331)
        except RuntimeError:
            pass

    @classmethod
    def moveFrameForth(cls):
        try:
            while (Event.Game.haveBoss and Event.Game.boss.bossrint == 4):
                Move.moveWin(Event.Game.rx, Event.Game.ry - 10)
                time.sleep(0.1655)
                Move.moveWin(Event.Game.rx - 10, Event.Game.ry - 10)
                time.sleep(0.1655)
                Move.moveWin(Event.Game.rx - 10, Event.Game.ry)
                time.sleep(0.1655)
                Move.moveWin(Event.Game.rx, Event.Game.ry)
                time.sleep(0.1655)
        except RuntimeError:
            pass

    @classmethod
    def framemove(cls):
        cls.frame = Frame.Frame('ATTENTION', (Event.Game.rx - 220, 0), (220, 230))
        panel1 = wx.Panel(cls.frame, -1, size=(200, 200))
        cls.frame.Show()
        image = wx.Image('image/attention.png', wx.BITMAP_TYPE_PNG)
        mypic = image.ConvertToBitmap()
        wx.StaticBitmap(panel1, -1, bitmap=mypic, pos=(0, 0))
        hwnd = pygame.display.get_wm_info()['window']
        win32gui.SetForegroundWindow(hwnd)
        cls.sin = random.random()
        cls.cos = random.random()
        th = threading.Thread(target=cls.move)
        th.daemon = True
        th.start()
        th2 = threading.Thread(target=cls.moveFrameForth)
        th2.daemon = True
        th2.start()
