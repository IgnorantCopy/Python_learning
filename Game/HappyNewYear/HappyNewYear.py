import sys

import pygame as p

WIDTH, HEIGHT = 1200, 800
p.init()
window = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('新年快乐')
p.display.flip()

image_list2 = [p.image.load('images/烟花（点击）/{}.png'.format(i)).convert_alpha() for i in range(2, 23)]
image_list3 = [p.image.load('images/烟花（满屏）/{}.png'.format(i)).convert_alpha() for i in range(1, 97)]
A, B, C = False, False, False
a, b, c, n = 0, 0, 0, 0


def update():
    p.draw.rect(window, (0, 0, 0), (0, 0, WIDTH, HEIGHT), 0)
    p.display.update()
    global A, B, C, a, b, c, count
    global x_m, y_m
    if B:
        window.blit(image_list2[b], (x_m - 300, y_m - 300))
        p.display.update()
        b += 1
        if b >= 20:
            b = 0
            B = False
    if C:
        x, y = image_list3[c].get_size()
        window.blit(image_list3[c], (600 - x / 2, 400 - y / 2))
        p.display.update()
        c += 1
        if c >= 95:
            c = 0
            C = False


while 1:
    n += 1
    if n % 300000 == 0:
        n = 0
        update()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN:
                b = 0
                x_m, y_m = event.pos
                B = True
            elif event.type == p.KEYUP:
                if event.key == p.K_ESCAPE:
                    p.quit()
                    sys.exit()
                elif event.key == p.K_z:
                    C = True
