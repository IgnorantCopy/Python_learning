import pygame as p
import random, sys, math, time

WIDTH, HEIGHT = 600, 800
p.init()
window = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('弹球')
window.fill((255, 255, 255))
p.display.flip()
font1 = p.font.SysFont('simsun', 50)

x_brick, y_brick = 100, 50
x_platform, y_platform = 275, 700
hit = 0
zero = 0
waste_ball = 1


def single_brick(x, y):
    p.draw.rect(window, (255, 0, 0), (x, y, 20, 10), 0)
    p.draw.rect(window, (255, 255, 255), (x, y, 20, 10), 1)


def double_brick(x, y):
    p.draw.rect(window, (0, 255, 0), (x, y, 20, 10), 0)
    p.draw.rect(window, (255, 255, 255), (x, y, 20, 10), 1)


def triple_brick(x, y):
    p.draw.rect(window, (0, 0, 255), (x, y, 20, 10), 0)
    p.draw.rect(window, (255, 255, 255), (x, y, 20, 10), 1)


def draw_brick(mode, x, y):
    if mode == 0:
        p.draw.rect(window, (255, 255, 255), (x, y, 20, 10), 0)
    elif mode == 1:
        single_brick(x, y)
    elif mode == 2:
        double_brick(x, y)
    elif mode == 3:
        triple_brick(x, y)


def draw_all():
    global list_brick
    for i in list_brick:
        draw_brick(i[0], i[1], i[2])


list_brick = []
for i in range(800):
    n = random.randint(1, 3)
    draw_brick(n, x_brick, y_brick)
    list_brick.append([n, x_brick, y_brick])
    x_brick += 20
    if x_brick >= 500:
        x_brick = 100
        y_brick += 10

p.draw.rect(window, (0, 0, 0), (x_platform, y_platform, 50, 5), 0)
p.display.update()

image1 = p.image.load('resources/金属球.jpg')
image2 = p.transform.scale(image1, (10, 10))
x_ball, y_ball, r_ball = 290, 690, 5
x_speed, y_speed = 0, 0
is_move = False
is_stop = False
window.blit(image2, (x_ball, y_ball))

font2 = p.font.SysFont('simsun', 20)
text3 = font2.render('再来一局', True, (255, 255, 255))
text4 = font2.render('退出', True, (255, 255, 255))
x_r1, y_r1, w_r, h_r = 150, 420, 100, 50
x_r2, y_r2 = 350, 420
x_t1, y_t1, x_t2, y_t2, w_t1, h_t1, w_t2, h_t2 = 0, 0, 0, 0, 0, 0, 0, 0


def choice():
    global x_r1, y_r1, w_r, h_r, x_r2, y_r2, text3, text4
    global x_t1, y_t1, x_t2, y_t2, w_t1, h_t1, w_t2, h_t2
    p.draw.rect(window, (255, 0, 0), (x_r1, y_r1, w_r, h_r))
    p.draw.rect(window, (0, 255, 0), (x_r2, y_r2, w_r, h_r))
    w_t1, h_t1 = text3.get_size()
    x_t1, y_t1 = x_r1 + w_r / 2 - w_t1 / 2, y_r1 + h_r / 2 - h_t1 / 2
    window.blit(text3, (x_t1, y_t1))
    w_t2, h_t2 = text4.get_size()
    x_t2, y_t2 = x_r2 + w_r / 2 - w_t2 / 2, y_r2 + h_r / 2 - h_t2 / 2
    window.blit(text4, (x_t2, y_t2))
    p.display.update()


while 1:
    if is_move == True:
        if hit == 0:
            y_speed = -0.3
            p.draw.rect(window, (255, 255, 255), (x_ball, y_ball, 10, 10), 0)
            y_ball += y_speed
            window.blit(image2, (x_ball, y_ball))
            for i in list_brick:
                if i[1] <= x_ball + r_ball <= i[1] + 20 and round(y_ball) == i[2] + 10 and i[0] != 0:
                    hit += 1
                    y_speed = -y_speed
                    i[0] -= 1
                    draw_brick(i[0], i[1], i[2])
            p.display.update()
        elif hit == 1:
            p.draw.rect(window, (255, 255, 255), (x_ball, y_ball, 10, 10), 0)
            y_ball += y_speed * 3
            x_ball += x_speed
            draw_all()
            window.blit(image2, (x_ball, y_ball))
            p.display.update()
            if y_platform <= y_ball + 10 <= y_platform + 5 and x_platform <= x_ball + 5 <= x_platform + 50:
                y_speed = -y_speed
                x_speed = math.sin(((x_ball + 5) - (x_platform + 25)) / 25 * (math.pi / 2) * 0.1) * 8

            for i in list_brick:
                if i[1] <= x_ball + r_ball <= i[1] + 20 and i[0] != 0:
                    if round(y_ball + 10) == i[2] or round(y_ball) == i[2] + 10:
                        y_speed = -y_speed
                        i[0] -= 1
                        draw_brick(i[0], i[1], i[2])
                        p.display.update()
                elif i[2] <= y_ball + r_ball <= i[2] + 10 and i[0] != 0:
                    if round(x_ball + 10) == i[1] or round(x_ball) == i[1] + 20:
                        x_speed = -x_speed
                        i[0] -= 1
                        draw_brick(i[0], i[1], i[2])
                        p.display.update()
                if i[0] <= 0:
                    zero += 1

            if zero == 800:
                x_speed, y_speed = 0, 0
                text1 = font1.render('游戏结束！', True, (0, 0, 0), (255, 255, 255))
                text2 = font1.render('用了{}个球'.format(waste_ball), True, (0, 0, 0), (255, 255, 255))
                window.blit(text1, (200, 300))
                window.blit(text2, (200, 360))
                p.display.update()
                zero = 0
                hit = -1
                is_stop = True
                choice()
            else:
                zero = 0

            if y_ball + 10 >= 800 or ((x_ball + 10 >= 600 or x_ball <= 0) and y_ball + 10 > 700):
                p.draw.rect(window, (255, 255, 255), (x_ball, y_ball, 10, 10), 0)
                time.sleep(1)
                waste_ball += 1
                hit = 0
                is_move = False
            elif y_ball <= 0:
                y_speed = -y_speed
            elif x_ball + 10 >= 600 or x_ball <= 0:
                x_speed = -x_speed
        elif hit == -1:
            x_speed, y_speed = 0, 0

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
        elif event.type == p.MOUSEMOTION:
            p.draw.rect(window, (255, 255, 255), (x_platform, y_platform, 50, 5), 0)
            x, y = event.pos
            x_platform = x - 25
            p.draw.rect(window, (0, 0, 0), (x_platform, y_platform, 50, 5), 0)
            p.display.update()
            if is_move == False:
                y_ball = 690
                p.draw.rect(window, (255, 255, 255), (x_ball, y_ball, 10, 10), 0)
                x_ball = x - 5
                window.blit(image2, (x_ball, y_ball))
                p.display.update()
        elif event.type == p.MOUSEBUTTONUP:
            if is_stop == True:
                x_m, y_m = event.pos
                if x_r1 <= x_m <= x_r1 + w_r and y_r1 <= y_m <= y_r1 + h_r:
                    p.draw.rect(window, (255, 0, 0), (x_r1, y_r1, w_r, h_r))
                    window.blit(text3, (x_t1, y_t1))
                    p.display.update()
                    time.sleep(0.5)
                    p.draw.rect(window, (255, 255, 255), (0, 0, 600, 650))
                    p.display.update()
                    is_stop = False
                    is_move = False
                    hit = 0
                    list_brick = []
                    x_brick, y_brick = 100, 50
                    zero = 0
                    waste_ball = 1
                    for i in range(800):
                        n = random.randint(1, 3)
                        draw_brick(n, x_brick, y_brick)
                        list_brick.append([n, x_brick, y_brick])
                        x_brick += 20
                        if x_brick >= 500:
                            x_brick = 100
                            y_brick += 10
                elif x_r2 <= x_m <= x_r2 + w_r and y_r2 <= y_m <= y_r2 + h_r:
                    p.draw.rect(window, (0, 255, 0), (x_r2, y_r2, w_r, h_r))
                    window.blit(text4, (x_t2, y_t2))
                    p.display.update()
                    time.sleep(0.5)
                    p.quit()
                    sys.exit()
        elif event.type == p.MOUSEBUTTONDOWN:
            is_move = True
            if is_stop == True:
                x_m, y_m = event.pos
                if x_r1 <= x_m <= x_r1 + w_r and y_r1 <= y_m <= y_r1 + h_r:
                    p.draw.rect(window, (200, 200, 200), (x_r1, y_r1, w_r, h_r))
                    window.blit(text3, (x_t1, y_t1))
                    p.display.update()
                elif x_r2 <= x_m <= x_r2 + w_r and y_r2 <= y_m <= y_r2 + h_r:
                    p.draw.rect(window, (200, 200, 200), (x_r2, y_r2, w_r, h_r))
                    window.blit(text4, (x_t2, y_t2))
                    p.display.update()
        elif event.type == p.KEYUP:
            if chr(event.key) == 'm':
                for i in list_brick:
                    i[0] = 0
                    p.draw.rect(window, (255, 255, 255), (i[1], i[2], 20, 10), 0)
                    p.display.update()
                x_speed, y_speed = 0, 0
                text1 = font1.render('游戏结束！', True, (0, 0, 0), (255, 255, 255))
                text2 = font1.render('用了{}个球'.format(waste_ball), True, (0, 0, 0), (255, 255, 255))
                window.blit(text1, (200, 300))
                window.blit(text2, (200, 360))
                hit = -1
                is_stop = True
                choice()
                p.display.update()