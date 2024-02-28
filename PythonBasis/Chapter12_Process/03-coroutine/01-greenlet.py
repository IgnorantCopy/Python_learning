"""
Created by Ignorant on 2024/2/28
Description: Coroutine & greenlet
"""
import time

import greenlet


def task1():
    for i in range(5):
        print('Task1-' + str(i))
        greenlet2.switch()
        time.sleep(0.2)


def task2():
    for i in range(5):
        print('Task2-' + str(i))
        greenlet3.switch()
        time.sleep(0.4)


def task3():
    for i in range(5):
        print('Task3-' + str(i))
        greenlet1.switch()
        time.sleep(0.8)


if __name__ == '__main__':
    greenlet1 = greenlet.greenlet(task1)
    greenlet2 = greenlet.greenlet(task2)
    greenlet3 = greenlet.greenlet(task3)

    greenlet1.switch()
