import pygame, Bullt, OEmoji, sys, time, random, main, AllSupply, Skill, Move, threading


class Game:
    wateremoji = object
    g_enemies = []
    score = 0
    latesttime = 0
    allenbumbs = []
    allsupply = []
    haveBoss = False
    allprevent = []
    Aleph = object
    Bgm = []
    FPS = 60
    lastBoss = 0
    Death = object
    rx = 0
    ry = 0
    thistime = 0
    boss = object
    bosscreatetime = 0
    rwidth = 0
    rheight = 0
    bossdeathtimes = 1
    haveTeleport = False
    teleportDeathtime = 0
    maxEn = 0
    bgmnow = 1
    Boardline = object
    app = object
    money = 0
    haveLovebumb = False
    loveBumb = object
    heaven = object
    temp = object
    gold = False
    golden = object
    theworld = object
    screen = object
    istimestoptime = False
    gamepauseImage = object
    backgroundImage = object
    backgroundImage2 = object
    backgroundImage3 = object
    boss1, boss3, boss4, boss1r, boss3r, boss2r, boss4r, boss5, boss5r = object, object, object, object, object, object, object, object, object
    bulluten = []
    isok = False
    boss4bgm, boss5bgm = object, object
    healtime = False
    power = 0
    isBossTimestop = False
    special = object

    @classmethod
    def createWaterEmoji(cls):
        cls.wateremoji = OEmoji.WaterEmoji()

    @classmethod
    def createBoss(cls):
        newBoss = OEmoji.BossEmemy()
        cls.haveBoss = True
        cls.Bgm[Game.bgmnow].stop()
        for i in cls.g_enemies:
            if not i.isboss:
                th = threading.Thread(target=cls.removeNormal, args=(i,))
                th.daemon = True
                th.start()
        if newBoss.bossrint == 1:
            cls.Aleph.play(loops=True)
        elif newBoss.bossrint == 2:
            cls.Boardline.play(loops=True)
        elif newBoss.bossrint == 3:
            cls.temp.play(loops=True)
        elif newBoss.bossrint == 4:
            cls.boss4bgm.play(loops=True)
        elif newBoss.bossrint == 5:
            cls.boss5bgm.play(loops=True)
        cls.boss = newBoss
        if newBoss.bossrint == 4:
            Skill.BossSkillForth.framemove()
        if newBoss.bossrint == 5:
            th = threading.Thread(target=Skill.BossSkillFifth.moveFrame)
            th.daemon = True
            th.start()
        cls.g_enemies.append(newBoss)

    @classmethod
    def removeNormal(cls, em):
        index = 255
        for i in range(20):
            em.image.set_alpha(index)
            index -= 20
            time.sleep(0.1)
        try:
            cls.g_enemies.remove(em)
        except ValueError:
            pass

    @classmethod
    def bossUseSkill(cls):
        cls.boss.useSkills()
        if cls.haveBoss and cls.boss.bossrint == 2:
            try:
                if pygame.sprite.collide_mask(cls.allprevent[0], cls.wateremoji) or pygame.sprite.collide_mask(
                        cls.allprevent[1], cls.wateremoji):
                    cls.wateremoji.x = random.randint(0, 300)
                    cls.wateremoji.y = random.randint(0, 440)

            except ValueError:
                pass

    @classmethod
    def showPrevent(cls, screen):
        screen.blit(cls.allprevent[0].image, (cls.allprevent[0].x, cls.allprevent[0].y))
        screen.blit(cls.allprevent[1].image, (cls.allprevent[1].x, cls.allprevent[1].y))

    @classmethod
    def createEnemy(cls, boostspeed):
        newEnemy = OEmoji.Enemy(boostspeed)
        cls.g_enemies.append(newEnemy)  # 三种不同的地方emoji设置三种血量

    @classmethod
    def randommove(cls, i, chance):
        randoms = random.random()
        if randoms > 0 and randoms < chance and time.time() - i.cotime >= 0.5:
            i.cotime = time.time()
            i.direction = 'left'
        elif randoms >= chance and randoms < 2 * chance and time.time() - i.cotime >= 0.5:
            i.cotime = time.time()
            i.direction = 'right'
        elif randoms >= 2 * chance and randoms < 3 * chance and time.time() - i.cotime >= 0.5:
            i.cotime = time.time()
            i.direction = 'up'
        elif randoms >= 3 * chance and randoms <= 4 * chance and time.time() - i.cotime >= 0.5:
            i.cotime = time.time()
            i.direction = 'down'
        elif time.time() - i.cotime >= 0.5:
            i.cotime = time.time()
            i.direction = 'none'

    @classmethod
    def setDirection(cls):  # 敌人随机移动的方法
        for i in cls.g_enemies:
            i.intervaltime = time.time() - i.createtime
            if i.canChangeMove:
                if i.rint != 0:
                    if i.intervaltime < 1:
                        i.direction = 'left'
                    else:
                        cls.randommove(i, 0.2)
                else:
                    if i.intervaltime < 2.4:
                        if i.bossrint == 2:
                            i.direction = 'down'
                        else:
                            i.direction = 'left'
                    elif i.intervaltime >= i.movetime:
                        cls.randommove(i, 0.125)

    @classmethod
    def getEffect(cls):  # 获得效果
        for i in cls.allsupply:
            if pygame.sprite.collide_mask(i, cls.wateremoji):
                i.attract()
                cls.allsupply.remove(i)

    @classmethod
    def createSupply(cls, type, x, y):  # 生成补给物
        cls.allsupply.append(AllSupply.Supply(type, x, y))

    @classmethod
    def supplyMove(cls, screen):  # 补给物移动的方法
        for i in cls.allsupply:
            i.move(screen)
        for i in cls.allsupply:
            if time.time() - i.createtime >= 18 + 3 * random.random():
                cls.allsupply.remove(i)

    @classmethod
    def gameinit(cls):  # 初始化游戏
        cls.createWaterEmoji()

    @classmethod
    def getkey(cls, key):
        cls.wateremoji.move(key)

    @classmethod
    def draw(cls, screen):
        cls.setDirection()
        for i in cls.g_enemies[::]:
            i.draw(screen)
            if i.x > main.WINDOWWIDTH:
                cls.g_enemies.remove(i)

        cls.wateremoji.draw(screen)
        cls.wateremoji.rect.left = cls.wateremoji.x
        cls.wateremoji.rect.top = cls.wateremoji.y
        for i in cls.wateremoji.allbumb[::]:
            if i.x > 640:
                cls.wateremoji.allbumb.remove(i)

    @classmethod
    def updateLocation(cls):
        for i in cls.g_enemies:
            i.move()  # 敌人移动
            i.rect.left = i.x
            i.rect.top = i.y

    @classmethod
    def testfor(cls, bumb, value):
        try:
            if pygame.sprite.collide_mask(bumb, cls.allprevent[0]) or pygame.sprite.collide_mask(bumb,
                                                                                                 cls.allprevent[1]):
                try:
                    if value == 0:
                        cls.allenbumbs.remove(bumb)
                    elif value == 1:
                        cls.wateremoji.allbumb.remove(bumb)
                except ValueError:
                    pass
        except IndexError:
            pass

    @classmethod
    def showAttr(cls, screen):
        screen.blit(Skill.BossSkillSecond.newattr.image,
                    (Skill.BossSkillSecond.newattr.x, Skill.BossSkillSecond.newattr.y))

    @classmethod
    def enshoot(cls, screen):  # 敌人射击的方法
        for i in cls.g_enemies:
            i.shoot()
        for j in cls.allenbumbs:
            j.draw(screen)
        for j in cls.allenbumbs:  # 检测碰撞体积
            if cls.haveBoss is True and cls.boss.bossrint == 2 and j.canRemove is True:  # 要求能够被消除
                t1 = threading.Thread(target=cls.testfor(j, 0))
                t1.daemon = True
                t1.start()
            if pygame.sprite.collide_mask(j,
                                          cls.wateremoji) and time.time() - cls.latesttime >= 1 and not j.blow:  # 给定1s的无敌帧
                cls.latesttime = time.time()
                cls.wateremoji.live = int(cls.wateremoji.live - j.hurt)  # 自己扣血
                if j.canDelete:
                    cls.allenbumbs.remove(j)
                if cls.wateremoji.live <= 0:
                    cls.wateremoji.live = 0
                    Game.isok = True
            elif pygame.sprite.collide_mask(j,
                                            cls.wateremoji) and not time.time() - cls.latesttime >= 1 and j.canDelete:  # 无敌帧期间子弹碰到自己也要消失
                cls.allenbumbs.remove(j)
            if j.canReturn and j.x <= 0:
                j.x += j.speed
                j.tan = -j.tan
                j.sample = -j.sample
                j.direction = 'right'
            if j.canReturn and (j.y <= 0 or j.y >= main.WINDOWHEIGHT - j.size):
                j.tan = -j.tan
            if (
                    j.x <= 0 - j.size or j.x >= main.WINDOWWIDTH or j.y < 0 - j.size or j.y >= main.WINDOWHEIGHT) \
                    and not j.banRemove:
                if j == cls.loveBumb:  # 爱心炮弹
                    cls.loveBumb = object
                    cls.haveLovebumb = False
                cls.allenbumbs.remove(j)  # 超出屏幕删除对应子弹

    @classmethod
    def generateSupply(cls, chance, x, y):  # 随机概率生成随机补给物
        if random.random() < chance:
            cls.createSupply(random.randint(1, 3), x - 20, y)
        if chance == 1:  # 只有boss才会有100%掉落，所以这里是boss掉落物
            cls.createSupply(6, x - 20, y)
            cls.createSupply(6, x - 20, y)
            cls.createSupply(6, x - 20, y)
            cls.createSupply(0, x - 20, y)
            cls.createSupply(7, x - 20, y)
            return
        if random.random() < chance * 1.7:
            cls.createSupply(4, x - 20, y)
        elif random.random() < chance:
            cls.createSupply(5, x - 20, y)
        elif random.random() < chance * 0.3:
            cls.createSupply(6, x - 20, y)

    @classmethod
    def bossDeath(cls, boss):
        cls.score += cls.boss.maxlive
        cls.haveBoss = False
        if cls.boss.bossrint == 1:
            cls.Aleph.stop()
        elif cls.boss.bossrint == 2:
            cls.Boardline.stop()
            cls.allprevent.clear()
        elif cls.boss.bossrint == 3:
            cls.temp.stop()
        elif cls.boss.bossrint == 4:
            cls.boss4bgm.stop()
            Skill.BossSkillForth.frame.Hide()
        elif cls.boss.bossrint == 5:
            cls.boss5bgm.stop()
        cls.Death.play()
        cls.bgmnow = random.randint(0, 4)
        cls.Bgm[cls.bgmnow].play()
        cls.lastBoss = time.time()
        cls.bossdeathtimes += 1
        Move.moveWin(cls.rx, cls.ry)  # 还原坐标
        for k in range(random.randint(1, 5)):
            cls.generateSupply(1, boss.x, boss.y)

    @classmethod
    def emojiDeath(cls, emoji):
        cls.createSupply(8, emoji.x - 20, emoji.y)
        if emoji.rint == 1:
            cls.score += emoji.maxlive
            cls.generateSupply(0.2, emoji.x, emoji.y)
        elif emoji.rint == 2:
            cls.score += emoji.maxlive
            cls.generateSupply(0.3, emoji.x, emoji.y)
        elif emoji.rint >= 3:
            if emoji.rint == 8:
                return
            cls.score += emoji.maxlive
            cls.generateSupply(0.5, emoji.x, emoji.y)
        elif emoji.rint == 0.5:
            cls.score += emoji.maxlive
            cls.generateSupply(0.6, emoji.x, emoji.y)
            cls.teleportDeathtime = time.time()
            cls.haveTeleport = False
        elif emoji.rint == -1:
            cls.score += emoji.maxlive
            cls.generateSupply(0.2, emoji.x, emoji.y)
        elif emoji.rint == -2:
            cls.score += emoji.maxlive
            cls.generateSupply(0.2, emoji.x, emoji.y)

    @classmethod
    def drawBoss(cls):  # boss血条
        pygame.draw.rect(cls.screen, (0, 0, 0), (69, 9, 502, 22))
        pygame.draw.rect(cls.screen, (123, 123, 123), (70, 10, 500, 20))
        pygame.draw.rect(cls.screen, (255, 0, 0), (70, 10, int(500 * (cls.boss.live / cls.boss.maxlive)), 20))

    @classmethod
    def shoot(cls, screen):  # 流汗黄豆射击方法
        cls.wateremoji.shoot()
        for i in cls.wateremoji.allbumb[::]:  # 创建切片副本，防止出现ValueError错误
            i.draw(screen)
            for j in cls.g_enemies[::]:
                if pygame.sprite.collide_mask(i, j) and j.canbeshoot:
                    if j.rint == 0 and cls.healtime:
                        j.live = int(j.live + i.hurt)
                        if j.live > j.maxlive:
                            j.live = j.maxlive
                    else:
                        j.live = int(j.live - i.hurt)
                    if j.live <= 0:
                        if j.rint != 0:
                            cls.emojiDeath(j)
                        elif j.rint == 0:
                            cls.bossDeath(j)
                        cls.g_enemies.remove(j)
                    try:
                        if i.Remove:
                            cls.wateremoji.allbumb.remove(i)
                    except ValueError:
                        pass

    @classmethod
    def gameover(cls):
        for i in cls.g_enemies:
            if pygame.sprite.collide_mask(cls.wateremoji, i) and time.time() - cls.latesttime >= 1:
                cls.wateremoji.live -= 10
                cls.latesttime = time.time()
                if cls.wateremoji.live <= 0:
                    cls.wateremoji.live = 0
                    return True
        return False

    @classmethod
    def waitForKeyPress(cls):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    cls.terminate()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        return

    @staticmethod
    def terminate():
        pygame.quit()
        sys.exit(0)

    @classmethod
    def pause(cls, screen, image):
        screen.blit(image, (0, 0))
        pygame.display.update()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    cls.terminate()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE or pygame.K_ESCAPE:
                        return

    @classmethod
    def showPower(cls):
        pygame.draw.rect(cls.screen, (0, 0, 0), (39, 439, 122, 22))
        pygame.draw.rect(cls.screen, (123, 123, 123), (40, 440, 120, 20))
        if cls.power != 100:
            pygame.draw.rect(cls.screen, (0, 0, 255), (40, 440, int(120 * (cls.power / 100)), 20))
        else:
            pygame.draw.rect(cls.screen, (199, 21, 133), (40, 440, 120, 20))

    @classmethod
    def showLife(cls, font, screen):  # 显示地方emoji的血量
        for i in cls.g_enemies:
            if not i.isboss:
                pygame.draw.rect(cls.screen, (123, 123, 123), (i.x, i.y - 10, 40, 5))
                pygame.draw.rect(cls.screen, (255, 0, 0),
                                 (i.x, i.y - 10, int(40 * (i.live / i.maxlive)), 5))
        pygame.draw.rect(cls.screen, (123, 123, 123), (cls.wateremoji.x, cls.wateremoji.y - 10, 40, 5))
        pygame.draw.rect(cls.screen, (255, 0, 0),
                         (cls.wateremoji.x, cls.wateremoji.y - 10,
                          int(40 * (cls.wateremoji.live / cls.wateremoji.maxlive)), 5))
        cls.drawText('%s/%s' % (cls.wateremoji.live, cls.wateremoji.maxlive), font, screen, cls.wateremoji.x,
                     cls.wateremoji.y - 15)

    @staticmethod
    def drawText(text, font, screen, x, y):
        content = font.render(text, False, (0, 0, 0))
        contentRect = content.get_rect()
        contentRect.left = x
        contentRect.top = y
        screen.blit(content, contentRect)

    @classmethod
    def crazyShoot(cls):
        for i in range(20):
            for j in range(0, 480, 40):
                cls.wateremoji.allbumb.append(Bullt.WaterBumb(cls.wateremoji.x, j, cls.wateremoji.hurt))
            time.sleep(0.1)

    @classmethod
    def blowbullut(cls):
        for i in cls.allenbumbs:
            i.direction = 'right'
            i.tan = 0
            i.sample = 0
            i.blow = True

    @classmethod
    def waterTimeStop(cls, screen):
        font1 = pygame.font.SysFont('arial', 12)
        font2 = pygame.font.SysFont(None, 20)
        Game.watertime.play()
        while cls.istimestoptime:
            if Game.haveBoss is True and Game.boss.bossrint == 1:  # 唐氏出场的换背景图的技能
                screen.blit(Game.boss1r, (0, 0))
            elif Game.haveBoss is True and Game.boss.bossrint == 2:
                screen.blit(Game.boss2r, (0, 0))
                try:
                    Game.showPrevent(screen)
                except IndexError:
                    pass
            elif Game.haveBoss is True and Game.boss.bossrint == 3:
                screen.blit(Game.boss3r, (0, 0))
            elif Game.haveBoss and Game.boss.bossrint == 4:
                screen.blit(Game.boss4r, (0, 0))
            elif Game.haveBoss and Game.boss.bossrint == 5:
                screen.blit(Game.boss5r, (0, 0))
            else:
                screen.blit(Game.backgroundImage2, (0, 0))
            if Game.haveBoss:
                Game.drawBoss()
            Game.drawText('score:%s' % (Game.score), font1, screen, 40, 10)
            Game.drawText('money:%s' % (Game.money), font1, screen, 40, 30)
            Game.drawText('gametime:%s' % ('TIMESTOP'), font1, screen, 540, 10)
            Game.showLife(font2, screen)
            Game.showPower()
            for i in Game.g_enemies:
                Game.screen.blit(i.image, (i.x, i.y))
            for i in Game.allenbumbs:
                try:
                    Game.screen.blit(i.image, (i.x, i.y))
                except pygame.error:
                    pass
            for i in Game.wateremoji.allbumb:
                Game.screen.blit(i.image, (i.x, i.y))
            try:
                for i in Game.allsupply:
                    Game.screen.blit(i.image, (i.x, i.y))
            except pygame.error:
                pass
            cls.wateremoji.shoot()
            if Skill.BossSkillSecond.hasAttr:  # 如果有心形传送门就把它画出来
                Game.showAttr(screen)
            try:
                Game.draw(screen)
            except pygame.error:
                pass
            Game.getEffect()
            pygame.display.update()
            tl = pygame.time.Clock()
            tl.tick(Game.FPS)

    @classmethod
    def powerShoot(cls):
        cls.wateremoji.canShoot = False
        for j in range(30):
            index = 50
            for i in range(4):
                while cls.isBossTimestop:
                    time.sleep(1)
                newbumb = Bullt.WaterBumb(cls.wateremoji.x, cls.wateremoji.y + index, cls.wateremoji.hurt / 1.8)
                newbumb.Remove = False
                newbumb.image = cls.special
                newbumb.rect = newbumb.image.get_rect()
                newbumb.rect.left, newbumb.rect.top = newbumb.x, newbumb.y
                cls.wateremoji.allbumb.append(newbumb)
                index -= 25
            time.sleep(0.1)
        cls.wateremoji.canShoot = True

    @classmethod
    def keyEvent(cls, screen, keylist, gamepauseImage):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Game.terminate()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE or e.key == pygame.K_ESCAPE:
                    Game.pause(screen, gamepauseImage)
                if e.key == pygame.K_e:
                    if cls.power == 100:
                        cls.power = 0
                        th = threading.Thread(target=cls.powerShoot)
                        th.daemon = True
                        th.start()
                if e.key == pygame.K_j:
                    if Game.money >= 2000:
                        Game.money -= 2000
                        th = threading.Thread(target=cls.crazyShoot)
                        th.daemon = True
                        th.start()
                if e.key == pygame.K_k:
                    if Game.money >= 2400:
                        Game.money -= 2400
                        cls.blowbullut()
                if e.key == pygame.K_l and not cls.istimestoptime:
                    if Game.money >= 2400:
                        Game.money -= 2400
                        th = threading.Thread(target=cls.waterTimeStop, args=(screen,))
                        th.daemon = True
                        th.start()
                        times = time.time()
                        cls.istimestoptime = True
                        while time.time() - times <= 2:
                            keylist = pygame.key.get_pressed()
                            Game.keyEvent(screen, keylist, Game.gamepauseImage)
                            pygame.time.Clock().tick(Game.FPS)
                        cls.istimestoptime = False

        if cls.haveBoss and cls.boss.bossrint == 3 and cls.gold:
            if (keylist[pygame.K_RIGHT] or keylist[pygame.K_d]) and (keylist[pygame.K_UP] or keylist[pygame.K_w]):
                Game.getkey('left-down')
            elif (keylist[pygame.K_RIGHT] or keylist[pygame.K_d]) and (
                    keylist[pygame.K_DOWN] or keylist[pygame.K_s]):
                Game.getkey('left-up')
            elif (keylist[pygame.K_LEFT] or keylist[pygame.K_a]) and (keylist[pygame.K_UP] or keylist[pygame.K_w]):
                Game.getkey('right-down')
            elif (keylist[pygame.K_LEFT] or keylist[pygame.K_a]) and (
                    keylist[pygame.K_DOWN] or keylist[pygame.K_s]):
                Game.getkey('right-up')
            elif keylist[pygame.K_UP] or keylist[pygame.K_w]:
                Game.getkey('down')
            elif keylist[pygame.K_DOWN] or keylist[pygame.K_s]:
                Game.getkey('up')
            elif keylist[pygame.K_LEFT] or keylist[pygame.K_a]:
                Game.getkey('right')
            elif keylist[pygame.K_RIGHT] or keylist[pygame.K_d]:
                Game.getkey('left')
        else:
            if (keylist[pygame.K_RIGHT] or keylist[pygame.K_d]) and (keylist[pygame.K_UP] or keylist[pygame.K_w]):
                Game.getkey('right-up')
            elif (keylist[pygame.K_RIGHT] or keylist[pygame.K_d]) and (
                    keylist[pygame.K_DOWN] or keylist[pygame.K_s]):
                Game.getkey('right-down')
            elif (keylist[pygame.K_LEFT] or keylist[pygame.K_a]) and (keylist[pygame.K_UP] or keylist[pygame.K_w]):
                Game.getkey('left-up')
            elif (keylist[pygame.K_LEFT] or keylist[pygame.K_a]) and (
                    keylist[pygame.K_DOWN] or keylist[pygame.K_s]):
                Game.getkey('left-down')
            elif keylist[pygame.K_UP] or keylist[pygame.K_w]:
                Game.getkey('up')
            elif keylist[pygame.K_DOWN] or keylist[pygame.K_s]:
                Game.getkey('down')
            elif keylist[pygame.K_LEFT] or keylist[pygame.K_a]:
                Game.getkey('left')
            elif keylist[pygame.K_RIGHT] or keylist[pygame.K_d]:
                Game.getkey('right')
