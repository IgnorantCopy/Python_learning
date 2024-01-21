"""
Created by Ignorant on 2024/1/21
Description: Set Operation
"""

import random

# the feature of set: no repetition and unordered(no index)
list1 = [1, 1, 2, 3, 4, 5, 5, 5, 8, 9, 12, 12, 12, 12]
set1 = set(list1)
print(set1)
set2 = set()
print(len(set2))
print(type(set2))
print()

'''
add
    1.add(self, __element: _T) -> None
        Add an element to a set.
        This has no effect if the element is already present.
    2.update(self, *s: Iterable[_T]) -> None
        Update a set with the union of itself and others.
'''
set2.add("Three")
print(set2)
set2.update(set1)
print(set2)
print()

'''
delete
    1.remove(self, __element: _T) -> None
        Remove an element from a set; it must be a member.
        If the element is not a member, raise a KeyError.
    2.discard(self, __element: _T) -> None
        Remove an element from a set if it is a member.
        If the element is not a member, do nothing.
    3.pop(self, __element: _T) -> None : Remove one element from the set randomly
    4.del set
    5.clear(self) -> None : Remove all elements from the set
'''
set2.remove("Three")
print(set2)
set2.discard(4)
print(set2)
set2.pop()
print(set2)
set2.clear()
print(set2)
del set2
print()

'''
Exercise:
    产生五组4位字母和数字组成的验证码，要求不允许重复
'''
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456890"
strings = set()
while len(strings) < 5:
    temp = ''
    for i in range(4):
        ch = char[random.randint(0, len(char) - 1)]
        temp += ch
    strings.add(temp)
print(strings)
