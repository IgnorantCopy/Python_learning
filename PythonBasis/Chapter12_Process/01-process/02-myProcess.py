"""
Created by Ignorant on 2024/2/9
Description: Self-define Process
"""
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        n = 1
        while n < 10:
            print("name:", self.name)
            n += 1


if __name__ == '__main__':
    process = MyProcess("Carl")
    process.start()
