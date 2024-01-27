"""
Created by Ignorant on 2024/1/25
Description: Reference
"""
import sys

list1 = [1, 2, 3, 4, 5]
list2 = list1
list3 = list2
'''
getrefcount(__object: Any) -> int
    Return the reference count of object.
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to getrefcount().
'''
print(sys.getrefcount(list1))
del list1
print(sys.getrefcount(list2))
del list2
print(sys.getrefcount(list3))
print()


def test1(n):
    for i in range(n):
        print(i, end=' ')
    print()


def test2(l):
    if isinstance(l, list):
        l.append(7)


n1 = 10
test1(n1)
print(n1)
print()

list1 = [1, 2, 3, 4, 5, 6]
test2(list1)
print(list1)
