"""
Created by Ignorant on 2024/1/26
Description: Decorator
"""

'''
functions of decorator:
    1.log
    2.do statics for run time
    3.pre-process before the function
    4.clear after the function
    5.qualify the authority
    6.cache
principle: do not modify the source code of the function while expanding the function of the function
'''


# empty decorator
def decorator1(func):
    print("-----------------> 1")

    def wrapper():
        func()
        print("Decorated Function")

    print("-----------------> 2")
    return wrapper


# decorator with arguments
def decorator2(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


# decorator with return value
def decorator3(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator1  # <=> func1 = decorator(func1)
def func1():
    print("func1...")


func1()
print()


@decorator2
def func2(n):
    print("f{}...".format(n))


func2(2)
print()


@decorator2
def func3(*args):
    for arg in args:
        print(arg)


func3(1, 2, 3, 4)
print()


@decorator3
def func4(*args):
    return sum(args)


print(func4(1, 2, 3, 4))
