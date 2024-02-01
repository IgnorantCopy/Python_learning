"""
Created by Ignorant on 2024/1/31
Description: Generator
"""

'''
Hook:
    通过列表推导式可以直接生成一个列表，但是受到内存限制，列表容量是有限的。
    所以，如果列表元素可以按照某种算法推算出来，那么就可以在循环的过程中不断推算出后续的元素。
    这样就不必创建完整的列表，从而节省大量的空间。
    在Python中的这种边循环边计算的机制，叫做 生成器(generator)。
'''

# ways to get generator
# 1.through inference
generator = (i for i in range(100000000000))
print(type(generator))
#   ways to get elements in generator
#   1.__next__()
for i in range(50):
    print(generator.__next__(), end=' ')
print()
#   2.next()
for i in range(50):
    print(next(generator), end=' ')
print()

'''
2.through function
    ① define a function and use the key word yield
    ② use the function and get the result
    ③ the result is a generator
'''


def generator():
    n = 0
    while True:
        yield n  # return n + pause(yield)
        n += 1


generator = generator()
for i in range(50):
    print(next(generator), end=' ')
print()


# exercise
def fibonacci(maximum):
    n1, n2 = 0, 1
    n = 0
    while n < maximum:
        n1, n2 = n2, n1 + n2
        yield n1
        n += 1


generator = fibonacci(10)
for i in generator:
    print(i, end=' ')
print()


# send
def func():
    i = 0
    while i < 5:
        temp = yield i
        print("temp:", temp)
        i += 1
    return "nothing else"


generator = func()
print(generator.send(None))  # the argument of the first send must be None
print(generator.send("gg"))
print(generator.send("jj"))
print()

'''
methods in generator:
    1.__next__(self): get the next element from the generator
    2.send(self, __value): send a value to the generator in each call and return the next element
'''


# python中的协程的概念：协程与线程的关系，就好比线程与进程的关系
def task1(n):
    for i in range(n):
        print("task1:", i)
        yield None


def task2(n):
    for i in range(n):
        print("task2:", i)
        yield None


g1 = task1(10)
g2 = task2(5)
while True:
    temp = 0
    try:
        next(g1)
    except StopIteration:
        temp += 1
    try:
        next(g2)
    except StopIteration:
        temp += 1
    if temp == 2:
        break
