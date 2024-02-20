"""
Created by Ignorant on 2024/2/13
Description: Communication Between Processes
"""
from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ["boy.jpg", "girl.png", "man.png", "woman.png"]
    for image in images:
        print("Downloading " + image)
        sleep(0.5)
        q.put(image)


def get_file(q):
    while not q.empty():
        file = q.get()
        print("Saving {}...".format(file))


if __name__ == '__main__':
    queue = Queue()
    process1 = Process(target=download, args=(queue,))
    process2 = Process(target=get_file, args=(queue,))
    process1.start()
    process1.join()
    process2.start()
