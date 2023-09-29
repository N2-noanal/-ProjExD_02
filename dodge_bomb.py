import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900,400
    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))
    x, y = random.randint(0,1600), random.randint(0,900)
    vx,vy = +5, +5
    enn_rct = enn.get_rect()
    enn_rct.center = x, y
    clock = pg.time.Clock()
    tmr = 0
    key_zi = {
        pg.K_UP: (0,-5),
        pg.K_DOWN: (0,+5),
        pg.K_LEFT: (-5,0),
        pg.K_RIGHT: (+5,0),
        }
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [kk_rct.x, kk_rct.y])
        
        key_lst = pg.key.get_pressed()
        total = [0, 0]
        for k, m in key_zi.items():
            if key_lst[k]:
                total[0] += m[0]
                total[1] += m[1]
        kk_rct.move_ip(total)
        
        screen.blit(enn, [enn_rct.x, enn_rct.y])
        enn_rct.move_ip(vx,vy)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()