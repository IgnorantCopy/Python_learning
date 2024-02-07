def func():
    from module1 import task1
    print("func in module2")
    task1()


if __name__ == '__main__':
    func()
