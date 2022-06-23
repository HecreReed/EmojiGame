import random

import EmojiAll.Ememies, time, pygame, Skills.Skills
from Event import *
from Bullut.BossBumb import *
from Bullut.EnemiesBumb import *


class BossEmemy(EmojiAll.Ememies.Enemy):
    def __init__(self):
        EmojiAll.Ememies.Enemy.__init__(self)
        self.live = 1200 * Game.wateremoji.grade + (Game.bossdeathtimes - 1) * 1500
        self.maxlive = 1200 * Game.wateremoji.grade + (Game.bossdeathtimes - 1) * 1500
        self.isboss = True
        self.rint = 0
        self.bossrint = random.randint(1, 5)
        self.image = pygame.image.load('image/bossenemy-' + str(self.bossrint) + '.png')
        self.rect = self.image.get_rect()
        self.imagesize = 80
        self.speed = 2
        self.sleepbumbtime = 0.6
        if self.bossrint == 2:
            self.x = random.randint(400, 550)
            self.y = -80
            self.direction = 'down'
            self.sleepbumbtime = 5
            self.speed = 4
        if self.bossrint == 3:
            self.sleepbumbtime = 1.5
        if self.bossrint == 4 or self.bossrint == 5:
            self.sleepbumbtime = 1.8
            self.x = random.randint(300, 400)
        self.canshoot = True
        self.canmove = True
        self.lastnormaltime = 0

    def thshoot(self):
        e1 = EmemiesBumb(self.x, self.y)
        e1.image = Event.Game.bulluten[4]
        e1.rect = e1.image.get_rect()
        e1.rect.left = e1.x
        e1.rect.top = e1.y
        Game.allenbumbs.append(e1)
        Game.allenbumbs.append(BossBumb(self.x, self.y))
        time.sleep(0.3)
        e2 = EmemiesBumb(self.x, self.y)
        e2.image = Event.Game.bulluten[4]
        e2.rect = e1.image.get_rect()
        e2.rect.left = e1.x
        e2.rect.top = e1.y
        Game.allenbumbs.append(e2)
        Game.allenbumbs.append(BossBumb(self.x, self.y))
        time.sleep(0.3)

    def doubleshoot(self):
        e1 = BossBumb(self.x, self.y)
        e1.image = Event.Game.bulluten[11]
        e1.canReturn = True
        e1.rect = e1.image.get_rect()
        e1.rect.left = e1.x
        e1.rect.top = e1.y
        Game.allenbumbs.append(e1)
        time.sleep(0.2)
        e1 = BossBumb(self.x, self.y)
        e1.image = Event.Game.bulluten[11]
        e1.canReturn = True
        e1.rect = e1.image.get_rect()
        e1.rect.left = e1.x
        e1.rect.top = e1.y
        Game.allenbumbs.append(e1)

    def shoot(self):
        if time.time() - self.lastnormaltime > 1 and self.canshoot:
            if self.bossrint == 2:
                self.lastnormaltime = time.time()
                newbumb = BossBumb(self.x, self.y)
                newbumb.image = Event.Game.bulluten[6]
                newbumb.rect = newbumb.image.get_rect()
                newbumb.rect.left = newbumb.x
                newbumb.rect.top = newbumb.y
                newbumb.canReturn = True
                Game.allenbumbs.append(newbumb)
        if (time.time() - self.lasttime > self.sleepbumbtime) and self.canshoot:
            self.lasttime = time.time()
            if self.bossrint == 5:
                th = threading.Thread(target=self.doubleshoot)
                th.daemon = True
                th.start()
            elif self.bossrint != 3:
                newbumb = BossBumb(self.x, self.y)
                if self.bossrint == 4:
                    newbumb.image = Event.Game.bulluten[10]
                if self.bossrint == 2:
                    newbumb.image = Event.Game.bulluten[2]
                    newbumb.speed = 8
                    newbumb.get = True
                newbumb.rect = newbumb.image.get_rect()
                newbumb.rect.left = newbumb.x
                newbumb.rect.top = newbumb.y
                Game.allenbumbs.append(newbumb)
            else:
                t1 = threading.Thread(target=self.thshoot)
                t1.daemon = True
                t1.start()

    def move(self):
        if self.canmove is True:
            if self.direction == 'left':
                if self.x >= 6 / 8 * main.WINDOWWIDTH:  # 限制在3/4宽度的右边移动
                    self.x -= self.speed
            elif self.direction == 'right':
                if self.x <= main.WINDOWWIDTH - self.imagesize:
                    self.x += self.speed
            elif self.direction == 'up':
                if self.y >= 0:
                    self.y -= self.speed
            elif self.direction == 'down':
                if self.y <= main.WINDOWHEIGHT - self.imagesize:  # 同上，防止敌军emoji飞出屏幕
                    self.y += self.speed

    def useSkills(self):
        if self.bossrint == 1:
            Skills.Skills.Skills.FirstBossSkill()
        elif self.bossrint == 2:
            Skills.Skills.Skills.SecondBossSkill()
        elif self.bossrint == 3:
            Skills.Skills.Skills.ThirdBossSkill()
        elif self.bossrint == 4:
            Skills.Skills.Skills.ForthBossSkill()
        elif self.bossrint == 5:
            Skills.Skills.Skills.FifthBossSkill()
