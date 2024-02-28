"""
Created by Ignorant on 2024/2/28
Description: Coroutine & gevent
"""
import time

import gevent
from gevent import monkey

monkey.patch_all()


def task1():
    for i in range(5):
        print('Task1-' + str(i))
        time.sleep(0.2)


def task2():
    for i in range(5):
        print('Task2-' + str(i))
        time.sleep(0.4)


def task3():
    for i in range(5):
        print('Task3-' + str(i))
        time.sleep(0.8)


if __name__ == '__main__':
    gevent1 = gevent.spawn(task1)
    gevent2 = gevent.spawn(task2)
    gevent3 = gevent.spawn(task3)

    gevent.joinall([gevent1, gevent2, gevent3])
