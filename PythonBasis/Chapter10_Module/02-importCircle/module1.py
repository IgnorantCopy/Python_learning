def task1():
    print("Task1")


def task2():
    # the way to avoid import circle
    from module2 import func
    print("Task2")
    func()


if __name__ == '__main__':
    task2()
