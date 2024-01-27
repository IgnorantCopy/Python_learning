"""
Created by Ignorant on 2024/1/25
Description: Variable Type
"""

'''
unchangeable variables: id changes if the value changes
    int str float bool tuple
changeable variables: id does not change if the value changes
    list dict set
'''
# unchangeable
a = 100
print(id(a))
a = 98
print(id(a))
print()

# changeable
list1 = [1, 2, 3]
print(id(list1))
list1.append(4)
print(id(list1))
print()

'''
global variable
local variable
only unchangeable variables need to be added by key word 'global'
'''
library = ["Python", "C++", "JavaScript"]
a = len(library)


def add_book(name):
    global a
    print(a)
    if name not in library:
        library.append(name)
        print("add book successfully")
    else:
        print("the book already exists")


add_book("Java")
print(library)
