"""
Created by Ignorant on 2024/2/13
Description: Queue
"""
from multiprocessing import Queue

queue = Queue(5)
# put(self, obj, block=True, timeout=None)
queue.put('a')
queue.put('b')
queue.put('c')
queue.put('d')
queue.put('e')
print(queue.qsize())
if queue.full():
    print(queue.get())
queue.put('f', timeout=3)  # wait
