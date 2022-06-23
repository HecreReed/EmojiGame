import threading

import pygame, time, random, math, Event, main


class Supply(pygame.sprite.Sprite, object):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.image = pygame.image.load('image/supply-' + str(self.type) + '.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 105
        self.createtime = time.time()
        self.size = 20
        self.sample = 1
        if random.random() < 0.5:
            self.tan = -2 * random.random()
        else:
            self.tan = 2 * random.random()

    def move(self, screen):  # 补给的移动
        if self.sample == 1:
            self.x -= math.sqrt(self.speed / (1 + self.tan ** 2))
            self.y -= math.sqrt(self.speed / (1 + self.tan ** 2)) * self.tan
        elif self.sample == -1:
            self.x += math.sqrt(self.speed / (1 + self.tan ** 2))
            self.y += math.sqrt(self.speed / (1 + self.tan ** 2)) * self.tan
        elif self.sample == 0:
            if self.ex - self.x > 0:
                self.x += self.speed
            elif self.ex - self.x < 0:
                self.x -= self.speed
        self.rect.left = self.x
        self.rect.top = self.y
        screen.blit(self.image, (self.x, self.y))
        t1 = threading.Thread(target=self.calu)
        t1.daemon = True
        t1.start()

    def calu(self):
        self.ex = Event.Game.wateremoji.x
        self.ey = Event.Game.wateremoji.y
        if self.ex - self.x != 0:
            self.tan = (self.ey - self.y) / (self.ex - self.x)
        else:
            self.tan = 0
            self.sample = 0
        if self.ex - self.x < 0:
            self.sample = 1
        elif self.ex - self.x > 0:
            self.sample = -1

    def attract(self):  # 补给被吸收
        if self.type == 1:
            if Event.Game.wateremoji.live < Event.Game.wateremoji.maxlive:
                Event.Game.wateremoji.live += int(8 + 4 * random.random())
                if Event.Game.wateremoji.live > Event.Game.wateremoji.maxlive:
                    Event.Game.wateremoji.live = Event.Game.wateremoji.maxlive
        elif self.type == 2:
            Event.Game.wateremoji.grade += 1
            Event.Game.wateremoji.upgrading()
        elif self.type == 3:
            Event.Game.wateremoji.sleepbumbtime -= 0.1
            if Event.Game.wateremoji.sleepbumbtime <= 0.125:
                Event.Game.wateremoji.sleepbumbtime = 0.125
        elif self.type == 4:
            Event.Game.money += 10
        elif self.type == 5:
            Event.Game.money += 50
        elif self.type == 6:
            Event.Game.money += 400
        elif self.type == 0:
            Event.Game.wateremoji.hurt += 2  # 力量药水
        elif self.type == 7:
            if Event.Game.wateremoji.maxlive <= 40:
                Event.Game.wateremoji.maxlive += 4
            else:
                Event.Game.wateremoji.maxlive = 40
        elif self.type == 8:
            Event.Game.power += random.randint(1, 3)
            if Event.Game.power > 100:
                Event.Game.power = 100
