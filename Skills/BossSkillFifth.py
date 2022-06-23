import time, pygame, win32gui, random, main, Event, Move, threading, Bullt, math, OEmoji

import wx

import Frame


class BossSkillFifth:
    @classmethod
    def moveFrame(cls):
        try:
            while (Event.Game.haveBoss and Event.Game.boss.bossrint == 5):
                Move.moveWin(Event.Game.rx, Event.Game.ry)
                time.sleep(0.06857)
                Move.moveWin(Event.Game.rx, Event.Game.ry - 10)
                time.sleep(0.06857)
                Move.moveWin(Event.Game.rx, Event.Game.ry - 20)
                time.sleep(0.06857)
                Move.moveWin(Event.Game.rx, Event.Game.ry - 10)
                time.sleep(0.06857)
                Move.moveWin(Event.Game.rx, Event.Game.ry)
                time.sleep(0.06857)
        except RuntimeError:
            pass

    @classmethod
    def modifyTNT(cls, tnt):
        time.sleep(1.5)
        tnt.image = Event.Game.bulluten[14]
        time.sleep(1)
        while Event.Game.istimestoptime:
            time.sleep(1)
        newbumb = Bullt.BossBumb(tnt.x, tnt.y)
        newbumb.canDelete = False
        newbumb.canMove = False
        newbumb.image = Event.Game.bulluten[13]
        newbumb.rect = newbumb.image.get_rect()
        newbumb.rect.left = newbumb.x
        newbumb.rect.top = newbumb.y
        Event.Game.allenbumbs.append(newbumb)
        try:
            Event.Game.allenbumbs.remove(tnt)
        except ValueError:
            pass
        index = 240
        newbumb.image.set_alpha(index)
        for i in range(10):
            while Event.Game.istimestoptime:
                time.sleep(1)
            newbumb.size += 8
            newbumb.x -= 4
            newbumb.y -= 4
            newbumb.image = pygame.transform.smoothscale(newbumb.image,
                                                         (newbumb.size, newbumb.size))
            newbumb.rect = newbumb.image.get_rect()
            newbumb.rect.left = newbumb.x
            newbumb.rect.top = newbumb.y  # 更新碰撞体积
            newbumb.image.set_alpha(index)
            index -= 20
            time.sleep(0.1)
        try:
            Event.Game.allenbumbs.remove(newbumb)
        except ValueError:
            pass

    @classmethod
    def dragAttack(cls, newbumb):
        art = math.atan(newbumb.tan)
        artt = math.atan(newbumb.tan)
        sample = newbumb.sample
        randoms = random.random()
        while -20 <= newbumb.x < main.WINDOWWIDTH and -20 <= newbumb.y <= main.WINDOWHEIGHT and not newbumb.blow:
            while Event.Game.istimestoptime:
                time.sleep(1)
            if randoms < 0.5:
                art -= math.pi / 5
            else:
                art += math.pi / 5
            newbumb.tan = math.tan(art)
            if sample == 0:
                if newbumb.direction == 'left':
                    newbumb.x -= newbumb.speed
            elif newbumb.direction == 'right':
                newbumb.x += math.sqrt(newbumb.speed * 10 / (1 + math.tan(artt) ** 2))
                newbumb.y += math.sqrt(newbumb.speed * 10 / (1 + math.tan(artt) ** 2)) * math.tan(artt)
            elif newbumb.direction == 'left' or (newbumb.direction == 'right' and newbumb.sample == -1):
                newbumb.x -= math.sqrt(newbumb.speed * 10 / (1 + math.tan(artt) ** 2))
                newbumb.y -= math.sqrt(newbumb.speed * 10 / (1 + math.tan(artt) ** 2)) * math.tan(artt)
            newbumb.rect.left = newbumb.x
            newbumb.rect.top = newbumb.y
            time.sleep(0.1)
        if not (-20 <= newbumb.x < main.WINDOWWIDTH and -20 <= newbumb.y <= main.WINDOWHEIGHT):
            try:
                Event.Game.allenbumbs.remove(newbumb)
            except ValueError:
                pass

    @classmethod
    def jumpShoot(cls):
        for i in range(10):
            if Event.Game.haveBoss:
                while Event.Game.istimestoptime:
                    time.sleep(1)
                newbumb = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
                newbumb.image = Event.Game.bulluten[5]
                newbumb.rect = newbumb.image.get_rect()
                newbumb.rect.left = newbumb.x
                newbumb.rect.top = newbumb.y
                newbumb.size = 23
                newbumb.banRemove = True
                newbumb.canReturn = True
                Event.Game.allenbumbs.append(newbumb)
                th = threading.Thread(target=cls.dragAttack, args=(newbumb,))
                th.daemon = True
                th.start()
                time.sleep(0.2)
    @classmethod
    def healMode(cls):
        Event.Game.healtime = True
        Event.Game.boss.image = pygame.image.load('image/lightboss1.png')
        time.sleep(3)
        Event.Game.healtime = False
        Event.Game.boss.image = pygame.image.load('image/bossenemy-5.png')
    @classmethod
    def throwTNT(cls):
        for i in range(5):
            if Event.Game.haveBoss:
                while Event.Game.istimestoptime:
                    time.sleep(1)
                tnt = Bullt.BossBumb(Event.Game.boss.x, Event.Game.boss.y)
                tnt.image = Event.Game.bulluten[12]
                tnt.rect = tnt.image.get_rect()
                tnt.rect.left = tnt.x
                tnt.rect.top = tnt.y
                tnt.speed = 7
                Event.Game.allenbumbs.append(tnt)
                th = threading.Thread(target=cls.modifyTNT, args=(tnt,))
                th.daemon = True
                th.start()
                time.sleep(0.8)
