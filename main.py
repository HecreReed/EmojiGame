# 黄豆流汗飞机大战
# made by Hecre_Reed
# coding = utf-8

# 导入pygame库和sys库
import pygame, time, sys, OEmoji, Bullt, random, sqlite3, Move, win32api, win32gui, wx, Frame, threading
from Event import *

Friend = 'friend'
Enemies = 'enemies'
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
if __name__ == '__main__':
    data = sqlite3.connect('data.db')
    curor = data.cursor()
    Game.rwidth = win32api.GetSystemMetrics(0)
    Game.rheight = win32api.GetSystemMetrics(1)
    try:
        curor.execute('create table user (id int(10) primary key,name varchar(20))')
    except sqlite3.OperationalError:
        pass
    try:
        curor.execute("insert into user values(1,0)")
        curor.execute("insert into user values(2,0)")
    except sqlite3.IntegrityError:
        pass
    curor.execute("select * from user")
    best = curor.fetchall()
    bestscore = int(best[0][1])
    money = int(best[1][1])
    Game.money = money
    pygame.init()
    pygame.mixer.init()
    Game.app = wx.App()
    loading = pygame.image.load('image/loading.png')
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    Game.screen = screen
    pygame.display.set_caption('流汗黄豆emoji抽象战争')
    screen.blit(loading, (0, 0))
    pygame.display.update()
    Game.Aleph = pygame.mixer.Sound('music/Aleph.mp3')
    Game.Death = pygame.mixer.Sound('music/Death.mp3')
    Game.Bgm.append(pygame.mixer.Sound('music/bgm1.mp3'))
    Game.Bgm.append(pygame.mixer.Sound('music/bgm2.mp3'))
    Game.Bgm.append(pygame.mixer.Sound('music/bgm3.mp3'))
    Game.Bgm.append(pygame.mixer.Sound('music/bgm4.mp3'))
    Game.Bgm.append(pygame.mixer.Sound('music/bgm5.mp3'))
    Game.Boardline = pygame.mixer.Sound('music/Boardline.mp3')
    Game.heaven = pygame.mixer.Sound('music/madeinheaven.wav')
    Game.golden = pygame.mixer.Sound('music/gold.wav')
    Game.theworld = pygame.mixer.Sound('music/theworld.wav')
    Game.temp = pygame.mixer.Sound('music/temp.mp3')
    Game.watertime = pygame.mixer.Sound('music/watertimestop.wav')
    Game.boss4bgm = pygame.mixer.Sound('music/boss4.mp3')
    Game.boss5bgm = pygame.mixer.Sound('music/boss5.mp3')
    Game.backgroundImage = pygame.image.load('image/sky.png')
    Game.backgroundImage2 = pygame.image.load('image/fucksky.png')
    Game.backgroundImage3 = pygame.image.load('image/redsky.png')
    Game.boss2r = pygame.image.load('image/redsky2.png')
    Game.boss1 = pygame.image.load('image/boss1.png')
    Game.boss3 = pygame.image.load('image/boss3.png')
    Game.boss3r = pygame.image.load('image/boss3r.png')
    Game.boss1r = pygame.image.load('image/boss1r.png')
    Game.boss4 = pygame.image.load('image/boss4.png')
    Game.boss4r = pygame.image.load('image/boss4r.png')
    Game.boss5 = pygame.image.load('image/boss5.png')
    Game.boss5r = pygame.image.load('image/boss5r.png')
    Game.bulluten.append(pygame.image.load('image/bossbullut-1.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-2.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-3.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-4.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-5.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-6.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-7.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-8.png'))
    Game.bulluten.append(pygame.image.load('image/enemybullut-1.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-9.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-10.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-11.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-12.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-13.png'))
    Game.bulluten.append(pygame.image.load('image/bossbullut-14.png'))
    Game.special = pygame.image.load('image/waterbullut2.png')
    gameoverImage = pygame.image.load('image/gameover.png')
    Game.gamepauseImage = pygame.image.load('image/gamepause.png')
    startImage = pygame.image.load('image/start.png')
    gamestartImage = pygame.image.load('image/gamestart.png')
    font = pygame.font.SysFont(None, 64)
    font1 = pygame.font.SysFont('arial', 12)
    font2 = pygame.font.SysFont(None, 20)
    screen.blit(gamestartImage, (0, 0))
    pygame.display.update()
    imagetime = time.time()  # 换背景图片的背景
    tl = pygame.time.Clock()
    tl.tick(Game.FPS)
    Game.waitForKeyPress()
    Game.gameinit()
    lastestTime = time.time()
    starttime = time.time()
    hwnd = pygame.display.get_wm_info()['window']
    rect = win32gui.GetWindowRect(hwnd)
    Game.rx = rect[0]
    Game.ry = rect[1]
    maxEmemies = 2
    maxBoss = 1
    choose = 1  # 选择背景图片，正为原图，反为反相
    Game.lastBoss = time.time()
    randomkis = 55 + 10 * random.random()
    Game.bgmnow = random.randint(0, 4)
    Game.Bgm[Game.bgmnow].play()
    while True:  # 主循环
        if Game.haveBoss is True and Game.boss.bossrint == 1:  # 唐氏出场的换背景图的技能
            if time.time() - imagetime >= 0.677:
                imagetime = time.time()
                choose = -choose
            if choose > 0:
                screen.blit(Game.boss1, (0, 0))
            elif choose < 0:
                screen.blit(Game.boss1r, (0, 0))
        elif Game.haveBoss is True and Game.boss.bossrint == 2:
            screen.blit(Game.backgroundImage3, (0, 0))
            try:
                Game.showPrevent(screen)
            except IndexError:
                pass
        elif Game.haveBoss is True and Game.boss.bossrint == 3:
            screen.blit(Game.boss3, (0, 0))
        elif Game.haveBoss is True and Game.boss.bossrint == 4:
            screen.blit(Game.boss4, (0, 0))
        elif Game.haveBoss is True and Game.boss.bossrint == 5:
            screen.blit(Game.boss5, (0, 0))
        else:
            screen.blit(Game.backgroundImage, (0, 0))
        screen.blit(startImage, (0, 0))
        if Game.haveBoss:
            Game.drawBoss()
        Game.drawText('score:%s' % (Game.score), font1, screen, 40, 10)
        Game.drawText('money:%s' % (Game.money), font1, screen, 40, 30)
        Game.drawText('gametime:%s' % (int(time.time() - starttime)), font1, screen, 540, 10)
        keylist = pygame.key.get_pressed()
        Game.keyEvent(screen, keylist, Game.gamepauseImage)
        interval = time.time() - lastestTime
        Game.showLife(font2, screen)
        Game.showPower()
        if time.time() - starttime <= randomkis:
            maxEmemies = int(2 + 1 / 15 * (time.time() - starttime))
            Game.maxEn = maxEmemies
        if interval >= 10 * random.random() and len(Game.g_enemies) < maxEmemies and Game.haveBoss is False:
            Game.createEnemy(0)
            lastestTime = time.time()
        if time.time() - Game.lastBoss >= random.randint(50, 60) and Game.haveBoss is False:
            Game.createBoss()
            Game.bosscreatetime = time.time()
            if Game.boss.bossrint == 2:
                Skill.BossSkillSecond.createFrame()
            if Game.boss.bossrint == 3:
                t1 = threading.Thread(target=Skill.BossSkillThird.teleport)
                t1.daemon = True
                t1.start()
                t2 = threading.Thread(target=Skill.BossSkillThird.moveFrameThird)
                t2.daemon = True
                t2.start()
        if Game.haveBoss is True:
            Game.bossUseSkill()
        th1 = threading.Thread(target=Game.shoot(screen))
        th1.daemon = True
        th1.start()
        if Skill.BossSkillSecond.hasAttr:  # 如果有心形传送门就把它画出来
            Game.showAttr(screen)
        Game.updateLocation()
        try:
            Game.draw(screen)
        except pygame.error:
            pass
        Game.supplyMove(screen)
        Game.getEffect()
        th2 = threading.Thread(target=Game.enshoot(screen))
        th2.daemon = True
        th2.start()
        pygame.display.update()
        tl.tick(Game.FPS)
        if Game.gameover() or Game.isok:
            time.sleep(1)
            screen.blit(gameoverImage, (0, 0))
            Game.drawText('score: %s' % (Game.score), font, screen, 170, 220)
            Game.drawText('best: %s' % (bestscore), font, screen, 170, 320)
            if (Game.score > bestscore):
                curor.execute('update user set name = ? where id = ?', (str(Game.score), 1))
            curor.execute('update user set name = ? where id = ?', (str(Game.money), 2))
            curor.execute("select * from user")
            k = curor.fetchall()
            curor.close()
            data.commit()
            data.close()
            pygame.display.update()
            Game.waitForKeyPress()
            break
