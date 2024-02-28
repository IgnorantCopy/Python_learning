"""
Created by Ignorant on 2024/2/25
Description: Producer & Consumer
"""
import queue
import random
import threading
import time


def producer(q):
    counter = 0
    while counter < 10:
        number = random.randint(1, 100)
        q.put(number)
        print("produce", number)
        time.sleep(0.2)
        counter += 1
    q.put(None)
    q.task_done()


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("consume", item)
        time.sleep(1)
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    list1 = []

    # producer
    thread1 = threading.Thread(target=producer, args=(q,))
    thread1.start()
    # consumer
    thread2 = threading.Thread(target=consumer, args=(q,))
    thread2.start()

    thread1.join()
    thread2.join()
    print("Done")

'''
process v.s. thread
    > communication:
        every process has a copy itself
        all the threads share the data
'''
