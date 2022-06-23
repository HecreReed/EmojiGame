import Skill, random, time, threading


class Skills:
    lastskilltime = 0

    @classmethod
    def FirstBossSkill(cls):
        Skill.BossSkillFirst.melySkill()
        if time.time() - cls.lastskilltime >= random.randint(5, 9):
            randoms = random.random()
            if randoms < 0.25:
                newthread = threading.Thread(target=Skill.BossSkillFirst.sandShoot)
            elif 0.25 <= randoms < 0.5:
                newthread = threading.Thread(target=Skill.BossSkillFirst.summonTeleport)
            elif 0.5 <= randoms < 0.75:
                newthread = threading.Thread(target=Skill.BossSkillFirst.shootaside)
            else:
                newthread = threading.Thread(target=Skill.BossSkillFirst.starShoot)
            cls.lastskilltime = time.time()
            newthread.daemon = True
            newthread.start()

    @classmethod
    def SecondBossSkill(cls):
        if time.time() - cls.lastskilltime >= random.randint(5, 9):
            Skill.BossSkillSecond.createPrevent()
            randoms = random.random()
            if randoms > 0.66:
                newthread = threading.Thread(target=Skill.BossSkillSecond.generateLove)
            elif 0.33 < randoms <= 0.66:
                newthread = threading.Thread(target=Skill.BossSkillSecond.useAttract)
            else:
                newthread = threading.Thread(target=Skill.BossSkillSecond.madeinheaven)
            newthread.daemon = True
            newthread.start()
            cls.lastskilltime = time.time()

    @classmethod
    def ThirdBossSkill(cls):
        if time.time() - cls.lastskilltime >= random.randint(5, 9):
            Skill.BossSkillSecond.createPrevent()
            randoms = random.random()
            if 0 <= randoms < 0.25:
                newthread = threading.Thread(target=Skill.BossSkillThird.setgold)
                newthread.daemon = True
                newthread.start()
            elif 0.25 <= randoms < 0.5:
                newthread = threading.Thread(target=Skill.BossSkillThird.cutBody)
                newthread.daemon = True
                newthread.start()
            elif 0.5 <= randoms < 0.75:
                Skill.BossSkillThird.timestop()
            else:
                newthread = threading.Thread(target=Skill.BossSkillThird.superShoot)
                newthread.daemon = True
                newthread.start()
            cls.lastskilltime = time.time()

    @classmethod
    def ForthBossSkill(cls):
        if time.time() - cls.lastskilltime >= random.randint(5, 9):
            Skill.BossSkillSecond.createPrevent()
            randoms = random.random()
            if randoms >= 0.75:
                th = threading.Thread(target=Skill.BossSkillForth.lightshoot)
                th.daemon = True
                th.start()
            elif 0.5 <= randoms < 0.75:
                th = threading.Thread(target=Skill.BossSkillForth.dragShoot)
                th.daemon = True
                th.start()
            elif 0.25 <= randoms < 0.5:
                th = threading.Thread(target=Skill.BossSkillForth.summonUFO)
                th.daemon = True
                th.start()
            else:
                th = threading.Thread(target=Skill.BossSkillForth.sideShoot)
                th.daemon = True
                th.start()
            cls.lastskilltime = time.time()

    @classmethod
    def FifthBossSkill(cls):
        if time.time() - cls.lastskilltime >= random.randint(5, 9):
            Skill.BossSkillSecond.createPrevent()
            randoms = random.random()
            if randoms > 0.625:
                th = threading.Thread(target=Skill.BossSkillFifth.throwTNT)
                th.daemon = True
                th.start()
            elif 0.25 < randoms <= 0.625:
                th = threading.Thread(target=Skill.BossSkillFifth.jumpShoot)
                th.daemon = True
                th.start()
            else:
                th = threading.Thread(target=Skill.BossSkillFifth.healMode)
                th.daemon = True
                th.start()
            cls.lastskilltime = time.time()
