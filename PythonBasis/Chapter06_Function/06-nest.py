"""
Created by Ignorant on 2024/1/25
Description: Nested functions
"""


def outer():
    a = 100
    print(a)

    def inner():
        b = 50
        nonlocal a
        b += a
        print(b)

    inner()
    print(locals())
    return inner


# closure: nest + inner uses the variable in outer + return inner
result = outer()
print(result)
print()
outer()()
