# limit the usage while using from import *
__all__ = ['PI', 'add', 'minus', 'multiply', 'divide', 'Calculator']
# constants
PI = 3.141592653589793
number = 100


# functions
def add(num1, num2, *args):
    temp = num1 + num2
    for i in args:
        temp += i
    return temp


def minus(num1, num2, *args):
    temp = num1 - num2
    for i in args:
        temp -= i
    return temp


def multiply(num1, num2, *args):
    temp = num1 * num2
    for i in args:
        temp *= i
    return temp


def divide(num1, num2, *args):
    temp = num1 / num2
    for i in args:
        temp /= i
    return temp


def test():
    print("Testing...")


# classes
class Calculator:
    def __init__(self, num):
        self.num = num

    def test(self):
        print("{} is entered to the calculator".format(self.num))


print("__name__: " + __name__)
if __name__ == '__main__':
    print(__name__)
    test()
