import time, pygame, win32gui, random, main, Event, Move, threading, Bullt, math, OEmoji


class BossSkillFirst:
    lastmovetime = 0
    movedirection = 'right'
    thistime = 0
    teleporttime = 0
    thisteleport = object

    @classmethod
    def haveTeleport(cls):  # 有传送门时执行
        while (Event.Game.haveTeleport):
            newe = OEmoji.SummonEnemies()
            newe.x = cls.thisteleport.x
            newe.y = cls.thisteleport.y
            if newe.rint == -1:
                newe.live = 100 * Event.Game.bossdeathtimes
                newe.maxlive = 100 * Event.Game.bossdeathtimes
            elif newe.rint == -2:
                newe.live = 130 * Event.Game.bossdeathtimes
                newe.maxlive = 130 * Event.Game.bossdeathtimes
            Event.Game.g_enemies.append(newe)
            time.sleep(random.randint(3, 9))

    @classmethod  # 传送门技能
    def summonTeleport(cls):
        if time.time() - cls.teleporttime >= 15 and time.time() - Event.Game.teleportDeathtime >= 8 + 8 * random.random() and Event.Game.haveTeleport is False:
            cls.thisteleport = OEmoji.Teleport()
            cls.thisteleport.x = Event.Game.boss.x - 120
            cls.thisteleport.y = Event.Game.boss.y
            Event.Game.g_enemies.append(cls.thisteleport)
            t1 = threading.Thread(target=cls.haveTeleport)
            t1.daemon = True
            t1.start()
        else:
            newthread = threading.Thread(target=cls.starShoot)
            newthread.daemon = True
            newthread.start()

    @classmethod
    def shootaside(cls):
        for i in range(35):
            if Event.Game.haveBoss is False:
                break
            while Event.Game.istimestoptime:
                time.sleep(1)
            newbumb1 = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
            newbumb2 = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
            newbumb1.tan = math.tan(math.atan(newbumb1.tan) + math.pi / 10)
            newbumb2.tan = math.tan(math.atan(newbumb1.tan) - math.pi / 10)
            newbumb1.image = Event.Game.bulluten[1]
            newbumb2.image = Event.Game.bulluten[1]
            newbumb1.rect = newbumb1.image.get_rect()
            newbumb1.rect.left = newbumb1.x
            newbumb1.rect.top = newbumb1.y
            newbumb2.rect = newbumb2.image.get_rect()
            newbumb2.rect.left = newbumb2.x
            newbumb2.rect.top = newbumb2.y
            Event.Game.allenbumbs.append(newbumb1)
            Event.Game.allenbumbs.append(newbumb2)
            time.sleep(0.2)

    @classmethod
    def sandShoot(cls):  # 散射技能
        settime = 1
        for i in range(random.randint(3, 5)):
            while Event.Game.istimestoptime:
                time.sleep(1)
            cls.setSand(settime)
            if Event.Game.haveBoss is False:
                break
            time.sleep(0.5)
            settime += 1

    @classmethod
    def setSand(cls, times):  # time为第几波
        rive = math.pi / 10
        artan = 0
        index = 0
        timek = 0
        for i in range(9 + times * 2):
            newbumb = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
            newbumb.speed = 12
            if i != 0:
                if index % 2 != 0:
                    newbumb.tan = math.tan(artan + timek * rive)
                else:
                    newbumb.tan = math.tan(artan - timek * rive)
                if index % 2 == 0:
                    timek += 1
            else:
                artan = math.atan(newbumb.tan)
            newbumb.image = Event.Game.bulluten[1]
            newbumb.rect = newbumb.image.get_rect()
            newbumb.rect.left = newbumb.x
            newbumb.rect.top = newbumb.y
            Event.Game.allenbumbs.append(newbumb)
            index += 1

    @classmethod  # 窗口移动的技能
    def melySkill(cls):
        if time.time() - cls.thistime >= 0.001:
            cls.thistime = time.time()
            cls.moveWindows()

    @classmethod
    def moveWindows(cls):
        hwnd = pygame.display.get_wm_info()['window']
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        if time.time() - cls.lastmovetime >= 2:
            randoms = random.random()
            if randoms > 0 and randoms <= 0.25:
                cls.movedirection = 'right'
            elif randoms > 0.25 and randoms <= 0.5:
                cls.movedirection = 'left'
            elif randoms > 0.5 and randoms <= 0.75:
                cls.movedirection = 'up'
            elif randoms > 0.75 and randoms < 1:
                cls.movedirection = 'down'
        if cls.movedirection == 'right':
            if x < Event.Game.rwidth - main.WINDOWWIDTH:
                Move.moveWin(x + random.randint(1, 3), y)
        elif cls.movedirection == 'left':
            if x > 0:
                Move.moveWin(x - random.randint(1, 3), y)
        elif cls.movedirection == 'down':
            if y < Event.Game.rheight - main.WINDOWHEIGHT:
                Move.moveWin(x, y + random.randint(1, 3))
        elif cls.movedirection == 'up':
            if y > 0:
                Move.moveWin(x, y - random.randint(1, 3))

    @classmethod
    def starChange(cls, newbumb):
        index = 0
        while -80 <= newbumb.x <= 640 and -80 <= newbumb.y <= 480:
            while Event.Game.istimestoptime:
                time.sleep(1)
            newbumb.image1 = pygame.transform.rotate(newbumb.image, 20 + index)
            time.sleep(0.1)
            newbumb.rect = newbumb.image1.get_rect()
            newbumb.rect.left = newbumb.x
            newbumb.rect.top = newbumb.y  # 更新碰撞体积
            index += 20

    @classmethod
    def starShoot(cls):
        for i in range(5):
            if Event.Game.haveBoss:
                while Event.Game.istimestoptime:
                    time.sleep(1)
                newbumb = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
                newbumb.size = 80
                newbumb.speed = 20
                newbumb.image = Event.Game.bulluten[9]
                newbumb.rect = newbumb.image.get_rect()
                newbumb.rect.left = newbumb.x
                newbumb.rect.top = newbumb.y
                newbumb.willRotate = True
                newbumb.canReturn = True
                newbumb.canDelete = False
                Event.Game.allenbumbs.append(newbumb)
                th = threading.Thread(target=cls.starChange, args=(newbumb,))
                th.daemon = True
                th.start()
                time.sleep(1.2)
