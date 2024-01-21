"""
Created by Ignorant on 2024/1/21
Description: Summary-Public Methods
"""

'''
一、
    print()
    input()
    type()
    id()
    len
    bin()
    oct()
    int()
    hex()
'''

'''
二、
    chr()
    ord()
    max()
    min()
    abs()
    sorted(__iterable: Iterable[SupportsRichComparisonT], *, 
            key: None = None, reverse: bool = False) -> list[SupportsRichComparisonT]
        Return a new list containing all items from the iterable in ascending order.
        A custom key function can be supplied to customize the sort order,
        and the reverse flag can be set to request the result in descending order.
'''
print(chr(48))
print(ord('a'))
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(list1))
print(min(list1))
tuple1 = (3, 5, 2, 4, 6, 1)
print(sorted(tuple1))

'''
三、
del <object>
in      string list tuple dictionary
not in  string list tuple dictionary
is
'''

'''
四、
    +   string list tuple
    *   string list tuple
    -   set
    &   set
    |   set
    ^   set
'''
