"""
Created by Ignorant on 2024/2/25
Description: Thread Communication 1
"""
import threading
import time

ticket = 1000


def sell():
    global ticket
    for i in range(100):
        time.sleep(0.001)
        ticket -= 1


if __name__ == '__main__':
    thread1 = threading.Thread(target=sell)
    thread2 = threading.Thread(target=sell)
    thread3 = threading.Thread(target=sell)
    thread4 = threading.Thread(target=sell)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print(ticket)
