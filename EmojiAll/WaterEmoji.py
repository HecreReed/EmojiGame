import main, pygame
from EmojiAll.Emoji import *
from Bullut.WaterBumb import *
from Statement.State import *


# 定义流汗黄豆
class WaterEmoji(Emoji):
    def __init__(self):
        Emoji.__init__(self)
        self.imagesourance = 'image/wateremoji.png'
        self.image = pygame.image.load(self.imagesourance)
        self.size = 40
        self.rect = self.image.get_rect()
        self.x = 80
        self.y = 220  # 记得没错的话，点应该在左上角而不是在中心捏
        self.type = main.Friend
        self.statement = State.NORMAL
        self.maxlive = 20
        self.live = 20
        self.grade = 1
        self.hurt = random.randint(8, 12)
        self.canShoot = True

    def move(self, key):
        if key == 'up' and self.y > 0:
            self.y -= 5
        elif key == 'down' and self.y < main.WINDOWHEIGHT - 40:
            self.y += 5
        elif key == 'right' and self.x < main.WINDOWWIDTH - 40:
            self.x += 5
        elif key == 'left' and self.x > 0:
            self.x -= 5
        elif key == 'right-up' and self.x < main.WINDOWWIDTH - 40 and self.y > 0:
            self.y -= 5
            self.x += 5
        elif key == 'left-up' and self.x > 0 and self.y > 0:
            self.y -= 5
            self.x -= 5
        elif key == 'right-down' and self.x < main.WINDOWWIDTH - 40 and self.y < main.WINDOWHEIGHT - 40:
            self.x += 5
            self.y += 5
        elif key == 'left-down' and self.x > 0 and self.y < main.WINDOWHEIGHT - 40:
            self.x -= 5
            self.y += 5

    def normalshoot(self):
        if (time.time() - self.lasttime > self.sleepbumbtime):
            self.allbumb.append(
                WaterBumb(self.x, self.y + 20, self.hurt + random.randint(2, 4)))  # y加20是因为图片均为40*40像素，确保子弹是由中间发射出来
            self.lasttime = time.time()  # 处理时间间隔

    def doubleshoot(self):
        if (time.time() - self.lasttime > self.sleepbumbtime):
            self.allbumb.append(WaterBumb(self.x, self.y + 35, self.hurt + random.randint(2, 4)))
            self.allbumb.append(WaterBumb(self.x, self.y + 5, self.hurt + random.randint(2, 4)))
            self.lasttime = time.time()

    def twinbleshoot(self):
        if (time.time() - self.lasttime > self.sleepbumbtime):
            self.allbumb.append(WaterBumb(self.x, self.y + 45, self.hurt + random.randint(2, 4)))
            self.allbumb.append(WaterBumb(self.x, self.y + 20, self.hurt + random.randint(2, 4)))
            self.allbumb.append(WaterBumb(self.x, self.y - 5, self.hurt + random.randint(2, 4)))
            self.lasttime = time.time()

    def finalshoot(self):
        if (time.time() - self.lasttime > self.sleepbumbtime):
            self.allbumb.append(WaterBumb(self.x, self.y + 50, self.hurt + random.randint(2, 4)))
            self.allbumb.append(WaterBumb(self.x, self.y + 25, self.hurt + random.randint(2, 4)))
            self.allbumb.append(WaterBumb(self.x, self.y, self.hurt + random.randint(2, 4)))
            self.allbumb.append(WaterBumb(self.x, self.y - 25, self.hurt + random.randint(2, 4)))
            self.lasttime = time.time()

    def shoot(self):
        if self.canShoot:
            if self.statement == State.NORMAL:
                self.normalshoot()
            elif self.statement == State.DOUBLE:
                self.doubleshoot()
            elif self.statement == State.TWINBLE:
                self.twinbleshoot()
            elif self.statement == State.FINAL:
                self.finalshoot()

    def upgrading(self):
        if self.grade > 4:
            self.grade = 4
        elif self.grade == 2:
            self.statement = State.DOUBLE
        elif self.grade == 3:
            self.statement = State.TWINBLE
        elif self.grade == 4:
            self.statement = State.FINAL
