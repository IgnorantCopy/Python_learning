"""
Created by Ignorant on 2024/1/22
Description: Definition of Function
"""

import random

'''
format
def <name>([arguments]):
    codes...
'''


# without argument
def generate_str1():
    code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    string = ""
    for i in range(4):
        string += code[random.randint(0, len(code) - 1)]
    return string


# with argument
def plus(a, b):
    """
    isinstance(__obj: object,
            __class_or_tuple: type | UnionType | tuple[type | tuple[Any, ...], ...]
                                | tuple[type | UnionType | tuple[Any, ...], ...])
                -> bool
        Return whether an object is an instance of a class or of a subclass thereof.

        A tuple, as in isinstance(x, (A, B, ...)), may be given as the target to check against.
        This is equivalent to isinstance(x, A) or isinstance(x, B) or ... etc.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        print("Wrong type!")


# with default argument
# the default arguments must be after the common arguments
def borrow_book(book_name, name, number=1, school="nju"):
    print("Entering {} borrow-book system".format(school))
    print("{} borrows {} {}".format(name, number, book_name))


# with a list argument
def get_list(list1):
    return [e for e in list1 if e >= 60]


# changeable arguments
def get_sum(*args):
    num = 0
    # args: a tuple storing the arguments
    for i in args:
        num += i
    return num


# key word arguments
def show_book(**kwargs):
    print(kwargs)


# return multiple results
def get_max_min(*args):
    max_number = args[0]
    min_number = args[0]
    for i in args:
        max_number = i if i > max_number else max_number
        min_number = i if i < min_number else min_number
    return max_number, min_number


print(generate_str1())
print(plus(5, 5))
print()

borrow_book("Three body", "Carl", 3)
borrow_book("Three body", "Carl", school="stju")
print()

print(get_list([50, 60, 70, 80]))
print(get_sum(1, 2, 3, 4, 5))
print(get_sum(*[1, 2, 3, 4, 5]))
print()

show_book(bookname="Three Body", author="CiXin Liu", price=60.98)
show_book(**{"bookname": "Three Body", "author": "CiXin Liu", "price": 60})
print(get_max_min(1, 1, 2, 3, 4))
