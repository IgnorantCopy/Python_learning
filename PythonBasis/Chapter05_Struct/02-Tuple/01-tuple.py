"""
Created by Ignorant on 2024/1/20
Description: Tuple
"""

# compared with list, the elements in tuple cannot be added  / deleted / modified
# one-element tuple cannot miss ,
str1 = ('a')
tuple1 = ('a',)
print(type(str1))
print(type(tuple1))

# index / slice
tuple2 = ('a', 'b', 'c')
print(tuple2[0])
print(tuple2[1:])

# transfer
list1 = list(tuple2)
list1.append('d')
tuple2 = tuple(list1)
print(tuple2)
