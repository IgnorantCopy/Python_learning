"""
Created by Ignorant on 2024/1/31
Description: Iterator
"""
from collections.abc import Iterable

'''
iterable objects:
    generator / tuple list set dict str
'''
print(isinstance("abcd", Iterable))
generator = (i for i in range(100))
print(isinstance(generator, Iterable))

'''
Iterator:
    迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置的对象
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束
    迭代器只会往前不会后退
    
    定义：可以被next()函数调用并且不断返回下一个值的对象称为迭代器(Iterator)
'''

# iterable != iterator
list1 = [1, 2, 3, 4, 5]
# print(next(list1)) ==> 'list' object is not an iterator
list1 = iter(list1)
print(next(list1))
