import time, pygame, win32gui, random, main, Event, Move, threading, Bullt, math, OEmoji, Frame, main, wx


class BossSkillSecond:
    frame1 = object
    frame2 = object
    newbumb = object
    hasAttr = False
    newattr = object
    canmadeinheaven = True

    @classmethod
    def madeinheaven(cls):
        if cls.canmadeinheaven:
            cls.canmadeinheaven = False
            Event.Game.heaven.play()
            Event.Game.boss.movetime = 0.01
            Event.Game.boss.speed = 30
            Event.Game.boss.sleepbumbtime = 1
            Event.Game.boss.image = pygame.image.load('image/madeinheaven.png')
            Event.Game.boss.canbeshoot = False
            time.sleep(8)
            Event.Game.boss.movetime = 0.12
            Event.Game.boss.speed = 4
            Event.Game.boss.sleepbumbtime = 5
            Event.Game.boss.image = pygame.image.load('image/bossenemy-2.png')
            Event.Game.boss.canbeshoot = True
        cls.canmadeinheaven = True

    @classmethod
    def attractMove(cls):
        while cls.hasAttr:
            cls.newattr.x += 5
            cls.newattr.y += 5
            time.sleep(0.1)
            cls.newattr.x -= 5
            cls.newattr.y -= 5
            time.sleep(0.1)
            cls.newattr.x += 5
            cls.newattr.y -= 5
            time.sleep(0.1)
            cls.newattr.x -= 5
            cls.newattr.y += 5
            time.sleep(0.1)

    @classmethod
    def attract(cls):
        while cls.hasAttr:
            while Event.Game.istimestoptime:
                time.sleep(1)
            ex = Event.Game.wateremoji.x
            ey = Event.Game.wateremoji.y
            if cls.newattr.x != ex:
                tan = (cls.newattr.y - ey) / (cls.newattr.x - ex)
                if cls.newattr.x > ex:
                    Event.Game.wateremoji.x += math.sqrt(125 / (1 + tan ** 2))
                    Event.Game.wateremoji.y += math.sqrt(125 / (1 + tan ** 2)) * tan
                else:
                    Event.Game.wateremoji.x -= math.sqrt(125 / (1 + tan ** 2))
                    Event.Game.wateremoji.y -= math.sqrt(125 / (1 + tan ** 2)) * tan
            else:
                if cls.newattr.y > ey:
                    Event.Game.wateremoji.y -= 125
                else:
                    Event.Game.wateremoji.y += 125
            time.sleep(0.05)

    @classmethod
    def closeAttract(cls):
        time.sleep(4)
        cls.hasAttr = False

    @classmethod
    def useAttract(cls):
        if not cls.hasAttr and cls.canmadeinheaven:
            cls.newattr = Bullt.BossBumb(Event.Game.boss.x - 50, Event.Game.boss.y)
            cls.newattr.image = pygame.image.load('image/attract.png')
            cls.newattr.rect = cls.newattr.image.get_rect()
            cls.newattr.rect.left = cls.newattr.x
            cls.newattr.rect.top = cls.newattr.y
            cls.newattr.canMove = False
            cls.hasAttr = True
            t1 = threading.Thread(target=cls.attractMove)
            t1.daemon = True
            t1.start()
            t2 = threading.Thread(target=cls.attract)
            t2.daemon = True
            t2.start()
            t3 = threading.Thread(target=cls.closeAttract)
            t3.daemon = True
            t3.start()

    @classmethod
    def enlargeLove(cls):
        while Event.Game.haveLovebumb:
            if cls.newbumb.size <= 120:
                cls.newbumb.size += 10
                cls.newbumb.image = pygame.transform.smoothscale(cls.newbumb.image,
                                                                 (cls.newbumb.size, cls.newbumb.size))
                cls.newbumb.rect = cls.newbumb.image.get_rect()
                cls.newbumb.rect.left = cls.newbumb.x
                cls.newbumb.rect.top = cls.newbumb.y  # 更新碰撞体积
            time.sleep(0.1)

    @classmethod
    def generateLove(cls):
        cls.newbumb = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
        cls.newbumb.image = Event.Game.bulluten[3]
        cls.newbumb.size = 25
        cls.newbumb.canRemove = False  # 不能被任意门消除
        cls.newbumb.get = False  # 不追踪
        cls.newbumb.sample = 0
        cls.newbumb.canDelete = False
        Event.Game.loveBumb = cls.newbumb
        Event.Game.allenbumbs.append(cls.newbumb)
        Event.Game.haveLovebumb = True
        t1 = threading.Thread(target=cls.enlargeLove())
        t1.daemon = True
        t1.start()

    @classmethod
    def createPrevent(cls):
        pr1 = OEmoji.Prevent(200, 0)
        pr2 = OEmoji.Prevent(200, 360)

    @classmethod
    def moveFrame(cls):
        try:
            while Event.Game.haveBoss:
                cls.frame1.Move(Event.Game.rx - 300, Event.Game.ry - 10)
                cls.frame2.Move(Event.Game.rx + 740, Event.Game.ry - 10)
                Move.moveWin(Event.Game.rx, Event.Game.ry - 5)
                time.sleep(0.0745)
                cls.frame1.Move(Event.Game.rx - 300, Event.Game.ry - 25)
                cls.frame2.Move(Event.Game.rx + 740, Event.Game.ry - 25)
                Move.moveWin(Event.Game.rx, Event.Game.ry - 10)
                time.sleep(0.0745)
                cls.frame1.Move(Event.Game.rx - 300, Event.Game.ry - 38)
                cls.frame2.Move(Event.Game.rx + 740, Event.Game.ry - 38)
                Move.moveWin(Event.Game.rx, Event.Game.ry - 15)
                time.sleep(0.0745)
                cls.frame1.Move(Event.Game.rx - 300, Event.Game.ry - 25)
                cls.frame2.Move(Event.Game.rx + 740, Event.Game.ry - 25)
                Move.moveWin(Event.Game.rx, Event.Game.ry - 10)
                time.sleep(0.0745)
                cls.frame1.Move(Event.Game.rx - 300, Event.Game.ry - 10)
                cls.frame2.Move(Event.Game.rx + 740, Event.Game.ry - 10)
                Move.moveWin(Event.Game.rx, Event.Game.ry - 5)
                time.sleep(0.0745)
                cls.frame1.Move(Event.Game.rx - 300, Event.Game.ry)
                cls.frame2.Move(Event.Game.rx + 740, Event.Game.ry)
                Move.moveWin(Event.Game.rx, Event.Game.ry)
                time.sleep(0.0745)
            cls.frame1.Hide()
            cls.frame2.Hide()
        except RuntimeError:
            pass

    @classmethod
    def createFrame(cls):
        cls.frame1 = Frame.Frame('禁忌的边界线', (Event.Game.rx - 200, Event.Game.ry), (220, 220))
        cls.frame2 = Frame.Frame('禁忌的边界线', (Event.Game.rx + 740, Event.Game.ry), (220, 220))
        panel1 = wx.Panel(cls.frame1, -1, size=(200, 200))
        panel2 = wx.Panel(cls.frame2, -1, size=(200, 200))
        cls.frame1.Show()
        cls.frame2.Show()
        image = wx.Image('image/heart.png', wx.BITMAP_TYPE_PNG)
        mypic = image.ConvertToBitmap()
        wx.StaticBitmap(panel1, -1, bitmap=mypic, pos=(0, 0))
        wx.StaticBitmap(panel2, -1, bitmap=mypic, pos=(0, 0))
        hwnd = pygame.display.get_wm_info()['window']
        win32gui.SetForegroundWindow(hwnd)
        t1 = threading.Thread(target=cls.moveFrame)
        t1.daemon = True
        t1.start()
