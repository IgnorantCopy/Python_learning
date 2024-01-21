"""
Created by Ignorant on 2024/1/19
Description: List Operations
"""

import random

'''
add
    1.append(self, __object: _T) -> None
        Append object to the end of the list.
    2.extend(self, __iterable: Iterable[_T]) -> None
        Extend list by appending elements from the iterable.
    3.insert(self, __index: SupportsIndex, __object: _T) -> None
        Insert object before index.
'''
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(list1)
list1.append('d')
print(list1)
list1 = list1 + list2
print(list1)
list1.extend(list2)
print(list1)
list1.insert(-2, 1)
print(list1)
print()

'''
delete
    1.pop(self, __index: SupportsIndex = -1) -> _T
        Remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.
    2.del
        del list[index]
        del list: delete list from memory
    3.remove(self, __value: _T) -> None
        Remove first occurrence of value.
        Raises ValueError if the value is not present.
    4.clear(self) -> None
        Remove all objects from the list
'''
list1.pop()
list1.pop(3)
del list1[3]
print(list1)
if 3 in list1:
    list1.remove(3)
print(list1)

# delete all numbers
i = 0
while i < len(list1):
    if str(list1[i]).isdigit():
        list1.pop(i)
    else:
        i += 1
print(list1)

list1.clear()
print(list1)
del list1
# print(list1) ==> X
print()

# edit: list[index] = value
list2[-1] = 1
print(list2)
print()

'''
find
    1.element in list -> bool
    2.index(self, __value: _T, __start: SupportsIndex = 0, __stop: SupportsIndex = sys.maxsize) -> int
        Return first index of value.
        Raises ValueError if the value is not present.
    3.count(self, __value: _T) -> int
        Return number of occurrences of value.
'''
print(2 in list2)
print(list2.index(2))
print(list2.count(1))
print()

list3 = []
for i in range(8):
    list3.append(random.randint(1, 20))
print(list3)

# reverse(self) -> None: reverse the list
list3.reverse()
print(list3)

'''
sort(self: list[SupportsRichComparisonT], *, key: None = None, reverse: bool = False) -> None
    Sort the list in ascending order and return None.
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).
    If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
    The reverse flag can be set to sort in descending order.
'''
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)
print()

# bubble sort
list4 = [15, 48, 62, 3, 1, 9, 56, 25, 7, 1, 15, 15]
for i in range(len(list4)):
    for j in range(len(list4) - 1 - i):
        if list4[j] > list4[j + 1]:
            list4[j], list4[j + 1] = list4[j + 1], list4[j]
print(list4)
