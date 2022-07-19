import pygame as pg
import sys
import random
import numpy as np
max_bm = 0
bg_x = 0
maxspeed = 3
t = 0
#スクリーン用クラス
class Screen:
    def __init__(self, title, wh: tuple, img):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rect = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(img).convert()
        self.bg_rect = self.bg_sfc.get_rect()

    def blit(self,bg_x):
        self.sfc.blit(self.bg_sfc,[bg_x-1600,0])
        self.sfc.blit(self.bg_sfc,[bg_x,0])

#こうかとん用クラス
class Bird:
    def __init__(self, img, size: float, xy: tuple):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rect = self.sfc.get_rect()
        self.rect.center = xy
        self.vey = 0
        self.jump = False

    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        key = pg.key.get_pressed()
        tori_speed = 1
        if key[pg.K_UP]:
            self.rect.centery -= tori_speed
        if key[pg.K_DOWN]:
            self.rect.centery += tori_speed
        if key[pg.K_LEFT]:
            self.rect.centerx -= tori_speed
        if key[pg.K_RIGHT]:
            self.rect.centerx += tori_speed
        if key[pg.K_SPACE] and self.jump == False:
            self.jump = True
            self.rect.centery-= 5
        if self.jump == True:
            self.rect.centery +=1
        
        if check_bound(self.rect, screen.rect) != (1, 1):
            if key[pg.K_UP]:
                self.rect.centery += tori_speed
            if key[pg.K_DOWN]:
                self.rect.centery -= tori_speed
            if key[pg.K_LEFT]:
                self.rect.centerx += tori_speed
            if key[pg.K_RIGHT]:
                self.rect.centerx -= tori_speed
        self.blit(screen)


#爆弾用クラス
class Bomb:
    def __init__(self, color: tuple, rad: int, screen: Screen):
        self.sfc = pg.Surface((rad * 2 , rad * 2))
        self.sfc.set_colorkey((0, 0, 0))
        for i in range(4):
            pg.draw.circle(self.sfc, (color[0] - i * color[0] // 4, color[1] - i * color[1] // 4, color[2] - i * color[2] // 4), (rad, rad), rad - i * (rad // 4 + 1))
        self.rect = self.sfc.get_rect()
        self.rect.centerx = 1600
        self.rect.centery = random.randint(rad * 2, screen.rect.height - rad * 2)
        self.vx = np.random.choice([-1, 1])


    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        global maxspeed
        global max_bm
        max_bm = random.randint(1,5)
        for i in range(max_bm):
            self.rect.move_ip(-1,0)
            maxspeed = 3
            self.blit(screen)


def main():
    global maxspeed
    global bg_x
    global t
    #fpsのカウント開始
    clock = pg.time.Clock()
    sc = Screen("負けるな！こうかとん", (1600, 900), "ex06/fig/pg_bg.jpg")
    tori = Bird("ex06/fig/6.png", 2.0, (900, 400))
    bomb = Bomb((255, 0, 0), 50, sc)

    #描画
    while True:
        t += 1
        bg_x = (bg_x-0.6)%1600
        sc.blit(bg_x)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        if t%2000 == 0:
            bomb = Bomb((255, 0, 0), 50, sc)
        tori.update(sc)
        bomb.update(sc)

        if tori.rect.colliderect(bomb.rect):
            return
        maxspeed += 0.001

        pg.display.update()
        clock.tick(1000)

def check_bound(rect, sc_rect):
    w, h = 1, 1
    if rect.left < sc_rect.left or rect.right > sc_rect.right:
        w = -1
    if rect.top < sc_rect.top or rect.bottom > sc_rect.bottom:
        h = -1
    return w, h


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()