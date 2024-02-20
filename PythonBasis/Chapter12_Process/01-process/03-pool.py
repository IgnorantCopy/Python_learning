"""
Created by Ignorant on 2024/2/9
Description: Process Pool
"""
import os
import random
import time
from multiprocessing import Pool


def task1(name):
    print("Task 1: %s" % name)
    start = time.time()
    time.sleep(random.random() * 2)
    end = time.time()
    print(name, "over. Task duration:", end - start, "id:", os.getpid())
    return name


container = []


def callback_func(r):
    container.append(r)


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ["listen music", "play game", "cook", "wash clothes", "walk a dog", "eat"]
    for task in tasks:
        # asynchronize / non-blocked: 任务见缝插针
        pool.apply_async(task1, args=(task,), callback=callback_func)
    for task in tasks:
        # synchronize / blocked: 一个任务不结束另一个任务就不会添加进来
        pool.apply(task1, args=(task,))
    pool.close()  # stop adding tasks
    pool.join()  # host process concedes for child process
    print("all over")
    print(container)
