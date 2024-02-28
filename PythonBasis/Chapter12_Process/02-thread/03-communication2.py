"""
Created by Ignorant on 2024/2/25
Description: Thread Communication
"""
import threading

n = 0


def task1():
    global n
    for i in range(100000000):
        n += 1
    print("n in task1:", n)


def task2():
    global n
    for i in range(100000000):
        n += 1
    print("n in task2:", n)


'''
GIL: 全局解释器锁
在多个线程共享相同变量时，可能会出现在赋值语句进行之前被另一个线程抢占的情况，造成数据不安全，因此需要加锁
但是加锁会使得整个程序的效率降低

而在Python底层，只要用了线程就会默认加锁
'''
if __name__ == '__main__':
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(n)
