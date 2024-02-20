"""
Created by Ignorant on 2024/2/9
Description: Process
"""
import os
from multiprocessing import Process
from time import sleep


def task1(sec):
    while True:
        sleep(sec)
        print('Task1...', os.getpid(), os.getppid())


def task2(sec):
    while True:
        sleep(sec)
        print('Task2...', os.getpid(), os.getppid())


'''
start(): start child process
run(): method to be run in sub-process
terminate(): terminate child process
'''

counter = 0
# main process
if __name__ == '__main__':
    print(os.getpid())
    process1 = Process(target=task1, name="Task1", args=(0.5,))
    process2 = Process(target=task2, name="Task2", args=(1,))
    # child process
    process1.start()
    process2.start()
    while counter < 100:
        counter += 1
        print("counter:", counter)
        sleep(0.1)
    process1.terminate()
    process2.terminate()
    print(process1.name)
    print(process2.name)
