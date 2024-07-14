import turtle as t

import numpy as np


def dot(x, y, size=max(t.pensize() + 4, 2 * t.pensize())):
    t.up()
    t.goto(x, y)
    t.down()
    t.dot(size, t.pencolor())


def bessel(*coordinate, precision=10):
    n = len(coordinate) // 2

    t.pencolor('red')
    for i in range(n):
        dot(coordinate[2 * i], coordinate[2 * i + 1])
    t.pencolor('black')
    t.up()
    t.goto(coordinate[0], coordinate[1])
    t.down()

    xs = []
    ys = []
    for i in range(0, n - 1):
        x1 = coordinate[2 * i]
        y1 = coordinate[2 * i + 1]
        x2 = coordinate[2 * i + 2]
        y2 = coordinate[2 * i + 3]
        xs.append(np.linspace(x1, x2, precision))
        ys.append(np.linspace(y1, y2, precision))
    n -= 1

    for i in range(precision - 1):
        new_n = n
        new_xs = []
        for j in range(len(xs)):
            new_xs.append(xs[j])
        new_ys = []
        for j in range(len(ys)):
            new_ys.append(ys[j])
        while new_n > 2:
            for j in range(new_n - 1):
                x1 = new_xs[j][i + 1]
                x2 = new_xs[j + 1][i + 1]
                y1 = new_ys[j][i + 1]
                y2 = new_ys[j + 1][i + 1]
                new_xs[j] = np.linspace(x1, x2, precision)
                new_ys[j] = np.linspace(y1, y2, precision)
            new_ys.pop()
            new_xs.pop()
            new_n -= 1

        x1 = new_xs[0][i + 1]
        x2 = new_xs[1][i + 1]
        y1 = new_ys[0][i + 1]
        y2 = new_ys[1][i + 1]
        x = np.linspace(x1, x2, precision)[i + 1]
        y = np.linspace(y1, y2, precision)[i + 1]
        t.goto(x, y)


t.setup(800, 600)
t.speed(0)
bessel(-300, -50, -200, 200, 100, 50, precision=600)
t.done()
