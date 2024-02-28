"""
Created by ignorant on 2024/2/25
Description: Dead Lock
"""
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


# self-define thread
class MyThread1(threading.Thread):
    def run(self):  # start()
        if lock1.acquire():
            print(self.name, "got lock1")
            time.sleep(0.1)
            if lock2.acquire(timeout=5):
                print(self.name, "got lock2 too")
                lock2.release()
            lock1.release()


class MyThread2(threading.Thread):
    def run(self):
        if lock2.acquire():
            print(self.name, "got lock1")
            time.sleep(0.1)
            if lock1.acquire(timeout=5):
                print(self.name, "got lock2 too")
                lock1.release()
            lock2.release()


if __name__ == '__main__':
    thread1 = MyThread1()
    thread2 = MyThread2()

    thread1.start()
    thread2.start()
    # ==> dead lock
