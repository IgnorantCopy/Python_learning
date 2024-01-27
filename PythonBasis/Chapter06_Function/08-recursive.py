"""
Created by Ignorant on 2024/1/27
Description: Recursive Functions
"""


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
