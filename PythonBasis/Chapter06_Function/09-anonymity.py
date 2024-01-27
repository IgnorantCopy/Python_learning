"""
Created by Ignorant on 2024/1/27
Description: Anonymous Function
"""
from functools import reduce

# format: lambda <arguments>: <return operation>
add = lambda x, y: x + y
print(add(1, 2))


# apply
# 高阶函数
def func1(n, f):
    print(n, f(n))


func1(10, lambda x: x ** 2)
print()

'''
max(__arg1: SupportsRichComparisonT,
        __arg2: SupportsRichComparisonT,
        *_args: SupportsRichComparisonT,
        key: None = None) -> SupportsRichComparisonT
    With a single iterable argument, return its biggest item.
    The default keyword-only argument specifies an object to return if the provided iterable is empty.
    With two or more arguments, return the largest argument.

sorted(__iterable: Iterable[SupportsRichComparisonT],
        *,
        key: None = None,
        reverse: bool = False) -> list[SupportsRichComparisonT]
    Return a new list containing all items from the iterable in ascending order.
    A custom key function can be supplied to customize the sort order,
    and the reverse flag can be set to request the result in descending order.

class filter(Iterator[_T], Generic[_T])
    Return an iterator yielding those items of iterable for which function(item) is true.
    If function is None, return the items that are true.

class map(Iterator[_S], Generic[_S])
    Make an iterator that computes the function using arguments from each of the iterables.
    Stops when the shortest iterable is exhausted.
'''
list1 = [("Jack", 19), ("John", 20), ("Jerry", 18), ("Tom", 25)]
print(max(list1, key=lambda x: x[1]))
print(min(list1, key=lambda x: x[1]))
print(sorted(list1, key=lambda x: x[1], reverse=True))
print(list(filter(lambda x: x[1] < 20, list1)))
print(list(map(lambda x: x[1] + 1, list1)))
print(list(map(lambda x: x[0].lower(), list1)))
print()

'''
reduce(function: (_T, _S) -> _T,
        sequence: Iterable[_S],
        initial: _T) -> _T
    Apply a function of two arguments cumulatively to the items of a sequence, from left to right,
    so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
    If initial is present, it is placed before the items of the sequence in the calculation,
    and serves as a default when the sequence is empty.
'''
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

# zip(*iterables) –> A zip object yielding tuples until an input is exhausted.
print(list(zip("abcdefg", range(3), range(4))))
