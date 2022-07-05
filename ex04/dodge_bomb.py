import re
import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) #Surface
    screen_rect = screen_sfc.get_rect() #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bgimg_rect = bgimg_sfc.get_rect() #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rect)

    #pg.display.update()

    clock.tick(0.5)

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)

        #練習２
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
    
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()