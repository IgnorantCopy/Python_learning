"""
Created by Ignorant on 2024/2/25
Description: Synchronize
"""
import threading
import time

lock = threading.Lock()
list1 = [0] * 10


def task1():
    # wait for unlock
    lock.acquire()  # block
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()


def task2():
    lock.acquire()
    for i in range(len(list1)):
        print(list1[i])
        time.sleep(0.5)
    lock.release()


if __name__ == '__main__':
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    thread1.start()
    thread2.start()
