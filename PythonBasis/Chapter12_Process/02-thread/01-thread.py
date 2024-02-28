"""
Created by Ignorant on 2024/2/13
Description: Thread
"""
import threading
import time


def download(n):
    images = ["girls.png", "boys.png", "man.jpg", "woman.jpg"]
    for image in images:
        print("Downloading", image)
        time.sleep(n)
        print("Done downloading", image)


def listen_music(n):
    musics = ["Hey Jude", "Come Together", "She Is My Sin"]
    for music in musics:
        time.sleep(n)
        print("Listening", music)


'''
conditions of thread:
    > new
    > ready
    > run
    > block
    > end
'''
if __name__ == '__main__':
    # create a thread: threading.Thread(target=func, name= < name >, args = (), kwargs = {})
    thread1 = threading.Thread(target=download, name="Download", args=(3,))
    thread1.start()
    thread2 = threading.Thread(target=listen_music, name="Listen Music", args=(3,))
    thread2.start()
    counter = 1
    while True:
        print(counter)
        time.sleep(1.5)
        counter += 1
